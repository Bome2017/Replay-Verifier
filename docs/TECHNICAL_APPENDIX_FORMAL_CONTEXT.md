# Technical Appendix: Formal Context for Track B

## Purpose

This appendix separates formal research context from the public Track B demo. Track B should be evaluated as a bounded workflow replay-risk audit artifact: workflow model, bound, verifier result, trace, remediation, and retest.

## Relationship to Broader CRSL/RSVT Work

Track B is developed alongside broader CRSL/RSVT replay and constraint-encoding research. The formal work provides research context, architecture, and claim discipline, but the Track B public packet does not rely on readers accepting operational claims beyond the bounded workflow artifacts.

## Public-Safe Formal Context

Track A is the formal CRSL/RSVT replay-to-SAT proof package. The current formal tower includes build-verified Lean reductions from scoped replay source classes to `TRACED_3_SAT`:

- Level 2.8d-RX: end-accepting bounded replay.
- Level 2.8e: accept-anywhere bounded replay.
- Level 3.1: strengthened relation-based finite replay.
- Level 3.2-1: `CNF3_SAT` and `TRACED_3_SAT` are build-verified equivalent as languages over `Cnf3`.

These results support the architecture and claim discipline behind Track B. They do not certify this Python demo as production-safe, do not prove agent safety, and do not replace security review.

The public-safe technical wording is: Levels 2.8d-RX, 2.8e, and 3.1 provide build-verified Lean reductions from scoped replay source classes to `TRACED_3_SAT`. Level 3.2-1 proves `CNF3_SAT` and `TRACED_3_SAT` equivalent as languages over `Cnf3`. These results support architectural credibility, not operational guarantees for Track B.

## What Track B Actually Claims

Track B claims only that, for supported Boolean workflow models, it can perform bounded replay-risk checks and return `UNSAFE` with a reconstructable trace or `SAFE_WITHIN_BOUND` under the supplied model and bound.

## Why Formal Context Still Matters

- It motivates the replay-to-constraint direction.
- It supports disciplined modeling.
- It encourages clear separation between model, bound, trace, and claim.
- It does not convert the demo into a broad theorem result.
- It does not establish NP-completeness, RCV completeness, P vs NP implications, production security, Track B production safety, or agent safety.

## Appendix Boundary

This appendix is background context. The public demo value stands or falls on the bounded Track B artifacts and validation results.
