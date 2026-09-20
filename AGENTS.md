# Maintaining this repository

Canonical skills live in `skills/`. Keep each skill independently usable with its
references, scripts, license, and optional host metadata. Provider adapters must not
duplicate or weaken substantive legal guidance.

Verify material legal corrections against current primary sources and record the
retrieval date and affected scope in the assessment/source notes. Preserve the author's
style as a preference, not a mandatory statewide rule. Use synthetic facts in tests and
templates; do not add private matter records, credentials, source archives, or paid
content to this public repository.

Run `python -m unittest discover -s tests -v` and
`python scripts/skill_tools.py validate` after consequential changes. Rebuild affected
JSON-backed templates into a scratch directory and inspect the rendered pages before
replacing the bundled DOCX assets. Update manifests only after reviewing changes.

Structural validation, script tests, source checks, and visual checks answer different
questions. Report their limits. Do not describe a generated document as filing-ready
solely because a script or linter passed.

Keep Git authorship with the human contributors. Do not add AI-provider co-author
trailers or generated-by signatures to commits or pull requests.
The shared `.claude/settings.json` disables Claude Code's automatic attribution;
see the [attribution setting](https://code.claude.com/docs/en/settings-reference#attribution).
