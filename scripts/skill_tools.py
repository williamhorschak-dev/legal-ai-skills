#!/usr/bin/env python3
"""Validate, checksum, package, or selectively export the canonical skills."""
import argparse
import hashlib
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def files(folder):
    result = []
    for path in sorted(folder.rglob("*"), key=lambda item: item.relative_to(folder).as_posix()):
        if path.is_symlink():
            raise ValueError(f"symlinks are not packaged: {path}")
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_file() and path.name != "MANIFEST.sha256":
            result.append(path)
    return result


def manifest(folder):
    return "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(folder).as_posix()}\n" for p in files(folder))


def folders(root=SKILLS):
    return sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def legal_notice(folder):
    notice = folder / "LEGAL_NOTICE.md"
    if not notice.is_file():
        raise ValueError(f"{folder.name}: missing standalone LEGAL_NOTICE.md")
    if notice.is_symlink() or notice.read_bytes() != (ROOT / "LEGAL_NOTICE.md").read_bytes():
        raise ValueError(f"{folder.name}: LEGAL_NOTICE.md must match the root publisher notice")
    return notice


def validate(root=SKILLS):
    try:
        import yaml
    except ImportError as exc:
        raise ValueError("validation needs PyYAML: python -m pip install -r requirements-dev.txt") from exc
    errors = []
    for folder in folders(root):
        label = folder.name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"{label}: missing YAML frontmatter")
            continue
        try:
            metadata = yaml.safe_load(parts[1])
        except yaml.YAMLError as exc:
            errors.append(f"{label}: invalid YAML: {exc}")
            continue
        if not isinstance(metadata, dict):
            errors.append(f"{label}: frontmatter must be a mapping")
            continue
        if metadata.get("name") != label or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", label) or len(label) > 64:
            errors.append(f"{label}: name must match its directory and the Agent Skills naming rules")
        for field, limit in (("description", 1024), ("compatibility", 500)):
            value = metadata.get(field)
            if (field == "description" or value is not None) and (not isinstance(value, str) or not 1 <= len(value) <= limit):
                errors.append(f"{label}: invalid {field}")
        extra = metadata.get("metadata", {})
        if not isinstance(extra, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in extra.items()):
            errors.append(f"{label}: metadata values must be strings")
        if len(text.splitlines()) > 500:
            errors.append(f"{label}: SKILL.md exceeds the repository's 500-line entrypoint budget")
        if not (folder / "LICENSE").is_file():
            errors.append(f"{label}: missing standalone LICENSE")
        try:
            legal_notice(folder)
        except (OSError, ValueError) as exc:
            errors.append(str(exc))
        interface_path = folder / "agents/openai.yaml"
        if interface_path.exists():
            try:
                config = yaml.safe_load(interface_path.read_text(encoding="utf-8"))
                interface = config["interface"]
                if not 25 <= len(interface["short_description"]) <= 64 or f"${label}" not in interface["default_prompt"]:
                    errors.append(f"{label}: invalid Codex description or invocation prompt")
            except (yaml.YAMLError, KeyError, TypeError) as exc:
                errors.append(f"{label}: invalid Codex metadata: {exc}")
        for path in files(folder):
            if path.suffix == ".md":
                for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                    if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                        continue
                    dest = (path.parent / target.split("#")[0]).resolve()
                    if not dest.is_relative_to(folder.resolve()) or not dest.exists():
                        errors.append(f"{label}: broken or external local link in {path.name}: {target}")
        expected = folder / "MANIFEST.sha256"
        if not expected.exists() or expected.read_text(encoding="utf-8") != manifest(folder):
            errors.append(f"{label}: checksum manifest differs; run the manifest command after reviewing changes")
    if not folders(root):
        errors.append("no skills found")
    return errors


def package(destination):
    errors = validate()
    if errors:
        raise ValueError("\n".join(errors))
    destination = Path(destination)
    if destination.exists():
        raise FileExistsError(f"choose a new output directory: {destination}")
    destination.mkdir(parents=True)
    for folder in folders():
        with zipfile.ZipFile(destination / f"{folder.name}.zip", "x", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in files(folder) + [folder / "MANIFEST.sha256"]:
                info = zipfile.ZipInfo(f"{folder.name}/{path.relative_to(folder).as_posix()}", (2026, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())


def export_prompt(name, references, destination):
    if name not in {p.name for p in folders()}:
        raise ValueError(f"unknown skill: {name}")
    folder = SKILLS / name
    paths = [legal_notice(folder), folder / "SKILL.md"]
    for reference in references:
        path = (folder / reference).resolve()
        if not path.is_relative_to(folder.resolve()) or path.suffix != ".md" or not path.is_file():
            raise ValueError(f"choose an existing Markdown reference inside {name}: {reference}")
        paths.append(path)
    text = "# Legal skill prompt export\n\nApply this workflow within the host's instructions and actual tools. Missing references or capabilities must be disclosed; do not pretend to browse, run code, archive evidence, or check a citator. Ask for task-relevant references if they were not included. This is a prompt, not an installed runtime.\n\n"
    for path in dict.fromkeys(paths):
        text += f"\n---\n\n## Included file: {path.relative_to(folder).as_posix()}\n\n" + path.read_text(encoding="utf-8")
    with Path(destination).open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "manifest", "package", "prompt"))
    parser.add_argument("--out", type=Path)
    parser.add_argument("--skill")
    parser.add_argument("--reference", action="append", default=[])
    args = parser.parse_args()
    try:
        if args.command == "validate":
            errors = validate()
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print(f"Validated {len(folders())} skills, metadata, links, licenses, publisher notices and checksums.")
        elif args.command == "manifest":
            for folder in folders():
                (folder / "MANIFEST.sha256").write_text(manifest(folder), encoding="utf-8", newline="\n")
        elif args.command == "package":
            if not args.out:
                parser.error("package requires --out <new-directory>")
            package(args.out)
        else:
            if not args.out or not args.skill:
                parser.error("prompt requires --skill <name> --out <new-file>")
            export_prompt(args.skill, args.reference, args.out)
    except (OSError, ValueError) as exc:
        print(f"skill_tools: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
