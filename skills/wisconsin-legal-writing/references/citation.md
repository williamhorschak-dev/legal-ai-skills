# Citation

**For appellate briefs, Rule 809.19(1)(e)** requires citations
"as set forth in the **Uniform System of Citation and SCR 80.02**." *The Bluebook:
A Uniform System of Citation* is what "Uniform System of Citation" names. Where
SCR 80.02 and the Bluebook conflict on the form of a Wisconsin case cite, **SCR
80.02 controls**. The State Bar's *Wisconsin Guide to Citation* (10th ed., 2021) is
the gap-filler for Wisconsin-specific forms the Bluebook does not reach; it is
followed by convention rather than adopted by rule, so it never overrides either of
the two above.

For circuit court filings and internal memoranda, this skill adopts the same
citation style as a default. Rule 809.19(1)(e) itself governs appellate briefs;
do not cite it as a universal circuit court formatting mandate. Check the rules
and orders applicable to the particular document and preserve a compliant user
style. See the [current rule](https://docs.legis.wisconsin.gov/statutes/statutes/809.pdf).

---

## Default type style: italics

**Use italics consistently in the body under this template's style:**

| Italicized | Example |
|---|---|
| Case names, in full and in short form | *State v. Salinas*; *Locke*, 177 Wis. 2d at 597 |
| Introductory signals | *see*; *see also*; *accord*; *cf.*; *but see*; *e.g.* |
| Short-form and cross-reference words | *Id.*; *id.* at 671-72; *supra*; *infra* |
| Procedural and party-designation phrases | *In re*; *Ex parte*; *State ex rel. Evanow v. Seraphim* |
| Explanatory words inside a cite | *quoting*; *citing*; *aff'd*; *rev'd*; *overruled by* |
| Book and periodical titles | *The Bluebook: A Uniform System of Citation* |
| Emphasis added by the writer | with the parenthetical (emphasis added) |

**Do NOT italicize:**

- Case names in the **table of authorities** on appeal. Those are set plain.
- Statutes, rules, or constitutional provisions: `Wis. Stat. § 971.12(1)` is roman.
- Reporter volumes and page numbers: `369 Wis. 2d 9, 879 N.W.2d 609` is roman.
- The `v.` question: the `v.` **is** italicized, because it is part of the case
  name. Italicize the whole name including the `v.`, not the parties alone.
- Procedural parentheticals: `(Ct. App. 1993)` is roman.

Only the case name itself carries the italics; the citation that follows it does
not. So:

> *State v. Salinas*, 2016 WI 44, ¶ 30, 369 Wis. 2d 9, 879 N.W.2d 609.

italic through `Salinas`, roman from the comma on.

When a signal attaches to a case name, the signal and the name are both italic and
run together:

> *accord State v. Watkins*, 2021 WI App 37, ¶ 24, 398 Wis. 2d 558, 961 N.W.2d 884.

**Getting italics into the .docx.** `scripts/build_filing.py` reads `*asterisks*`
as italic in every body block. Write the body text with the case names already
marked. A body block containing a bare, unmarked `State v. Salinas` produces a
roman case name in the filed document. Correct that style inconsistency when using
this template; do not equate every type-style difference with a filing defect.

---

## Wisconsin cases

**Decided on or after January 1, 2000, public domain cite first, pinpoint by
paragraph.**

```
*State v. Salinas*, 2016 WI 44, ¶ 30, 369 Wis. 2d 9, 879 N.W.2d 609.
*State v. Watkins*, 2021 WI App 37, ¶ 24, 398 Wis. 2d 558, 961 N.W.2d 884.
*State v. Dorsey*, 2018 WI 10, ¶ 33, 379 Wis. 2d 386, 906 N.W.2d 158.
```

The asterisks are the builder's italic markup. In the filed document the case name
is italic and everything after the first comma is roman.

Order under SCR 80.02: public domain cite, then Wisconsin Reports, then North
Western Reporter. Supreme Court is `2016 WI 44`; Court of Appeals is
`2021 WI App 37`. No comma between the year and `WI` / `WI App`. Pinpoint with `¶`,
not a page.

**Decided before January 1, 2000, parallel cite, pinpoint by page.**

```
*State v. Locke*, 177 Wis. 2d 590, 596, 502 N.W.2d 891 (Ct. App. 1993).
*State v. Bettinger*, 100 Wis. 2d 691, 303 N.W.2d 585 (1981).
```

Court of Appeals: include `(Ct. App. YEAR)`. Supreme Court: **omit** the court
name; the bare year signals it.

**Short forms.**

```
*Locke*, 177 Wis. 2d at 597.
*Bettinger*, 100 Wis. 2d at 697.
*Salinas*, 2016 WI 44, ¶ 43.
*Id.* at 671–72.
```

Short-form case names stay italic. So does `Id.`, including its period.

Subsequent citations need include only one of the references, and must stay
internally consistent through the document.

## Statutes

```
Wis. Stat. § 971.12(1)
Wis. Stat. §§ 804.09, 804.12(1)(a)–(c)
Wis. Stat. § 809.19(8)(c)2.
```

- Non-breaking space after `§`. No internal spaces in the subsection string.
- Begin a sentence with `Section 971.12(1) provides…`, never with `§`.
- Full form carries the biennial edition, `Wis. Stat. § 21.36(2) (2013-14)`, but
  Wisconsin brief practice omits it and states the edition **once**, in a footnote
  to the first statutory citation, or parenthetically at the end of the
  introduction:

  > All references to the Wisconsin Statutes are to the 2023-24 version unless
  > otherwise noted.

  or, in-line as the corpus does it:

  > (All citations to the Wisconsin Statutes are to the 2023–24 edition.)

- **The current edition as of August 2026 is the 2023-24 Wisconsin Statutes.** The
  2025-26 edition is not published; Wisconsin publishes biennially and the 2025-26
  biennium does not close until January 2027. Verified against the LRB certification
  page, the official ch. 809 PDF ("Updated 23-24 Wis. Stats."), and 2026 Court of
  Appeals opinions.
- If an offline snapshot of the Wisconsin Statutes is kept locally, capture its
  currency line verbatim (the docs.legis banner reads, for example, *"2023-24 Wisconsin
  Statutes updated through 2025 Wis. Act 247 and through all Supreme Court Orders and
  Controlled Substances Board Orders filed before and in effect on August 5, 2026 ...
  (Published 8-5-26)."*). **A snapshot is offline convenience only — the live
  docs.legis.wisconsin.gov page is always canonical.** Use a local copy to orient fast;
  quote only from the live page re-read in the run.
- The Court of Appeals itself uses, in 2026 opinions:

  > All references to the Wisconsin Statutes are to the 2023-24 version.

  and, where anything else is cited:

  > All references to the Wisconsin Statutes are to the 2023-24 version unless
  > otherwise noted.

- **Re-confirm the edition before filing** once the calendar reaches 2027. Where the
  governing version matters, and in criminal and administrative appeals it often
  does, cite the version in effect at the relevant time and say so, rather than
  relying on the blanket footnote.

Administrative code: `Wis. Admin. Code § DHS 10.33(2)`.
Constitution: `Wis. Const. art. I, § 8`.

## Unpublished opinions, Rule 809.23(3)

**(a)** An unpublished opinion **may not be cited as precedent or authority**,
except to support claim preclusion, issue preclusion, or law of the case, and
except as provided in (b).

**(b)** An unpublished opinion issued **on or after July 1, 2009** that is
**authored** by a member of a three-judge panel or by a single judge under
§ 752.31(2) may be cited **for its persuasive value**. A per curiam opinion,
memorandum opinion, summary disposition order, or other order is **not** an
authored opinion. An opinion cited for persuasive value is not precedent and binds
no court.

**(c)** A party citing an unpublished opinion **must file and serve a copy with the
brief or paper**. On appeal that copy goes in the appendix, and the appendix
certification specifically covers it.

## Citations go in the text, not in numbered footnotes

**Do not use superscript numbered citations.** `In *Gonzalez*,¹ the court held...`
with the cite in a footnote is not Wisconsin practice and should not appear in a
filing here.

Wisconsin uses **in-text citation**: the citation is a sentence or a clause in the
body, right where the proposition is.

- Citation **sentence**, supporting the whole preceding sentence, standing on its
  own and starting with a capital:

  > Whether initial joinder is proper is a question of law. *State v. Salinas*,
  > 2016 WI 44, ¶ 30, 369 Wis. 2d 9, 879 N.W.2d 609.

- Citation **clause**, supporting part of a sentence, set off by commas and
  lowercase:

  > The joinder statute "is to be construed broadly in favor of the initial
  > joinder," *State v. Hoffman*, 106 Wis. 2d 185, 208, 316 N.W.2d 143 (Ct. App.
  > 1982), but broad construction still requires a statutory basis.

**Why not footnotes.** The footnote-citation style is a Bryan Garner advocacy
proposal: move every cite to a footnote so the text reads cleanly. Some judges like
it. Most Wisconsin judges are not expecting it, Rule 809.19(1)(e) requires citations
"as set forth in the Uniform System of Citation and SCR 80.02" (both of which
contemplate in-text citation), and a filing that departs from local convention draws
attention to its form instead of its argument. A pro se or paralegal-drafted filing
has less margin for that than a well-known appellate lawyer does.

There is also a practical cost: the Court of Appeals excludes tables and
certifications from the page count but **not** footnotes, and Rule 809.19(8)(b)
requires footnotes at **11 point** rather than 13. Moving citations into footnotes
shrinks them and buries them.

### What footnotes ARE for

Use them sparingly, and for material that genuinely does not belong in the line of
argument:

1. **The statutory edition note**, attached to the first statutory citation. This is
   the standard and expected use:

   > ¹ All references to the Wisconsin Statutes are to the 2023-24 version unless
   > otherwise noted.

2. A **collateral procedural fact** the reader may want but that would interrupt the
   argument, for example noting that a related case is pending, or that a cited
   document was filed under seal.
3. A **parallel or historical citation** where the point is genuinely secondary.

**Never** put in a footnote: the answer to the opponent's best argument, adverse
authority, or anything you would be uncomfortable having the court skip. If it
matters, it goes in the body. `argument.md` says the same thing about anticipated
responses.

Three or four footnotes in a brief is a lot. A brief with a footnote on every page
is using them to evade a length problem, and the court will read it that way.

### Superscript numbers generally

The only superscript in a Wisconsin filing is a footnote marker. Do not number
authorities, do not use bracketed reference numbers `[1]`, and do not build a
numbered authorities list at the end. The table of authorities on appeal is
alphabetical with page references, not numbered. See `appellate.md`.

## Record citations

- Circuit court, eFiled: `(Doc. 43:2)` is document number, colon, page.
- On appeal: `(R. 43:2)`.
- Transcripts: `(R. 112:15-17)`.
- Appendix: `(App. 7)`.

Never cite a document without a number. Rule 809.19(1)(d) requires "appropriate
references to the record" in the statement of the case, and Rule 809.19(1)(e)
requires them in the argument.

## Quotation practice

- Alterations bracketed: `"[w]ithin the four corners of the document…"`
- Omissions with an ellipsis; do not use one at the start of a quotation that
  already begins mid-sentence with a bracketed capital.
- Block quotes for anything over about fifty words, indented, **11 point** in an
  appellate brief (Rule 809.19(8)(b)).
- `*accord*`, `*see*`, `*see also*`, `*citing*`, `*quoting*` in the ordinary
  Bluebook sense, and all of them italic.
- Parentheticals explaining a case go after the cite and start with a present
  participle: `(requiring "a higher degree of prejudice, or certainty of
  prejudice")`.

## Typographic conventions

- Case names italicized in the body, plain in the table of authorities. See
  **Italics: mandatory** above; this is the rule that gets missed most often.
- Section symbol `§`, paragraph symbol `¶`, en dash in page and paragraph ranges
  (`596–97`, `¶¶ 30–33`).
- **No em dashes** in the default style. Recast with a comma, a colon, or a new sentence.
