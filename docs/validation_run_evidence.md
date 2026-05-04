# Validation Run Evidence

This document records the evidence that the bounded replay-risk audit demo behaves as the public site claims. Numbers are from a fresh local run on May 3, 2026.

## Test Suite

The full unittest suite was run against the bounded reference checker, the optional Z3 backend, the workflow validator, the trace/report writer, and the backend-comparison harness:

```text
Ran 37 tests in 0.022s
OK (skipped=8)   # 8 tests skipped only when Z3 is not installed; with Z3 installed: Ran 37 tests, OK
```

Wall-clock for the full test invocation including Python startup: ~0.12s.

## Per-Workflow Brute-Force Verifier

Each canonical workflow JSON was run through the dependency-free brute-force verifier. The status, expected outcome, first bad step, and runtime are reproducible by anyone who clones the repository and executes the same command.

| Workflow | State vars | Actions | Bound | Status | First bad step | Reachable states | Wall time |
|---|---:|---:|---:|---|---:|---:|---:|
| `agent_email_exfiltration` | 7 | 5 | 5 | `UNSAFE` | 3 | 8 | ~50 ms |
| `agent_email_requires_approval` | 7 | 5 | 5 | `SAFE_WITHIN_BOUND` | — | 6 | ~30 ms |
| `agent_delete_without_confirmation` | 5 | 4 | 4 | `UNSAFE` | 2 | 7 | ~30 ms |
| `agent_delete_requires_confirmation` | 5 | 4 | 4 | `SAFE_WITHIN_BOUND` | — | 5 | ~30 ms |
| `agent_vendor_payment_unauthorized` | 9 | 8 | 8 | `UNSAFE` | 5 | 23 | ~90 ms |
| `agent_vendor_payment_guarded` | 9 | 8 | 8 | `SAFE_WITHIN_BOUND` | — | 16 | ~180 ms |

"Reachable states" is the count of distinct Boolean state assignments the audit can reach within the configured bound under the supplied transition semantics. It is computed from the same model the verifier uses.

## Z3 Backend Cross-Check

The optional Z3 backend was run on the canonical examples and the new vendor-payment pair. The brute-force result and the Z3 result are recorded together in `outputs/<name>_compare/comparison.json`:

| Workflow | Brute-force | Z3 | `status_match` | Wall time |
|---|---|---|---|---:|
| `agent_email_exfiltration` | `UNSAFE` | `UNSAFE` | `True` | ~100 ms |
| `agent_delete_without_confirmation` | `UNSAFE` | `UNSAFE` | `True` | ~80 ms |
| `agent_vendor_payment_unauthorized` | `UNSAFE` | `UNSAFE` | `True` | ~250 ms |
| `agent_vendor_payment_guarded` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | `True` | ~440 ms |

Two independent encodings (a deterministic BFS reference and an SMT-based bounded model checker) produce the same status on every supported example. Disagreement would surface in `comparison.json`.

## Reproduction

From the project root, with Python 3 installed:

```bash
# brute-force (no extra deps)
python3 -m unittest discover -s tests
python3 -m src.solver_bruteforce examples/agent_vendor_payment_unauthorized/workflow.json

# optional Z3 cross-check
pip install z3-solver
python3 -m src.backend_compare examples/agent_vendor_payment_unauthorized/workflow.json
```

Each verifier run writes a `result.json` and `report.md` into `outputs/<workflow_name>/`; each cross-check writes a `comparison.json` into `outputs/<workflow_name>_compare/`. Selected outputs from these runs are linked from the [Examples page](../examples.html) and the [Downloads page](../downloads.html).

## What This Evidence Supports

The brute-force reference checker and the optional Z3 backend agree on every supported example workflow, including the deliberately larger `agent_vendor_payment_*` pair. Test suites pass in both the system-Python and Z3-enabled environments. The repeatability matrix on the [Validation page](../validation.html) extends the same audit pattern across additional workflow families (support reply, refund, permission escalation, sensitive data export, email exfiltration, delete confirmation) without changes to verifier source code.

## What This Evidence Does Not Support

`SAFE_WITHIN_BOUND` is tied to the supplied workflow model and the configured search bound. These results do not establish unrestricted system safety, do not certify the demo as production-safe, do not replace security review, and do not model probabilistic, temporal, or hidden tool behavior outside the supplied model.
