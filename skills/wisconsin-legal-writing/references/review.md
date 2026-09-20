# Review mode

For when the user hands over a draft rather than asking for one: "check this,"
"review my brief," "is this ready to file," or a document pasted or attached with no
instruction.

**Review is a different job from drafting and has a different failure mode.** The
drafting failure is a document that does not exist yet. The review failure is telling
someone a filing is fine when it is not. Default to saying the uncomfortable thing.

---

## How to run it

Five passes, in this order. Do not reorder them: mechanical defects are cheap to fix
and finding them first stops you from praising the architecture of a document that
will be rejected at the counter.

Report findings **most serious first**, not in document order. Lead with anything
that would cause the filing to be rejected, missed, or lost.

---

**First: what can you actually see?** Pasted text carries no tab stops, margins,
fonts, or page count, and no access to the record. A .docx can be inspected (unzip it
or read it with python-docx) and should be; plain text cannot. **Say at the top of
the report what you could not verify** rather than passing it silently: caption
geometry, whether a document number is right, whether a quoted response is accurate,
whether the deadline math matches the real service date. A reviewer who reports only
what it could see, without naming what it could not, gives false assurance.

**For a matter involving requests for admission, inventory them before evaluating
affected facts in the draft.** § 804.11's clock is self-executing — an unanswered RFA is deemed
admitted, and a deemed-admitted fact binds the case regardless of what the draft
under review asserts. Before running the five passes below, ask: were RFAs served on
either side, when, and has every one been timely answered? An admission that
contradicts a factual claim in the draft is a Pass-3 defect the internal-consistency
pass will otherwise miss, because nothing in Pass 3 currently checks the draft's
facts against outstanding discovery. See `responding.md` § 1.

## Pass 1: will it be accepted and heard

Check potential filing or hearing defects against the actual governing requirement.
Call an issue blocking only when the rule, order, missing information, or actual
deadline supports that conclusion. Typography preferences alone are craft findings.

- [ ] Caption identifies the actual court, county, parties, case number, and any
      designation required by the applicable form, rule, or order. The template
      geometry in `captions.md` is a default, not an independent filing requirement.
- [ ] **Motion title names the party and the type of relief.** § 802.01(2)(d).
- [ ] Signature and contact details meet § 802.05(1) and § 801.18(12): actual signer
      and role, required contact details, electronic or imaged handwritten signature
      for eFiling, handwritten signature for paper parties. Italics are optional style.
- [ ] **La Crosse: does the notice of hearing state the time the court allotted?**
      Local Rule 435: without it, "the matter will not be heard." This is the single
      most likely way a La Crosse filing silently fails.
- [ ] Deadline computed from the actual trigger, rule, service method/time, court
      calendar, and controlling orders/stays. The § 801.15(5) adjustments apply to
      prescribed periods **after service**, not automatically to every deadline.
- [ ] Proposed order, if any, is .docx with a 3" top margin and **no** judicial
      signature block.
- [ ] A party's § 802.05(3)(a)1 sanctions motion is separate and satisfies the
      safe harbor, including any court-prescribed alternative period.
- [ ] Typeface and layout comply with the actual rule or order. Century Schoolbook
      and Times New Roman are repository defaults, not the only permissible fonts.

## Pass 2: the law

- [ ] Every statutory citation checked against the current official text, including
      amendments and effective dates; record the source currency and the access
      date separately. The subsection is the right one. Common slips:
      § 804.12(1)(**b**) is "evasive or incomplete answer," not (1)(c);
      § 804.01(3)(a) is the protective order provision, and Wisconsin has **no**
      codified privilege-log rule to cite.
- [ ] Post-2000 cases carry the public domain cite first and pinpoint by ¶.
- [ ] Pre-2000 Court of Appeals cases carry `(Ct. App. YEAR)`; pre-2000 supreme court
      cases do not name the court.
- [ ] **Case names italicized** in the body, in full and short form, along with
      signals, `Id.`, and `supra`.
- [ ] Unpublished opinions: authored, post-July-2009, cited only for persuasive
      value, copy filed and served. Rule 809.23(3).
- [ ] **The governing standard fits the proceeding.** Use Wisconsin's "erroneous
      exercise of discretion" in analysis when appropriate; preserve accurate
      quotations and distinguish another jurisdiction's terminology.
- [ ] Local rules checked for the actual county. They differ: Trempealeau Rule 6
      requires numbered proposed findings of fact with record cites on summary
      judgment; La Crosse Rule 502 does not.

### Cite-checking is a separate step and it is not optional

Format is not accuracy. A correctly formatted citation to a case that does not say
what it is cited for is worse than no citation, because opposing counsel will find it
and the court will remember.

For every case cited for a proposition:

1. **Open it.** Confirm the proposition is actually in the opinion, at the pincite
   given.
2. **Check it is still good law.** Reversed, overruled, superseded by statute,
   abrogated in part. The `cite-check` skill in this session handles this if it is
   available; use Shepard's or KeyCite if the user has access to either.
3. **Check the level and the year.** A Court of Appeals case does not bind the
   supreme court; a pre-2000 case may have been superseded by a statutory amendment.
4. **Check the parenthetical.** If you wrote one, it must describe the holding, not
   your argument.

If a brief turns on a potentially changing doctrine, check the current decisions
and the relevant docket. For Wisconsin statutory interpretation, verify *Kalal*
and any later treatment using `wisconsin-legal-interpretation` when available.
A grant of review in another case does not itself overrule precedent, and a
stored docket date does not establish the case's present status.

## Pass 3: internal consistency

- [ ] **Relief in the conclusion matches relief in the motion**, ideally word for
      word. This is the most common substantive defect in an otherwise clean filing.
- [ ] Argument sections appear in the same order as the issues or relief they
      support.
- [ ] Every record citation has a document number. **You usually cannot confirm the
      number is right from a pasted draft; say so.** Flag any date, time, dollar
      figure, or quotation from an opposing paper that you cannot trace to something
      the user supplied. An invented one is the most damaging defect available.
- [ ] Every exhibit referenced is actually attached and identified.
- [ ] Party short forms defined once and used consistently.
- [ ] Dates in the brief match the dates in the record.
- [ ] Nothing promised earlier in the brief ("as discussed below") goes undelivered.

## Pass 4: the argument

This is where a review earns its keep. Apply `argument.md`.

- [ ] **Point headings are propositions**, not labels. If the court read only the
      headings, would it know what to do and why?
- [ ] Each section runs rule → sub-rule → application → answer, with the application
      the longest part. Flag any section that is mostly law recitation.
- [ ] **Factor tests are walked, not asserted.**
- [ ] The best argument against the filing is named and answered.
- [ ] Adverse authority is cited and dealt with, not omitted.
- [ ] Bad facts are surfaced, not buried.
- [ ] **Is there an argument here that should be cut or narrowed?** Explain why,
      after checking preservation, jurisdiction, and alternative grounds for relief.
- [ ] Length proportionate: under ~10 pages for a non-dispositive motion brief, under
      ~25 for summary judgment, absent a scheduling order saying otherwise.
- [ ] No intensifiers ("clearly," "plainly," "obviously"), no rhetorical questions, no
      em dashes.

## Pass 5: tone, voice, and credibility

Especially for a pro se filing against represented parties. See `argument.md` § 9.

- [ ] **No procedural grievance mixed into a merits argument.** If misconduct
      matters, it belongs in its own motion with its own relief.
- [ ] No indignation. Facts, not adjectives.
- [ ] Nothing included because it felt good to write.
- [ ] Nothing overstated. One overclaimed case contaminates the whole brief.
- [ ] Wisconsin authority used where Wisconsin authority exists.
- [ ] **Fits the requested voice.** Run `voice.md` § 8: remove padding, preserve
      supplied dates and record detail, and compare with supplied writing examples
      when available. Do not force paragraph-length variation or stock formulas,
      or infer the signer's identity or personal voice from this repository.
- [ ] Local AI disclosure rule checked for this county and this judge.

---

## How to report

**Structure the response as:**

1. **Blocking**: will be rejected, will not be heard, or will miss a deadline. If
   there are none, say so in one line.
2. **Substantive**: wrong law, unsupported citation, mismatched relief, an argument
   that should be cut.
3. **Craft**: structure, ordering, length, tone.
4. **What is working.** Brief and specific. Not a compliment sandwich; a reviewer who
   only reports faults is not calibrating the writer.

**Quote the specific language you are flagging** and give the fix, not just the
diagnosis. "Point heading III.B is a label" is not useful. "Point heading III.B reads
'Discovery.' Make it the proposition: 'Acme's possession-of-third-parties objection
does not answer the request, because § 804.09 reaches documents within a party's
control.'" is.

**Do not rewrite the document unless asked.** Review and rewriting are different
requests, and a user who wanted a rewrite will say so.

**Say when something is fine.** A review that manufactures findings to look thorough
trains the writer to ignore reviews.

## The question to answer at the end

**What remains to be verified or corrected before filing?** Put the most consequential
item first. State the scope of the review and unresolved issues. A style pass or
automated check alone cannot establish filing readiness, validate the record, or
authorize signing, serving, or filing the document.
