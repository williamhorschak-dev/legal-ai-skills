# Reliability implementation record

The follow-up assessment at commit `073dc42` identified a citation-log separator
defect, UTF-8 BOM rejection, and conflicting interpretation-template guidance.
The first two are corrected with regression cases, including preserving existing
bytes and rejecting malformed inputs. The template now agrees with its reference
about enacted construction directives and limited extrinsic confirmation.

On September 20, 2026, the official [SEIU opinion, 2025 WI 29](https://www.wicourts.gov/sc/order/DisplayDocImage.pdf?docId=977376)
was consulted for paragraphs 8, 10–12 and 32. This was a focused source check of
intrinsic sources and confirmation of an already established plain reading.
Applying that distinction to enacted construction directives is identified as
an application of the intrinsic-source principle, not a holding about every
directive. No new citator review is claimed.

[SCR chapter 23](https://www.wicourts.gov/sc/rules/chap23.pdf) was read for the
publication/support distinction in SCR 23.01 and 23.02, including the general
information provision and supervised-work exceptions. Publication notices remain
unchanged; this is not an opinion on anyone's compliance. The chapter 990 HTML
retrieval failed, so its new registry record remains pending rather than receiving
a fabricated verification date. Other procedural records carry forward the
specific earlier review in ASSESSMENT-2026-09-20.md.

The model-evaluation suite, prompt profiles, source register, template regression
checks, and release builder implement the remaining maintenance recommendations.
The suite records missing provider results honestly. No Claude or OpenAI provider
trials ran for this release. Simulated subprocess tests validate the collector's
mechanics only.

Versioned release downloads and branch protection are operational controls,
separate from legal and behavioral review. See the release's BUILD.json, checksum
file, compatibility record, CI checks, and repository settings for their actual state.

The expanded suite contains 67 tests. The local Windows run passed with two
symlink tests skipped because the account lacked symlink-creation privilege; the
hosted matrix supplies separate platform evidence. Static skill scans found no
critical pattern. The writing skill's sole warning was its existing ImportError
message showing a pip command; inspection confirms it prints an installation
instruction and does not execute that command. This was not a live advisory audit.
