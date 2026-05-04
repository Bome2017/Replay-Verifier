# Bounded Replay-Risk Audit: One-Page Brief

## One-Sentence Description

A bounded replay-risk audit checks whether a dangerous action sequence is reachable inside a scoped workflow model and returns either `SAFE_WITHIN_BOUND` or a reconstructable counterexample trace.

The concrete status values are `UNSAFE` and `SAFE_WITHIN_BOUND`.

## Problem

AI-agent and SaaS workflows can contain dangerous action compositions even when each individual action appears permitted. Example: an agent accesses customer data, drafts a reply, and sends it externally before approval.

## What the Audit Does

1. Translate the workflow into a bounded Boolean transition model.
2. Define the forbidden condition.
3. Search for a reachable bad replay within the configured bound.
4. Return `UNSAFE` with a reconstructable trace if found.
5. Return `SAFE_WITHIN_BOUND` if no violation is found within the configured bound.

## Example Failure Shapes

- Customer/account data externally disclosed before approval.
- File deleted before confirmation.
- Approval-gated variant returns `SAFE_WITHIN_BOUND` under the supplied model.

## Evidence Returned

- status
- bound
- violated condition, if unsafe
- first bad step
- reconstructable trace
- `state_before` / `state_delta` / `state_after`
- remediation note
- retest result when a safe variant is modeled

## Current Demo Status

The current demo includes a dependency-free brute-force reference verifier and an optional locally validated Z3 backend. Both agree on the supported example workflows.

## Best-Fit Use Cases

- AI-agent tool workflows
- SaaS approval flows
- data disclosure review
- destructive-action review
- approval-bypass review
- early-stage product/security review

## Not a Fit For

- production-security certification
- legal/compliance certification
- full IAM/cloud graph analysis
- penetration testing replacement
- probabilistic LLM behavior modeling
- claims about all possible workflow behavior

## Deliverable

- scoped workflow model
- assumptions and exclusions
- verifier result
- counterexample trace if unsafe
- remediation notes
- optional retest with guarded/safe variant

## Claim Boundary

Results are bounded to the supplied model and execution depth. `SAFE_WITHIN_BOUND` means no violation was found within that configured bound and model; it does not establish unrestricted system safety.

## Formal Backing

Track A supplies formal replay-to-SAT infrastructure and claim discipline. It does not certify the Track B implementation as production-safe.

Levels 2.8d-RX, 2.8e, and 3.1 provide build-verified Lean reductions from scoped replay source classes to `TRACED_3_SAT`. Level 3.2-1 proves `CNF3_SAT` and `TRACED_3_SAT` equivalent as languages over `Cnf3`. These results support architectural credibility, not operational guarantees for Track B.

## Suggested First Engagement

Bounded Replay-Risk Audit - Starter Package

- one workflow
- one forbidden condition
- small Boolean model
- bounded verifier run
- report with witness trace if unsafe
- remediation/retest note
