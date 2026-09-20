import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("skill_tools", ROOT / "scripts/skill_tools.py")
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


class PackagingTests(unittest.TestCase):
    def test_manifest_uses_platform_independent_case_sensitive_path_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("SKILL.md", "LICENSE", "agents/openai.yaml", "references/example.md"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(name, encoding="utf-8")
            entries = [line.split("  ", 1)[1] for line in tools.manifest(root).splitlines()]
            self.assertEqual(entries, ["LICENSE", "SKILL.md", "agents/openai.yaml", "references/example.md"])

    def test_packages_are_deterministic_complete_and_independently_licensed(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = Path(directory)/"first", Path(directory)/"second"
            tools.package(first)
            tools.package(second)
            for folder in tools.folders():
                archive_path = first / f"{folder.name}.zip"
                self.assertEqual(archive_path.read_bytes(), (second/archive_path.name).read_bytes())
                with zipfile.ZipFile(archive_path) as archive:
                    names = archive.namelist()
                    self.assertTrue(all(item.create_system == 3 for item in archive.infolist()))
                    self.assertIn(f"{folder.name}/SKILL.md", names)
                    self.assertIn(f"{folder.name}/LICENSE", names)
                    self.assertIn(f"{folder.name}/MANIFEST.sha256", names)
                    self.assertTrue(all(name.startswith(folder.name+"/") for name in names))
                    self.assertFalse(any("__pycache__" in name for name in names))
                    for file in tools.files(folder):
                        self.assertEqual(archive.read(f"{folder.name}/{file.relative_to(folder).as_posix()}"),file.read_bytes())
            with self.assertRaises(FileExistsError):
                tools.package(first)

    def test_manifest_changes_when_source_bytes_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.md"
            source.write_text("first", encoding="utf-8")
            before = tools.manifest(root)
            source.write_text("changed", encoding="utf-8")
            self.assertNotEqual(before, tools.manifest(root))

    def test_prompt_export_is_selective_and_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/"prompt.md"
            tools.export_prompt("cite-check", ["references/verification.md"], target)
            text = target.read_text(encoding="utf-8")
            self.assertIn("Included file: SKILL.md", text)
            self.assertIn("Included file: references/verification.md", text)
            self.assertNotIn("Included file: references/sources.md", text)
            with self.assertRaises(FileExistsError):
                tools.export_prompt("cite-check", [], target)
            self.assertEqual(text, target.read_text(encoding="utf-8"))

    def test_prompt_export_refuses_traversal_and_unknown_skills(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/"prompt.md"
            for name, references in (("unknown", []), ("cite-check", ["../../README.md"]), ("cite-check", ["scripts/cite_check.py"])):
                with self.subTest(name=name, references=references), self.assertRaises(ValueError):
                    tools.export_prompt(name, references, target)
                self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
