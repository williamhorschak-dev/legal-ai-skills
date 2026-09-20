# The Six Checks — Procedure, Standards, Evidence

Every check runs against the **local copy in `sources/`** — never memory, never a
search-result snippet. Verification is per *use*, not just per authority: a case quoted
three times gets each quote checked; a statute cited for two propositions gets both
checked. Acquire once per authority; verify per use; verify the authorities the argument
stands on before string-cite filler, so an interrupted run fails gracefully.

Cases get all six checks (Check 6 where record cites appear). Statutes, regulations, and
rules get Checks 1, 2, 3 (subsection-level locators), 4 (vintage + validity), and 5.

## The evidence log — write it as you go

Use [evidence-tool.md](evidence-tool.md) and `scripts/cite_check.py` for the supported
inventory/log/report schema. Plain-text substring matching can be automated; holdings,
attribution, treatment, OCR corrections, and altered quotations require source review.
If execution is unavailable, identify the report as manual and record the same evidence.
The following older illustrative record explains the evidence fields; use the tool's
schema (including `document_sha256`, `note`, and its check names) for executable runs:

```json
{"cite": "457 U.S. 800", "use": "quote-3", "check": "verbatim",
 "file": "opinions/457-US-800 - Harlow v Fitzgerald (1982).pdf",
 "sha256": "…", "locator": "[*818]", "matched": "…normalized matched text…",
 "result": "pass", "note": ""}
```

The supplied generator reports `RECORDED PASS` only for complete passing evidence
records. This status is a summary of recorded checks, not an independent legal judgment.
An interrupted run may add missing checks. Corrections or changed drafts/sources use a
new run; duplicate check records cannot overwrite prior failures. Manual review is
allowed and must be identified as such, with source evidence and limitations.

## Check 1 — Verbatim quotes

**Standard.** Every quoted passage matches the source character for character after
normalizing *only*:

- straight ↔ curly quotes and apostrophes; hyphen/dash variants when OCR-induced
- whitespace runs and line breaks; **hyphenation across line breaks** (`judg-` + newline
  + `ment` → `judgment`)
- ligatures (ﬁ → fi) and soft hyphens from PDF extraction
- **pagination artifacts**: star-page markers (`[*805]`), page anchors, running headers
  and footers, and line numbers are stripped before matching — but record which page
  marker bracketed the match, because that is the pincite evidence (one function, both
  jobs). Watch two-column PDFs for scrambled column order in extracted text.

Everything else — a dropped "the," a tense change, a reordered clause — is a mismatch.
Report it; do not average it away.

**Alterations must be shown.** Brackets for changed or added material; ellipses for
omissions (never at the start of a quote; never splicing two sentences into one without
showing it); *(emphasis added)* when the emphasis isn't in the original.

**"(Cleaned up)" is narrow.** It permits removing internal quotation marks, brackets,
ellipses, internal citations, and footnote markers, and conforming capitalization —
**nothing else. Every retained word must still match character for character**, and the
verifier confirms the removed material actually existed in the source. A "(cleaned up)"
quote whose words differ from the source is a `FLAG: QUOTE` like any other.

**Attribution — right voice.** Verify the quote comes from where the draft implies:
majority/lead opinion unless labeled. Language from a concurrence, dissent, footnote, or
a party's argument the court was *describing* (or rejecting) must say so — a verbatim
quote in the wrong voice is `FLAG: ATTRIBUTION`.

**Attribution — quotes of quotes.** If the quoted language sits inside quotation marks in
the source, the court is quoting someone else. Identify the original. The draft either
carries the correct `(quoting …)` chain, or — if it actually relies on the original's
holding — the original is acquired and verified as its own authority. "(Cleaned up)"
strips exactly the quotation marks that reveal this; check for it deliberately whenever
that convention appears.

**OCR.** Detect image-only PDFs before matching (rule of thumb: under ~200 characters of
extracted text per page). OCR the file or check mismatches against the page image — the
image controls, in both directions; never conform a quote to an OCR error. If no image
can be reviewed in this environment, the check is `UNVERIFIED — OCR-only copy, image not
reviewable here`, not a guess.

## Check 2 — Citation accuracy and format

**Existence first.** If a citation-lookup integration is available, inspect its actual
tool schema, coverage, limits, and result semantics before using it. Do not assume a
specific MCP tool name or batch limit. Whether lookup is automated or manual, resolve
a disagreement between the draft's case name and the reporter location against the
primary text. Track all remaining inventory items so truncated results cannot pass.

**Against the copy, verify:**

- **Caption** — party names as the source has them, abbreviated per the citation
  convention the draft uses.
- **Reporter, volume, first page** — the case begins where the cite says. Wisconsin
  public-domain cites: year, court designator, sequential number — and every parallel
  cite (`Wis. 2d`, `N.W.2d`) verified against a copy, not assumed.
- **Court and year** — as the copy states them.
- **Subsequent-history notation** — matches what the citator/docket shows, where the
  convention requires it.
- **Statutes** — the section exists in the archived vintage and contains the cited
  language; subsections point where the draft says; the date parenthetical matches the
  archived copy's `vintage`/`updated_through`.
- **Format** — the Bluebook layer in `references/bluebook.md`: italics, year
  parentheticals, statute date parentheticals, short forms. Formatting failures are
  `FLAG: FORMAT` (they never block a substantive `VERIFIED`, but they ship in the report).

**Corrections are identity-locked.** A citation may be conformed only to the local copy
that already pins the authority's identity — the corrected cite must resolve to the same
file in `sources/`. A wrong first page or divergent caption that could belong to a
*different* case is `FLAG: CITE`, not a typo fix; if the "typo" hypothesis requires
choosing between two plausible authorities, it is not a typo. Every applied correction is
logged old → new with the pinning file.

## Check 3 — Pincites

**Standard.** The quoted or relied-on material appears on the exact page(s) or ¶(s)
cited.

- Pincites verify only against a copy showing the cited pagination scheme: reporter star
  pages, official PDFs whose numbering matches the reporter, or Wisconsin ¶ numbers.
  **PDF viewer page position is not pagination.**
- Wisconsin post-2000: pincite by paragraph (`¶ 23`); the official slip PDF's ¶ numbers
  are the check.
- Recent U.S. Supreme Court: pincite the slip opinion (`slip op., at 12`) until final
  U.S. Reports pagination exists in an archived copy — never an invented page.
- Quotes spanning a page break cite the span (`800-01`); confirm both ends.
- Short forms and `id.` chains inherit nothing: each resolved use gets its own pincite
  check against its own locator.
- If no obtainable copy shows the needed pagination, the pincite is `UNVERIFIED —
  pagination unavailable in accessible copies`. Do not transfer a pincite from memory,
  another brief, or a headnote.

## Check 4 — Good law and citability

**Standard.** Every case relied on is screened for negative subsequent treatment as of
the run date; the screen used and its result are recorded — and the screen's *strength*
is part of the result.

1. **Shepard's (Nexis Uni) or KeyCite (Westlaw)** — the only screens that support a
   `GOOD` result. Record the signal and every negative entry verbatim.
2. **CourtListener citing-cases scan** — scan the "cited by" list for reversal,
   overruling, abrogation, supersession language. This is a *partial* screen: it misses
   implicit abrogation, supersession by statute, depublication, and anything the citing
   court said without the magic words, and the citation graph is incomplete. **Best
   possible result: `CAUTION — no citator run`, stated in those words.**
3. **Docket check** — for recent opinions, confirm on WSCCA / RECAP that the specific
   decision was not reversed, vacated, withdrawn, or depublished on review.

Results: `GOOD` (citator run, clean) · `CAUTION` (criticized/distinguished on the
relevant point, pending review, or no citator available — the user decides) · `NEGATIVE`
(`FLAG: NEGATIVE HISTORY` — say whether the negative treatment touches the proposition
cited) · `UNKNOWN` (no screen reachable — an `UNVERIFIED` state, never a pass).

**Statutes and regulations.** Good law means: the archived copy is the version in force
at the operative time (conduct vs. filing date — ask the user when unclear); history notes
and currency banners show no intervening amendment to the cited language; no case in the
screen holds the provision unconstitutional or preempted as applied. The vintage rule
extends to regulations. Use dated eCFR text within its point-in-time coverage, or govinfo
annual editions plus intervening Federal Register changes; verify the effective date.

**Citability screens.**

- **Wisconsin unpublished opinions — Wis. Stat. § (Rule) 809.23(3).** In substance: an
  unpublished opinion is not precedent; an *authored* (judge-signed) unpublished opinion
  issued on or after July 1, 2009 may be cited for persuasive value; per curiam,
  memorandum, and summary dispositions may not be cited except to support claim
  preclusion, issue preclusion, or **the law of the case**. **§ 809.23(3)(c): a party
  citing an unpublished opinion must file and serve a copy with the brief** — the
  archived PDF alone does not file or serve it; list the separate action required. Cite unpublished
  Wisconsin opinions by docket number and date (e.g., *Caption*, No. 2019APXXXX,
  unpublished slip op. (Wis. Ct. App. Mar. 3, 2020)) — never with an invented
  public-domain cite. Download the current rule text into `sources/statutes/` during the
  run and verify against it rather than trusting this paragraph.
- **Federal nonprecedential dispositions — FRAP 32.1.** The rule bars courts from
  prohibiting or restricting citation of federal judicial dispositions designated
  "unpublished"/"non-precedential" **issued on or after January 1, 2007** — it grants no
  precedential weight; such a disposition remains nonprecedential, and the deciding
  circuit's current local rule (verify it during the run) governs how it is treated.
  **FRAP 32.1(b):** if the disposition is not in a publicly accessible database, a copy
  must be filed and served — same "Copies to file" list.
- Any citation the screen bars or restricts: `FLAG: NONCITABLE`, with the rule quoted.

## Check 5 — Proposition support

**Standard.** The authority must actually say what the draft uses it for. This is the
check that catches the dominant real-world AI failure: a real case, correctly cited,
verbatim-quoted — for a proposition it never decided.

Procedure, bounded so it stays verification rather than lawyering:

1. For each use, state the draft's proposition in one line.
2. Find, at the cited pincite, the sentence or passage that states it, and **quote that
   passage verbatim into the evidence log and report**.
3. If the support is there: pass, with the quoted passage as evidence.
4. If supporting the proposition requires inference, synthesis of multiple passages,
   analogy, or extension beyond the facts — that may be perfectly good lawyering, but it
   is not verification: status `FLAG: PROPOSITION`, marker `[NEEDS USER]`, with the
   closest passage quoted so the user can judge the gap. Never `VERIFIED` on inference.
5. Watch for propositions resting on dicta, a dissent, or a holding later limited —
   cross-reference Checks 1 (voice) and 4 (treatment).

## Check 6 — Record and appendix cites

Record cites (`R. 12:3`, `App. 45`, CCAP document numbers) assert what the *record*
contains. Verify against the matter's record: the case-file archive, the appendix being
assembled, or the docket. The cited document exists, and the cited page contains the
asserted fact — quoted into the log like any other evidence. If the record set is not
available to this session, every record cite is `UNVERIFIED — record not accessible this
run`, listed together in the report; never assume a record cite from context. Format
follows the forum's rule (e.g., Wis. Stat. § 809.19 record-cite requirements for
Wisconsin appellate briefs — verify the current rule during an appellate run).

## Recording results

Each use's row carries the outcome of each applicable check plus overall status —
`RECORDED PASS` only when every applicable check has passing evidence recorded. Review
the underlying judgments before calling a citation verified. `sources/
_index.md` gains a row per acquired file (File | Authority | Origin | URL | Retrieved |
Pagination | Notes).

Two disciplines make the record trustworthy:

- **Name the copy and locator for every check.** "Verbatim per `opinions/457-US-800 -
  Harlow v Fitzgerald (1982).pdf` at [*818]" is auditable; "verified" alone is a vibe.
- **Report failures in the source's own words.** A flag that quotes the opinion's actual
  sentence lets the user fix the draft in one pass, cold.
