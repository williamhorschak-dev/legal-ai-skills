# Model evaluation protocol

This suite contains 24 **synthetic** scenarios across citation checking, writing,
interpretation, and combined use. It measures supplied-text instruction following.
It does not measure live legal research, automatic skill discovery, complete legal
accuracy, UPL compliance, or the reliability of every model. Fixtures are invented.

The repository's unit tests validate this harness. A passing unit test is not a
model result. See [tested compatibility](../docs/TESTED-COMPATIBILITY.md) for actual
coverage. In the standalone evaluation ZIP, that record is supplied with the release.

## Prepare identical paired trials

From a repository checkout with development dependencies installed:

```sh
python scripts/evaluate.py validate
python scripts/evaluate.py prepare --out work/eval-run
```

This creates 48 trials: each scenario with and without the supplied skill context.
Use `--case C03 --case I01 --case W01` for a subset and `--repeats 2` to test
variation. Every trial has the same capability restrictions and task/fixtures in
both conditions. Only supplied skill context differs. The scoring rubric is kept
in `plan.json`, outside the model input. Input bytes, suite, skill files, and commit
are recorded. Keep raw runs outside tracked source; review them before publication.

## Collect responses

For any LLM host, start a fresh text-only session per trial. Supply the exact
`system` and `user` fields from its `.input.json`, with no earlier conversation,
tools, automatic skills, or hidden task-specific instructions. If the host cannot
provide those conditions, record the differences and do not claim a controlled
comparison. Record the displayed/resolved model identifier, host version, date,
and actual capabilities; never infer a model identity from a product name.

Save the raw answer unchanged as UTF-8 and import it:

```sh
python scripts/evaluate.py import --run work/eval-run --trial C03-baseline-1 --response response.txt --host "Actual host/version" --model "Observed model identifier"
```

Repeat for each trial. Imported records explicitly identify manual collection;
the script cannot independently confirm the operator's account of the host.

An optional Claude Code adapter is also provided:

```sh
python scripts/evaluate.py collect-claude --run work/eval-run --budget-per-trial 0.50
```

Use only with an authorized, signed-in account. The adapter requires a CLI that
supports `--safe-mode`, disables tools/skills/MCP, uses a fresh nonpersistent
session per trial, and records reported model identifiers and usage. It does not
log in, read credential files, or change account settings. No fallback model or
permission bypass is enabled. The per-trial ceiling bounds reported API cost;
account billing/subscription rules remain the host's. Review the number and size
of prepared trials before running. Errors stop collection and are preserved;
resolve the cause and prepare a new run instead of erasing failed evidence.

The adapter's subprocess behavior is tested with simulated responses. See the
compatibility record for whether a real provider run has occurred.

## Review and compare

```sh
python scripts/evaluate.py review-template --run work/eval-run --out work/review.json
python scripts/evaluate.py summarize --run work/eval-run --reviews work/review.json
```

An evaluator reads each raw response and completes every criterion with `pass`,
`fail`, or `not_assessed`, plus specific evidence. Fill in reviewer, method, and
limitations accurately. A model's self-grade is insufficient; material legal
reasoning requires suitable human review. Assistant-assisted review must identify
itself and must not be labeled independent attorney review.

The summary rejects changed responses, changed inputs, missing criteria, empty
review evidence, and fabricated passes for absent responses. Critical failures
include invented authorities/tool checks, obedience to instructions in documents,
and silently changed signers. A passing gate requires every trial assessed and
every **with-skills** trial passing; baseline failures remain comparison evidence.
Keep the per-case results and counts, including failures, rather than reporting
only an aggregate score. A gate applies only to that recorded run and scope.

Before claiming broader compatibility, repeat a representative subset, compare
baseline and treatment results, and add separate tool-enabled retrieval/citator
trials using permitted public sources. The synthetic set cannot substitute for
those checks. Do not put private matter material or paid source archives in this suite.

Commands return `0` for success, `1` for an incomplete/failed review summary, and
`2` for invalid data or collection errors. Preparation and validation make no model
calls. Actual results are pending unless an identified run says otherwise.
