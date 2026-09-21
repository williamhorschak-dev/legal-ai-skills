#!/usr/bin/env python3
"""Validate source-maintenance records and list reviews due; never certify law."""
import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/legal-sources.json"


def validate(data, root=ROOT):
    errors, seen = [], set()
    for item in data.get("sources", []):
        label = item.get("id", "<missing>")
        if label in seen:
            errors.append(f"duplicate source: {label}")
        seen.add(label)
        for key in ("id", "authority", "proposition", "operative_version", "review_scope", "review_basis"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                errors.append(f"{label}: missing {key}")
        if urlparse(item.get("url", "")).scheme != "https" or not urlparse(item.get("url", "")).netloc:
            errors.append(f"{label}: expected an official HTTPS source URL")
        if item.get("status") not in {"focused_primary_check", "inherited_review", "needs_primary_review"}:
            errors.append(f"{label}: unknown review status")
        try:
            reviewed = date.fromisoformat(item["last_reviewed"]) if item.get("last_reviewed") else None
            if reviewed is None and item.get("status") != "needs_primary_review":
                errors.append(f"{label}: reviewed status needs a date")
            if not isinstance(item.get("review_interval_days"), int) or isinstance(item["review_interval_days"], bool) or not 1 <= item["review_interval_days"] <= 365:
                errors.append(f"{label}: review interval must be 1-365 days")
        except (ValueError, TypeError, KeyError):
            errors.append(f"{label}: invalid review date or interval")
        paths = item.get("affected_files", [])
        if not paths:
            errors.append(f"{label}: no affected files")
        for relative in paths:
            target = (root / relative).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f"{label}: missing or unsafe affected file {relative}")
    if not seen:
        errors.append("source registry is empty")
    return errors


def due_sources(data, today):
    due = []
    for item in data["sources"]:
        last = date.fromisoformat(item["last_reviewed"]) if item.get("last_reviewed") else None
        deadline = last + timedelta(days=item["review_interval_days"]) if last else None
        if item["status"] == "needs_primary_review" or deadline is None or deadline <= today:
            due.append({"id": item["id"], "status": item["status"], "review_due": deadline.isoformat() if deadline else None,
                        "url": item["url"], "affected_files": item["affected_files"]})
    return due


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "due"))
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        errors = validate(data)
        if errors:
            raise ValueError("\n".join(errors))
        if args.command == "validate":
            print(f"Validated {len(data['sources'])} maintenance records; legal currency was not checked.")
            return 0
        due = due_sources(data, args.as_of)
        print(json.dumps({"as_of": args.as_of.isoformat(), "due": due, "meaning": "Review reminders, not a determination of legal currency."}, indent=2))
        return 1 if due else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"source_registry: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
