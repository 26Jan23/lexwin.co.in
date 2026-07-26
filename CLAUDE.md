# LexWin Legal & HR Consulting — Site Notes

Static HTML site (no build step, no bundler) served directly from this
repo's `main` branch. Every page is a standalone `.html` file with its
own inline `<style>` (except blog articles — see below). Pushing to
`main` is what deploys the live site at www.lexwin.co.in.

## Before publishing any new or edited page

Run this and make sure it passes:

```
python3 scripts/check_seo_meta.py
```

It checks, across every `.html` file in the repo:
- `<title>` is ≤65 characters (Google truncates longer titles in search results)
- meta description is 120–160 characters (Google truncates the search
  snippet past ~155–160 chars — anything longer just gets cut off
  mid-sentence, which is worse than a shorter, complete description)
- JSON-LD `"description"` matches the meta description exactly, and
  (where present) `"headline"` matches the `<title>` minus the
  ` | LexWin` suffix — these are meant to be single sources of truth,
  not independently drifting copies

The `<h1>` on the page can (and usually should) be a longer, richer
headline than the `<title>` tag — they don't have to match. Only the
`<title>` tag itself is length-constrained.

## Publishing a new blog article

1. Copy `blog-template/BLOG_TEMPLATE.html` → `blog/{slug}.html`. Follow
   `blog-template/TEMPLATE_README.md` for every placeholder and the
   full pre-publish checklist (includes the length checks above, plus
   TOC/h2-id consistency, table-wrapper usage, etc).
2. Do **not** hand-write the nav, footer, WhatsApp button, or design
   tokens — the template already links to `assets/css/blog-chrome.css`,
   the single shared stylesheet for all blog articles. If the site-wide
   nav/footer ever needs to change, edit that file and the template
   first, then nothing else needs updating per-article.
3. Add the new article's card to `blog/index.html`, the homepage
   slideshow in `index.html`, and an entry in `sitemap.xml` — this is
   currently manual, not automated. Bump the `#blogCountNum` count where
   it's still hardcoded.

## Site-wide conventions (apply to every page, not just blog articles)

- **Nav**: Services dropdown (HR Consulting / Corporate Legal / Setting
  Up Business in India / Real Estate Due Diligence) + Who We Help +
  Engagement + Insights + Free Tools + About + Pune + Free Consultation
  CTA. Every page should have all of these — a few pages have drifted
  from this in the past (missing About/Pune, or a stale nav entirely)
  and had to be retrofitted.
- **Footer nav landmark**: the footer's `<nav aria-label="Footer
  navigation">` must stay excluded from any bare `nav` CSS selector —
  use `nav:not([aria-label="Footer navigation"])` for the main nav's
  styling, or the footer nav silently inherits the dark sticky main-nav
  look. This bit everyone once already; don't reintroduce a bare `nav {`
  selector.
- **Tables**: always wrap in `<div class="table-wrapper">...</div>` —
  this is what makes wide tables scroll on mobile instead of breaking
  the layout.
- **`rel="noopener"`**: every `target="_blank"` link needs it.
- **`robots.txt`** disallows `/blog-template/` — that folder is an
  internal authoring aid, not public content. Don't remove the
  disallow rule, and don't add new internal-only folders without a
  similar exclusion.

## Git workflow

- Small, well-understood fixes: commit and push straight to `main`
  (that's the deploy trigger — there's no separate staging environment).
- Larger or riskier changes (anything touching many files at once, or
  where a mistake would be hard to spot from a code diff alone — CSS
  refactors are the classic case): work on a separate branch first,
  verify thoroughly (including an actual rendered/screenshot check, not
  just structural checks — subtle visual regressions do not show up in
  a text diff), then merge to `main` once confirmed.
- Never delete a branch without checking whether it's merged into
  `main` first (`git branch -r --no-merged origin/main`). An unmerged
  branch may be the only place certain history still exists — this
  repo has at least one long-lived branch,
  `backup-pre-free-tools-2026-07-15`, that exists specifically to
  preserve early project history no longer reachable from `main`. Keep
  it unless explicitly told to remove it.
