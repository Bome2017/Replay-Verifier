# Remediation Notes Template

## 1. Finding Summary

Workflow:

`<workflow_name>`

Verifier status:

`UNSAFE`

Configured bound:

`<bound>`

First bad step:

`<first_bad_step>`

Forbidden condition reached:

```text
<forbidden_condition>
```

Plain-language finding:

```text
<Describe the dangerous reachable path in one or two sentences.>
```

Example:

```text
A destructive action can occur before confirmation is received.
```

## 2. Counterexample Path

Action sequence:

```text
initial -> <action_1> -> <action_2> -> <bad_action>
```

Bad action:

`<bad_action_name>`

Why the bad state appears:

```text
<Explain which state variables become true/false at the first bad step and why that satisfies the forbidden condition.>
```

Trace source:

```text
outputs/<workflow_name>/result.json
```

The trace should be reconstructable from:

* `state_before`
* `state_delta`
* `state_after`

## 3. Root Cause Pattern

Primary root cause pattern:

* [ ] missing approval precondition
* [ ] missing confirmation precondition
* [ ] missing authorization precondition
* [ ] missing verification precondition
* [ ] missing escalation gate
* [ ] unsafe action ordering
* [ ] ambiguous model boundary
* [ ] other: `<describe>`

Root cause in model terms:

```text
<Action X> is reachable when <required_guard_variable> is still false because its preconditions do not require <required_guard_variable> == true.
```

Relevant unsafe action:

`<action_name>`

Current unsafe preconditions:

```text
<current_preconditions>
```

Required guard condition:

```text
<required_guard_variable> == true
```

## 4. Candidate Remediation

Recommended model change:

```text
Require <required_guard_variable> == true before <action_name>.
```

Patch target:

```text
examples/<workflow_name>/workflow.json
```

Unsafe action before remediation:

```json
{
  "name": "<action_name>",
  "pre": {
    "<existing_precondition>": true
  },
  "effects": {
    "<dangerous_effect>": true
  }
}
```

Guarded action after remediation:

```json
{
  "name": "<action_name>",
  "pre": {
    "<existing_precondition>": true,
    "<required_guard_variable>": true
  },
  "effects": {
    "<dangerous_effect>": true
  }
}
```

If multiple gates are required, include all required guard variables:

```json
"pre": {
  "<existing_precondition>": true,
  "<approval_received>": true,
  "<authorization_received>": true,
  "<verification_completed>": true
}
```

## 5. Optional Additional Remediation

Use this section only if the model suggests more than one plausible fix.

Potential additional controls:

* split unsafe and safe action variants
* add explicit content-safety state variables
* add explicit authorization state variables
* require human escalation before the risky action
* require approval before sensitive data enters the workflow
* separate "prepared" from "verified"
* separate "accessed" from "authorized"
* add a cancellation/stop state
* narrow the workflow boundary and retest

Notes:

```text
<Explain optional additional remediation if relevant.>
```

## 6. Guarded Variant Retest

Guarded workflow file:

```text
examples/<guarded_workflow_name>/workflow.json
```

Retest command:

```bash
python3 -m src.solver_bruteforce examples/<guarded_workflow_name>/workflow.json
```

Optional Z3 sanity cross-check:

```bash
python3 -m src.backend_compare examples/<guarded_workflow_name>/workflow.json
```

Expected guarded result:

`SAFE_WITHIN_BOUND`

Actual guarded result:

`<SAFE_WITHIN_BOUND | UNSAFE | NOT_RUN>`

Retest output:

```text
outputs/<guarded_workflow_name>/result.json
```

## 7. Retest Interpretation

If guarded result is `SAFE_WITHIN_BOUND`:

```text
No forbidden state was found within the supplied guarded model and configured bound.
This does not prove global safety. It means the specific forbidden condition was not reachable within this model and bound.
```

If guarded result remains `UNSAFE`:

```text
The proposed remediation did not block all reachable bad paths within the supplied model and bound. Review the new counterexample trace and update the model or guard condition.
```

## 8. Residual Risk

Residual risks that remain outside this bounded model:

* model omissions
* incorrect or incomplete workflow description
* insufficient bound
* probabilistic LLM behavior
* hidden tool behavior
* real network behavior
* real cloud/IAM behavior
* prompt injection
* tool output content
* human approval quality
* legal/compliance determination
* production-security validation

Additional residual risks for this workflow:

```text
<List workflow-specific residual risks.>
```

## 9. Assumptions and Exclusions

Assumptions:

* Boolean transition model
* one action per step
* configured finite bound
* preconditions determine action eligibility
* variables not affected by an action persist
* result is valid only relative to the supplied workflow model

Exclusions:

* no probabilistic agent-choice model
* no runtime monitoring
* no full IAM/cloud graph analysis
* no penetration testing
* no legal/compliance certification
* no global safety claim

## 10. Remediation Checklist

* [ ] Unsafe action identified.
* [ ] Missing guard condition identified.
* [ ] Candidate remediation written as explicit precondition change.
* [ ] Guarded workflow variant created.
* [ ] Guarded variant retested.
* [ ] Retest result recorded.
* [ ] Residual risks documented.
* [ ] Claim boundary preserved.

## 11. Claim Boundary

These remediation notes are part of a bounded replay-risk audit. They are valid only relative to the supplied workflow model, configured bound, stated assumptions, and stated exclusions.

`SAFE_WITHIN_BOUND` means no forbidden state was found within the supplied model and configured bound. It does not establish unrestricted system safety, production security, legal compliance, or global agent safety.
