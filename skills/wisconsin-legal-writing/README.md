# wisconsin-legal-writing

William Horschak is not a licensed attorney. This is a published research and
drafting tool; the maintainer does not offer legal services through this project.
Read the [legal notice and public support boundaries](LEGAL_NOTICE.md).

Default style for filings in Wisconsin circuit courts (La Crosse, Trempealeau, and
the western tier) and the Wisconsin Court of Appeals.

```
SKILL.md                        entry point
references/captions.md          caption geometry and every variant
references/circuit-court.md     document skeletons, placement, timing
references/appellate.md         Rule 809.19 / 809.81 / 809.801
references/citation.md          SCR 80.02, statutes, record cites
references/memoranda.md          objective research memos; work product; the UPL boundary
references/memo-worked-example.md  annotated walkthrough of a model memo
references/responding.md        response clocks, RFA deemed-admission trap, two-way cost exposure
references/voice.md             writing in the signer's voice; humanizer hybrid; AI disclosure
references/argument.md          argument craft; the pro se credibility problem
references/worked-example.md    annotated walkthrough of a model motion (fictionalized)
references/review.md            five-pass review of a finished draft
references/standards-of-review.md   canonical formulations and terminology traps
references/practice-areas.md    public records, small claims, substitution, discovery
references/signature-blocks.md  pro se and attorney blocks; use the actual signer
references/letters.md           correspondence to the court
references/checklists.md        pre-filing checks by document type
scripts/build_filing.py         spec.json → .docx; validates supported structure, not legal readiness
scripts/make_templates.py       rebuild JSON-backed templates into an explicit scratch directory
assets/                         fourteen ready-to-fill templates (see assets/README.md)
```

Derived from a corpus of Wisconsin circuit court filings (consumer civil,
public-records mandamus, and criminal matters in La Crosse and Trempealeau
Counties), checked against Wis. Stat. chs. 801-806 and 809, SCR 80.02, and
the Director of State Courts' eFiling technical requirements.
