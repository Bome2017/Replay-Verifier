# Bounded Replay-Risk Audit Demo — Static Site

This folder is the static presentation layer for the public brand `Bounded Replay-Risk Audit Demo`. Its contents are mirrored to the GitHub Pages repo.

## Naming

- Service / product: **Bounded Replay-Risk Audit**.
- Tool / engine / demo repo: **Replay Verifier**.
- Output artifact: **Bounded Replay Verification Report**.

## Canonical public URL

Canonical public URL: <https://bome2017.github.io/Replay-Verifier/>

The URL path is case-sensitive. Use `Replay-Verifier` exactly (capital `R` and `V`, hyphen between).

Per-page canonical URLs:

- <https://bome2017.github.io/Replay-Verifier/>
- <https://bome2017.github.io/Replay-Verifier/validation.html>
- <https://bome2017.github.io/Replay-Verifier/examples.html>
- <https://bome2017.github.io/Replay-Verifier/audit.html>
- <https://bome2017.github.io/Replay-Verifier/service.html>
- <https://bome2017.github.io/Replay-Verifier/boundaries.html>
- <https://bome2017.github.io/Replay-Verifier/downloads.html>

## Open Locally

Open `index.html` directly in a browser, then use the local navigation links:

- `index.html`
- `validation.html`
- `examples.html`
- `audit.html`
- `service.html`
- `boundaries.html`
- `downloads.html`

No local server is required. The pages use plain HTML and CSS with relative links only. Linked markdown, workflow JSON, output, and dry-run files live alongside the HTML under `docs/`, `examples/`, `outputs/`, and `dry_runs/`.

## Link Check

A no-dependency link checker is available at `scripts/check_site_links.py` (relative to the repo root that contains this `site/` folder, depending on staging layout):

```bash
python3 scripts/check_site_links.py
```

It verifies that local relative `href`/`src` targets resolve to files on disk and reports external `http(s)` links separately without failing.

## Publishing

The contents of this folder are intended to be copied to the public GitHub Pages repo as static content. No build step or external dependency is required.

## Claim Boundary

Public claims remain bounded to supplied workflow models and configured search depth. The site presents this work as a scoped replay-risk audit demo, not as unrestricted system safety coverage, third-party independent benchmark validation, or a replacement for security review.
