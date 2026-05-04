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

## Input Form

Plain-language input is acceptable. The formal table below can be completed during the modeling step. Acceptable starting materials include:

- agent prompt or system message
- tool / function schema
- MCP or server tool list
- approval, confirmation, or escalation rule
- workflow diagram or runbook
- policy description or product spec

The audit step translates that material into the formal workflow model below (state variables, actions, preconditions, effects, forbidden condition, bound, assumptions, exclusions). You do not need to arrive with a Boolean model already filled in.

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
- production-security validation

## Customer Confirmation

- [ ] I understand this is a bounded model.
- [ ] I understand `SAFE_WITHIN_BOUND` is not global safety.
- [ ] I understand results depend on the supplied workflow model.
- [ ] I understand omissions in the model may affect the result.
