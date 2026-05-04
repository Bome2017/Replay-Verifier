# Public Site Cleanup Report

Date: 2026-05-03

Scope: public-facing HTML / CSS / Markdown for the Bounded Replay-Risk Audit Demo (the `Replay-Verifier` GitHub Pages site) and an optional no-dependency local link checker. Verifier source semantics, workflow JSON, and generated `result.json` outputs were not touched.

## Files Changed

HTML pages (under `site/`):

- `index.html` — added meta description and canonical `<link>`. Replaced the buried support-agent example in the lead with the vendor-payment "show first" block. Promoted the product sentence ("Approval gates only protect against composed misuse if the workflow definition actually forces the agent through them.") into a muted-box highlight directly under the lead and again inside the Why-This-Matters section. Reframed Current Demo Status to use "self-constructed examples" and "Z3 sanity cross-check". Removed the "Related Public Demos" section (A/G demos no longer surface on the homepage). Added a footer line clarifying separation from A/G scoring systems.
- `service.html` — added meta description and canonical `<link>`. Added a "What you provide vs. what the audit models" translation-layer section. Added a "Request a starter audit" CTA pointing to the customer input template, the Bounded Replay Verification Report template, and the GitHub repo at <https://github.com/Bome2017/Replay-Verifier>; phrased as "Open a GitHub issue or share the completed template through your normal contact channel" (no email invented). Added "third-party independent benchmark validation" to the Not Included list. Promoted the product sentence at the top.
- `audit.html` — added meta description and canonical `<link>`. Added a brief "What you provide vs. what the audit models" intake note linking to the Service page and customer input template. Renamed the report artifact to "Bounded Replay Verification Report" and the matrix link to "Example validation matrix (customer-style dry runs)".
- `validation.html` — added meta description and canonical `<link>`. Renamed page to "Example Validation Matrix". Added an explicit "what this page is and is not" block. Reframed the in-page table as the Demo Exercise Matrix mixing canonical demo examples and customer-style dry-run shapes; added a note pointing to the downloadable customer-style matrix and to the canonical-examples evidence doc. Renamed the Z3 column from "Solver Cross-Check / Matched" to "Z3 Sanity Cross-Check / Agreed" and added a note explicitly downgrading agreement to implementation QA, not independent validation. Strengthened the limits-of-evidence box.
- `examples.html` — added meta description and canonical `<link>`. Promoted the vendor-payment example to the top with the existing "Why It's Easy to Miss" framing plus the explicit "the point is not that send_wire is individually mysterious; reviewers may assume earlier preparation implies verification" sentence. Softened the Z3 sentence to "implementation-QA agreement on a self-constructed example, not independent real-world validation".
- `boundaries.html` — added meta description and canonical `<link>`. Renamed Technical Context section to "Formal Research Context (Optional Background)" and reused the Formal Research Context paragraph. CRSL/RSVT names are no longer surfaced on this page — they remain only inside `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`. Added "It does not establish independent benchmark validation or third-party repeatability" to the out-of-scope list.
- `downloads.html` — added meta description and canonical `<link>`. Demoted the A/G demos block from a `grid` of cards to a small "Related Work" bullet list with a one-sentence framing that they are separate projects. Added the vendor-payment workflow + outputs into the Selected Artifacts table. Renamed the report-template link to "Bounded Replay Verification Report template".

Markdown docs (under `site/docs/`):

- `external_one_page_brief.md` — replaced "Formal Backing" with a shorter "Formal Research Context" section that does not name CRSL/RSVT or the Lean levels. Added a Naming section. Reframed Current Demo Status as Z3-sanity-cross-check, not "Both agree". Replaced "production-security certification" with "production-security validation"; added "third-party independent benchmark validation" and "claims about all possible workflow behavior" to Not-a-Fit-For. Renamed deliverable as "Bounded Replay Verification Report".
- `repeatability_validation_matrix.md` — renamed to "Customer-Style Dry-Run Matrix". Reframed the introduction to make clear it covers customer-style dry runs while canonical demo examples are documented in `validation_run_evidence.md`. Renamed columns ("Brute-force status" → "Reference status", "Z3 status" → "Z3 sanity status", "Status match" → "Status agreement"). Strengthened the interpretation paragraph to disclaim independent benchmark validation, third-party repeatability, and production-security validation. Did not invent rows; kept the four rows that already had backing in the matrix because the canonical six-row coverage is provided separately in `validation_run_evidence.md` (option 2 from the brief).
- `validation_run_evidence.md` — relabeled brute-force vs. Z3 as Reference Checker and Optional Z3 Sanity Cross-Check throughout. Tightened the wording to call out that two-encoder agreement is implementation QA on the same supplied model, not independent real-world validation. Strengthened the "What This Evidence Does Not Support" paragraph.
- `customer_input_template.md` — added a "Plain-language input is acceptable" block before State Variables, listing acceptable starting materials (agent prompt, tool/function schema, MCP/server tool list, approval rule, workflow diagram, runbook, policy description, product spec). Replaced "production-security certification" with "production-security validation" in Known Exclusions.
- `audit_report_template.md` — renamed top heading from "Bounded Replay-Risk Audit Report" to "Bounded Replay Verification Report" to match the artifact name in the new naming hierarchy.
- `TECHNICAL_APPENDIX_FORMAL_CONTEXT.md` — left as-is. Already explicitly bounded; CRSL/RSVT now only appear here.

Other:

- `site/README.md` — added the canonical public URL (with case-sensitivity warning), per-page canonical URLs, the naming hierarchy, and a Link Check section with the script invocation.
- `README.md` (project root, mirrored to repo) — added the canonical public URL and the naming hierarchy at the top. Did not change verifier semantics, examples, or output references.
- `site/scripts/check_site_links.py` — new no-dependency Python 3 link checker. Walks `*.html` under the site root, extracts `href`/`src`, ignores anchors after `#`, skips `http(s)`/`mailto`/`tel` (and reports them separately without failing), and exits non-zero if any local link does not resolve on disk.

Files explicitly NOT touched:

- `src/` (verifier semantics).
- `examples/*/workflow.json` and `outputs/*/result.json` (no broken paths required correction).
- `outputs/*/report.md` (generated output; current claim-boundary wording in those files is already inside the allowed phrase set).

## Link-Check Result

```text
$ python3 scripts/check_site_links.py
site root: /Users/bsm/ag_scoreboard/TrackB_Replay_Verifier_Demo/site
html files scanned: 7
local links checked: 113
external links seen: 11
external links (not fetched):
  audit.html -> https://bome2017.github.io/Replay-Verifier/audit.html
  boundaries.html -> https://bome2017.github.io/Replay-Verifier/boundaries.html
  downloads.html -> https://bome2017.github.io/Replay-Verifier/downloads.html
  downloads.html -> https://bome2017.github.io/ag-bank-scoreboard/
  downloads.html -> https://bome2017.github.io/ag-corporate-filings/
  downloads.html -> https://bome2017.github.io/ag-higher-education/
  examples.html -> https://bome2017.github.io/Replay-Verifier/examples.html
  index.html -> https://bome2017.github.io/Replay-Verifier/
  service.html -> https://bome2017.github.io/Replay-Verifier/service.html
  service.html -> https://github.com/Bome2017/Replay-Verifier
  validation.html -> https://bome2017.github.io/Replay-Verifier/validation.html
all local links resolved
```

All 113 local relative links across the seven HTML pages resolve to files on disk. Eleven external links were detected (seven canonical self-references, three A/G related-work links on `downloads.html`, and one GitHub repository link on `service.html`) and not fetched.

## Overclaim Scan Result

Searched all `*.html` and `*.md` under the site root for the phrases the brief listed as soft/hard overclaims:

```text
proves safety | guarantees | production-safe | certifies | certify
formal proof of agent safety | complete safety | all possible workflows
unrestricted | real-world security coverage | validated | repeatability
matched | match | legal/compliance | formal proof | production security
production-security | formal verification
```

Findings:

- All remaining occurrences of `unrestricted`, `production-safe`, `certify`, `repeatability`, `production-security`, `legal/compliance`, and similar terms appear inside negation/boundary clauses ("does NOT certify", "is NOT third-party repeatability", "does NOT establish unrestricted system safety", "is NOT independent benchmark validation"). These are claim boundaries and are intentionally preserved.
- The two remaining occurrences of `match`/`matched` reference the literal `status_match` field name in the `comparison.json` output (factual data field, not a validation claim).
- "validated" no longer appears anywhere in the public site or docs as an unqualified third-party-validation claim. The earlier phrase "in the local validated environment" was softened to "in the local development environment" on `validation.html` and in `external_one_page_brief.md`.
- CRSL/RSVT and the named Lean levels (2.8d-RX / 2.8e / 3.1 / 3.2-1) no longer appear on any HTML page or in `external_one_page_brief.md`. They remain only inside `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`, which is explicitly framed as optional research background.
- `boundaries.html` still links to the technical appendix as optional background.

## Known Remaining Limitations

- The downloadable customer-style dry-run matrix (`docs/repeatability_validation_matrix.md`) covers four rows (support reply, refund, permission escalation, sensitive data export). The in-page validation table on `validation.html` shows six rows (those four plus email exfiltration and delete confirmation). The canonical six-row evidence is documented in `docs/validation_run_evidence.md`, and the in-page note now explains the split. Per the brief's instructions, option 2 was used because the four customer-style dry-run workflow JSONs are not mirrored under `site/`; the canonical examples are.
- The audit_report_template.md heading was renamed to "Bounded Replay Verification Report" to match the new naming hierarchy. The legacy phrase "Bounded Replay-Risk Audit Report" still occurs in the body of generated `outputs/*/report.md` files, which were intentionally left unmodified per scope; they remain factually correct and inside the claim boundary.
- The Service page CTA links to the GitHub repository `https://github.com/Bome2017/Replay-Verifier` and to `docs/customer_input_template.md`. No email address was invented.

## Unresolved Items Requiring Decision

1. **Real contact channel.** The Service-page CTA currently says "Open a GitHub issue or share the completed template through your normal contact channel" and points at the `Bome2017/Replay-Verifier` repository. If you have a real preferred contact (email alias, web form, or a dedicated GitHub issue template), provide it and I will replace the wording.
2. **GitHub Issues availability.** The CTA assumes the public repo has Issues enabled at `https://github.com/Bome2017/Replay-Verifier`. If Issues are disabled or the repo path differs in case (e.g., `replay-verifier` lowercase), the link should be updated; please confirm.
3. **Customer-style dry-run mirroring.** If the support-reply, refund, permission-escalation, and data-export workflow artifacts should be mirrored into `site/dry_runs/` so the customer-style matrix can be expanded to six rows (option 1), confirm and I will copy them in a follow-up pass.
4. **Generated output renaming.** If the output `report.md` files should be regenerated with the new "Bounded Replay Verification Report" heading, that requires re-running the verifier (which is out of scope for this pass — verifier semantics intentionally untouched). Confirm whether to schedule that regeneration.
5. **Project root README.** The project-level `README.md` (one directory above `site/`) was lightly updated with the canonical URL and naming hierarchy at the top. If that file should remain unchanged outside the `site/` folder, revert that single edit and the work above still stands on its own.
