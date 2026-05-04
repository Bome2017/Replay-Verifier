# Technical Appendix: Formal Context

## Purpose

This appendix separates formal research context from the bounded audit demo itself. The demo should be evaluated as a bounded workflow replay-risk audit artifact: workflow model, bound, verifier result, trace, remediation, and retest.

## Relationship to Broader CRSL/RSVT Work

The demo is developed alongside broader CRSL/RSVT replay and constraint-encoding research. CRSL stands for *Certificate–Replay Substitution Law*; RSVT stands for *Recursive Structural Verification Theory*. The formal work provides research context, architecture, and claim discipline, but the public packet does not rely on readers accepting operational claims beyond the bounded workflow artifacts.

## Public-Safe Formal Context

The associated formal CRSL/RSVT replay-to-SAT proof package includes build-verified Lean reductions from scoped replay source classes to `TRACED_3_SAT`:

- Level 2.8d-RX: end-accepting bounded replay.
- Level 2.8e: accept-anywhere bounded replay.
- Level 3.1: strengthened relation-based finite replay.
- Level 3.2-1: `CNF3_SAT` and `TRACED_3_SAT` are build-verified equivalent as languages over `Cnf3`.

These results support the architecture and claim discipline behind the audit demo. They do not certify this Python implementation as production-safe, do not prove agent safety, and do not replace security review.

The public-safe technical wording is: Levels 2.8d-RX, 2.8e, and 3.1 provide build-verified Lean reductions from scoped replay source classes to `TRACED_3_SAT`. Level 3.2-1 proves `CNF3_SAT` and `TRACED_3_SAT` equivalent as languages over `Cnf3`. These results support architectural credibility, not operational guarantees for the demo.

## What the Demo Actually Claims

The demo claims only that, for supported Boolean workflow models, it can perform bounded replay-risk checks and return `UNSAFE` with a reconstructable trace or `SAFE_WITHIN_BOUND` under the supplied model and bound.

## Why Formal Context Still Matters

- It motivates the replay-to-constraint direction.
- It supports disciplined modeling.
- It encourages clear separation between model, bound, trace, and claim.
- It does not convert the demo into a broad theorem result.
- It does not establish NP-completeness, RCV completeness, P vs NP implications, production security, demo production safety, or agent safety.

## Appendix Boundary

This appendix is background context. The public demo value stands or falls on the bounded audit artifacts and validation results.
