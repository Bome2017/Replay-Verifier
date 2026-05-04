# Bounded Replay-Risk Audit: One-Page Brief

## One-Sentence Description

A bounded replay-risk audit checks whether a dangerous action sequence is reachable inside a scoped workflow model and returns either `SAFE_WITHIN_BOUND` or a reconstructable counterexample trace.

The concrete status values are `UNSAFE` and `SAFE_WITHIN_BOUND`.

## Why This Matters

Approval gates only protect against composed misuse if the workflow definition actually forces the agent through them. AI-agent and SaaS workflows can contain dangerous action compositions even when each individual action appears permitted &mdash; for example, an agent accesses customer data, drafts a reply, and sends it externally before approval, or a wire is sent before vendor verification, compliance review, or manager approval.

## What the Audit Does

1. Translate the workflow into a bounded Boolean transition model.
2. Define the forbidden condition.
3. Search for a reachable bad replay within the configured bound.
4. Return `UNSAFE` with a reconstructable trace if found.
5. Return `SAFE_WITHIN_BOUND` if no violation is found within the configured bound.

## Naming

- Service: Bounded Replay-Risk Audit.
- Tool / engine / demo repo: Replay Verifier.
- Output artifact: Bounded Replay Verification Report.

## Example Failure Shapes

- Workflow approval bypass.
- Confirmation bypass on destructive actions.
- Permission escalation before authorization.
- Sensitive data export before authorization.
- Composed action ordering across agent tool-use steps (e.g. wire sent before vendor verification, compliance review, manager approval).
- Approval-gated variant returns `SAFE_WITHIN_BOUND` under the supplied model and bound.

## Evidence Returned (Bounded Replay Verification Report)

- status
- bound
- violated condition, if unsafe
- first bad step
- reconstructable trace
- `state_before` / `state_delta` / `state_after`
- remediation note
- retest result when a safe variant is modeled

## Current Demo Status

The current demo includes a dependency-free brute-force reference verifier (the Replay Verifier engine) and an optional Z3 sanity cross-check that runs against the reference checker on supported examples in the local development environment. Z3 agreement is necessary and useful for implementation QA but is not independent real-world validation.

## Best-Fit Use Cases

- AI-agent tool-use workflows
- SaaS approval flows
- data disclosure review
- destructive-action review
- approval-bypass review
- pre-deployment workflow check

## Not a Fit For

- production-security validation
- legal/compliance certification
- full IAM/cloud graph analysis
- penetration testing replacement
- probabilistic LLM behavior modeling
- claims about all possible workflow behavior
- third-party independent benchmark validation

## Deliverable

- scoped workflow model
- assumptions and exclusions
- verifier result
- counterexample trace if unsafe
- remediation notes
- optional retest with guarded/safe variant

## Claim Boundary

Results are bounded to the supplied model and execution depth. `SAFE_WITHIN_BOUND` means no violation was found within that configured bound and model; it does not establish unrestricted system safety.

## Formal Research Context

Separate formal research motivates the replay-to-constraint framing and claim discipline behind this demo. The audit's public claims stand on the supplied model, bound, trace, remediation, and retest artifacts. Formal context does not certify this implementation as production-safe and does not prove agent safety. Optional background is in `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`.

## Suggested First Engagement

Bounded Replay-Risk Audit &mdash; Starter Package

- one workflow
- one forbidden condition
- small Boolean model
- bounded verifier run
- Bounded Replay Verification Report with witness trace if unsafe
- remediation/retest note
