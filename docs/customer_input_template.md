# Customer Input Template for Bounded Replay-Risk Audit

## Workflow Name

Name:

## Workflow Description

- What system or workflow is being modeled?
- What is the dangerous outcome to check?

## System Boundary

- What is inside the model?
- What is outside the model?
- What assumptions are being made?

## State Variables

For v0.1/v0.2, variables are Boolean only.

| Variable | Meaning | Initial Value | Notes |
|---|---|---:|---|
|  |  | true/false |  |

## Actions

| Action | Preconditions | Effects | Notes |
|---|---|---|---|
|  |  |  |  |

## Forbidden Condition

Define the unsafe condition to check.

Example:

```text
has_customer_data == true
AND emailed_external == true
AND approval_received == false
```

## Bound

Maximum number of transitions to check:

Higher bounds increase search cost. `SAFE_WITHIN_BOUND` means no violation was found within this bound, not global safety.

## Known Exclusions

- probabilistic LLM behavior
- hidden tool behavior
- real network behavior
- real cloud/IAM behavior
- legal/compliance determination
- production-security certification

## Customer Confirmation

- [ ] I understand this is a bounded model.
- [ ] I understand `SAFE_WITHIN_BOUND` is not global safety.
- [ ] I understand results depend on the supplied workflow model.
- [ ] I understand omissions in the model may affect the result.
