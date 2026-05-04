#!/usr/bin/env python3
"""No-dependency local link checker for the static site.

Walks every `.html` file under the site root, extracts `href` and `src`
attributes, and verifies that local relative targets resolve to files on
disk. External `http`/`https` links are reported separately and do not
cause a non-zero exit. Anchors after `#` are ignored. Anchors of the
form `#name` (no path) are ignored entirely.

Usage:

    python3 scripts/check_site_links.py [SITE_ROOT]

Default SITE_ROOT is the parent directory of this script, i.e. the `site/`
folder when this script lives at `site/scripts/check_site_links.py`.

Exit code is 0 when every local link resolves, 1 otherwise.
"""

from __future__ import annotations

import html
import os
import re
import sys
from pathlib import Path
from typing import Iterable

ATTR_RE = re.compile(
    r'\b(?:href|src)\s*=\s*(?P<q>["\'])(?P<val>.*?)(?P=q)',
    re.IGNORECASE | re.DOTALL,
)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:"))


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def iter_html_files(root: Path) -> Iterable[Path]:
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".html"):
                yield Path(dirpath) / name


def extract_links(html_text: str) -> list[str]:
    return [html.unescape(m.group("val")) for m in ATTR_RE.finditer(html_text)]


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        root = Path(argv[1]).resolve()
    else:
        root = Path(__file__).resolve().parent.parent

    if not root.is_dir():
        print(f"site root not found: {root}", file=sys.stderr)
        return 2

    missing: list[tuple[Path, str, Path]] = []
    external: list[tuple[Path, str]] = []
    checked_local = 0

    for html_path in sorted(iter_html_files(root)):
        try:
            text = html_path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"could not read {html_path}: {exc}", file=sys.stderr)
            continue

        for raw in extract_links(text):
            target = raw.strip()
            if not target:
                continue
            if target.startswith("#"):
                continue
            if is_external(target):
                external.append((html_path, target))
                continue

            local = strip_anchor(target)
            if not local:
                continue

            if local.startswith("/"):
                resolved = (root / local.lstrip("/")).resolve()
            else:
                resolved = (html_path.parent / local).resolve()

            checked_local += 1
            if not resolved.exists():
                missing.append((html_path, target, resolved))

    print(f"site root: {root}")
    print(f"html files scanned: {sum(1 for _ in iter_html_files(root))}")
    print(f"local links checked: {checked_local}")
    print(f"external links seen: {len(external)}")

    if external:
        print("external links (not fetched):")
        for src, link in sorted(set((str(s.relative_to(root)), l) for s, l in external)):
            print(f"  {src} -> {link}")

    if missing:
        print("missing local links:")
        for src, link, resolved in missing:
            try:
                rel_src = src.relative_to(root)
            except ValueError:
                rel_src = src
            print(f"  {rel_src}: {link} -> {resolved}")
        return 1

    print("all local links resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
