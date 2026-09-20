#!/usr/bin/env python3
"""
Checks meta description length (and a few other cheap SEO/consistency
invariants) across every .html file in the site.

Run before publishing any new or edited page:
    python3 scripts/check_seo_meta.py

Exits non-zero if any page fails a check, so it can be wired into a
pre-commit hook or CI step later if this repo ever gets one.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DESC_MIN, DESC_MAX = 120, 160  # Google truncates the SERP snippet around ~155-160 chars

SKIP_DIRS = {'.git', 'blog-template', 'node_modules'}


def find_html_files():
    for path in REPO_ROOT.rglob('*.html'):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def check_file(path):
    problems = []
    content = path.read_text(encoding='utf-8', errors='ignore')

    desc_m = re.search(r'name="description"\s+content="([^"]*)"', content)
    if not desc_m:
        problems.append("missing <meta name=\"description\">")
    else:
        length = len(desc_m.group(1))
        if length > DESC_MAX:
            problems.append(f"meta description too long: {length} chars (max {DESC_MAX})")
        elif length < DESC_MIN:
            problems.append(f"meta description quite short: {length} chars (min recommended {DESC_MIN})")

    title_m = re.search(r'<title>(.*?)</title>', content, re.S)
    if not title_m:
        problems.append("missing <title>")
    elif len(title_m.group(1)) > 65:
        problems.append(f"<title> long: {len(title_m.group(1))} chars (Google truncates ~60-65)")

    # meta description and JSON-LD "description" should stay in sync (single source of truth)
    jsonld_m = re.search(r'"description":\s*"([^"]*)"', content)
    if desc_m and jsonld_m and desc_m.group(1) != jsonld_m.group(1):
        problems.append("JSON-LD \"description\" doesn't match meta description (should be the same text)")

    return problems


def main():
    total = 0
    failed = 0
    for path in sorted(find_html_files()):
        total += 1
        problems = check_file(path)
        if problems:
            failed += 1
            rel = path.relative_to(REPO_ROOT)
            print(f"\n{rel}")
            for p in problems:
                print(f"  - {p}")

    print(f"\n{'-'*60}")
    if failed:
        print(f"{failed} of {total} pages have issues.")
        sys.exit(1)
    else:
        print(f"All {total} pages OK.")
        sys.exit(0)


if __name__ == '__main__':
    main()
