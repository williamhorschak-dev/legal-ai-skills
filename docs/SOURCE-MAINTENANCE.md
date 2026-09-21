# Maintaining legal references

[legal-sources.json](legal-sources.json) starts with frequently used procedural
rules, interpretation guidance, and publication boundaries. It is not an inventory
of every authority mentioned in the skills. Add a record when materially changing
an uncovered legal proposition.

Each record identifies the proposition, official source URL, operative-version
description, review scope/date, review basis, affected files, and review interval.
`focused_primary_check` means the identified passage was read for that limited
purpose. `inherited_review` carries forward a documented earlier review without
pretending a new one occurred. `needs_primary_review` records an actual gap.
Neither a date nor an accessible URL establishes current law or subsequent treatment.

```sh
python scripts/source_registry.py validate
python scripts/source_registry.py due --as-of 2026-09-20
```

`validate` checks record structure and file references, without network requests.
`due` returns `1` when review is due or pending, `0` when no reminder is due, and
`2` for invalid data. These are maintenance reminders, not legal-currency verdicts.
Review before releases and when an amendment, court order, or reported defect
affects an entry; intervals are upper bounds for routine reminders, not safe
reliance periods. No automatic scheduler or third-party notification is enabled.

For each review, retrieve the official text, establish the applicable version and
effective date, read the proposition in context, and inspect subsequent history
or treatment appropriate to the proposed claim. Record what actually happened,
including retrieval failure or absent citator coverage. Review every affected file
and its examples/templates together. Update the date only after the described
review, then refresh skill manifests and run validation.

Keep a private matter's source archive separate. The citation helper's optional
structured provenance records origin, retrieval timestamp, operative version,
extraction method, and an original-file/hash link. That is evidence for a specific
run, not content for the public register. Do not publish private or licensed source
archives as maintenance examples.
