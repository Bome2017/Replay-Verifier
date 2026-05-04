# Repeatability Validation Matrix

This matrix summarizes customer-style bounded replay-risk dry runs across multiple workflow families. Each workflow uses the existing v0.1 Boolean replay model and the optional v0.2 Z3 backend when available.

| Workflow family | Unsafe workflow name | Forbidden condition | Bound | Brute-force status | Z3 status | Status match | First bad step | Trace action sequence | Safe variant status | Safe variant Z3 status | Safe variant status match | Source-code changes needed? | Report created? | Remediation created? |
|---|---|---|---:|---|---|---|---:|---|---|---|---|---|---|---|
| Support agent external reply | `support_agent_external_reply_risk` | `customer_account_data_accessed == true AND external_reply_sent == true AND manager_approval_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_ticket", "access_customer_account_data", "draft_reply", "send_reply_external"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Refund issued without approval | `refund_without_manager_approval` | `refund_issued == true AND manager_approval_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_refund_request", "access_customer_billing_record", "draft_refund", "issue_refund"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Permission escalation | `permission_escalation_without_authorization` | `elevated_access_granted == true AND admin_authorization_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_access_request", "inspect_user_account", "prepare_permission_change", "grant_elevated_access"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Sensitive data export | `sensitive_data_export_without_authorization` | `sensitive_data_exported == true AND export_authorization_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 3 | `[null, "select_sensitive_records", "prepare_export", "export_data"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |

## Interpretation

The repeatability dry runs show that multiple scoped workflow families can be modeled, checked, remediated, and retested without changing verifier source code. This supports the bounded service workflow, not any unrestricted safety claim.
