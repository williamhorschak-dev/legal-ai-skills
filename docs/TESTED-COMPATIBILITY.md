# Tested compatibility — 2026.09.20.2

Format support and observed behavior are separate claims.

| Layer | Evidence | Limit |
|---|---|---|
| Skill packages | Metadata, local links, notices, hashes and ZIP contents are checked by CI. | The host must support the format and expose the needed capabilities. |
| Python helpers | Windows/Linux, Python 3.10/3.12 CI matrix; regression and integrity tests. | Passing code tests do not establish legal accuracy. |
| Document templates | All 11 JSON-backed templates are rebuilt; all 14 Word assets have a byte-bound review record. | Structural/text checks do not render pages. The existing visual review is inherited; see TEMPLATE-QA.md. |
| Claude model behavior | No provider trials recorded for this release. | The optional CLI adapter is tested with simulated subprocess responses only. |
| GPT/OpenAI model behavior | No provider trials recorded for this release. | Codex metadata and prompt exports establish integration format, not answer quality. |
| Other LLMs | Portable prompt inputs and manual result import are available. No provider trials recorded. | No universal compatibility or equivalent-performance claim. |

The 24 scenarios prepare 48 paired trials per repetition. None is marked passed
merely because its fixture exists. There is no published model score, legal-accuracy
score, or attorney approval for this release. Current publication provides tested
helpers and evaluation infrastructure, not a completed cross-model benchmark.

Record future model/host versions, capabilities, dates, raw outputs, baseline
comparison, rubric decisions, repetitions, and remaining failures before changing
this table. Do not translate a later finite test pass into a guarantee of error-free
behavior. See [evaluation protocol](../evals/README.md) and
[GitHub validation runs](https://github.com/williamhorschak-dev/wisconsin-legal-ai-skills/actions/workflows/validate.yml).
