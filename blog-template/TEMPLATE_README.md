# LexWin Blog Template — Usage Guide

## File to copy for every new article
`BLOG_TEMPLATE.html` → copy to `/blog/{{ARTICLE_SLUG}}.html`

## Already built in — do not rebuild these per article
Nav (with Services dropdown + About/Pune), footer, favicon links, GA4,
Tawk.to chat widget, WhatsApp button, and mobile-responsive table CSS
are all already wired into this template exactly as they appear on
every live page. Copy them as-is — do not hand-write them per article.
If the site-wide nav or footer ever changes, update this template
first so it stays the single source of truth, then update live
articles to match — not the other way round.

---

## Mandatory fills — EVERY article

| Placeholder | What to put |
|---|---|
| `{{ARTICLE_SLUG}}` | URL-safe filename, e.g. `legal-consultant-corporate` |
| `{{ARTICLE_TITLE}}` | The `<h1>` can be a longer, richer headline (wrap the accent word in `<em>`) — but the `<title>` tag itself must be a **short** version, 60–65 chars including ` | LexWin`, since Google truncates longer titles in search results. They don't have to be the same text; the `<h1>` sells the article, the `<title>` just needs to fit. |
| `{{META_DESCRIPTION}}` | 120–160 chars, ideally ~150. Action-oriented. Summarise the reader's benefit. Anything longer gets truncated mid-sentence in Google's search snippet. |
| `{{META_KEYWORDS}}` | 6–10 comma-separated keywords. Include "LexWin" as one. |
| `{{OG_TITLE}}` | Same as article title (plain text, no `<em>`). Max 60 chars. |
| `{{OG_DESCRIPTION}}` | Same as meta description or a short variant. |
| `{{TWITTER_TITLE}}` | Same as OG title. |
| `{{TWITTER_DESCRIPTION}}` | Max 200 chars. |
| `{{DATE_ISO}}` | ISO 8601, e.g. `2025-06-15` |
| `{{HERO_CATEGORY}}` | Short category label, e.g. `Corporate Legal Advisory` or `HR Compliance` |
| `{{READ_TIME}}` | Estimated reading time in minutes (word count ÷ 200) |
| `{{PUBLISH_MONTH_YEAR}}` | e.g. `June 2025` |
| `{{COPYRIGHT_YEAR}}` | Current year, e.g. `2025` |

---

## Stat strip — 4 stats per article

| Placeholder | What to put |
|---|---|
| `{{STAT_1_NUM}}` through `{{STAT_4_NUM}}` | Short number/value, e.g. `73%` or `₹50K+` or `12+` |
| `{{STAT_1_LABEL}}` through `{{STAT_4_LABEL}}` | Short descriptor, e.g. `disputes involve policy ambiguity` |

Stats must be relevant to the article topic. Use real data where possible.

---

## Article content placeholders

| Placeholder | What to put |
|---|---|
| `{{INTRO_PARAGRAPH_1}}` | The hook — the problem or the stakes. No heading. |
| `{{INTRO_PARAGRAPH_2}}` | Bridge — why this matters now, what the article covers. |
| `{{CALLOUT_LABEL}}` | Bold label for opening callout, e.g. `The key insight` |
| `{{CALLOUT_TEXT}}` | The insight statement. 1–2 sentences. |
| `{{SECTION_1_ID}}` | Lowercase, hyphenated anchor id, e.g. `what-is` |
| `{{SECTION_1_HEADING}}` | Full heading text with numbering, e.g. `1. What is a legal consultant?` |
| `{{SECTION_1_CONTENT}}` | Opening paragraph(s) for that section. |

Add as many `h2` sections as the topic requires. Every `h2` **must** have a matching `id=` attribute.

---

## Article flow — follow this order every time

1. Hook paragraph (problem / stakes)
2. Bridge paragraph (why now, what this covers)
3. Opening callout (key insight)
4. Substance sections (`h2` → `h3` as needed)
5. Scenario / real-world example boxes (`.scenario`)
6. Urgency section (India's evolving landscape, deadlines, costs)
7. LexWin process section (how we approach this)
8. Who-needs-this table (`.compare-table`)
9. Self-diagnostic checklist (`.checklist`)
10. Conclusion + LexWin callout
11. Tags

Minimum 2,500 words. Target 3,500+.

---

## Visual toolkit — when to use each component

| Component | Class | Use when |
|---|---|---|
| Insight callout | `.callout` | Highlighting a key principle or LexWin perspective |
| Warning callout | `.callout-warn` | A common mistake or legal danger |
| Tip callout | `.callout-tip` | A positive recommendation or best practice |
| Scenario box | `.scenario` | Real-world example (anonymised) |
| Process steps | `.process-steps` | Step-by-step how-to (LexWin process, procedures) |
| Comparison table | `.compare-table` | Comparing two approaches, litigation vs non-lit, etc. |
| Card grid | `.card-grid` + `.policy-card` | Listing services, agreement types, policy areas |
| Highlight cards | `.highlight-card` | Policies/topics with risk badge (high/med/low) |
| Checklist | `.checklist` | Self-diagnostic or recommended action list |
| Icon process flow | `.icon-flow` + `.flow-step` | A genuine ordered sequence — a legal procedure, a deal lifecycle. 3–5 steps. |
| Icon category grid | `.icon-grid` + `.icon-card` | A set of distinct types/categories, placed **above** the detailed table or prose it indexes. 6 cards (3×2) is ideal. |

---

## Diagrams — every article should carry at least one where the content fits

The two diagram components (`.icon-flow`, `.icon-grid`) are what keep
articles from being walls of text. The rule:

- **If the article explains a process or sequence** → add an `.icon-flow`
  summarising it visually, placed right after the intro paragraph of the
  section whose process it depicts. The detailed prose stays below it —
  the diagram is an overview, not a replacement.
- **If the article covers a set of categories/types** → add an
  `.icon-grid` as a scannable index above the detailed comparison table
  or prose.
- **If neither structure genuinely exists in the content** → skip the
  diagram. A forced diagram is worse than none.

Icon rules (both components):

- Hand-drawn **inline SVG**, `viewBox="0 0 24 24"`, stroke-based paths
  only — no `fill` attribute, no `stroke` attribute on the SVG itself
  (the component CSS sets stroke color and width).
- Draw each icon for its **specific concept** — a warehouse roofline for
  industrial property, a magnifier for a title search — not generic
  clip-art. The template's example flow-step contains a reference icon.
- **Never** use external images, stock photos, or icon-font/CDN icons —
  licensing cannot be verified, and external requests are a dependency.
  Everything must be drawn in the file.
- Both components handle mobile automatically (flow → vertical connected
  list below 700px; grid → 2 columns below 640px). Nothing extra needed.

Reference implementation live on the site:
`blog/property-buying-guide-pune-maharashtra.html` (due-diligence flow +
six-property-types grid).

---

## Table of contents + remaining body placeholders

The layout is single-column (no sidebar) — the "In this article" box at
the top of `.article-body` is the TOC. Add one `<li>` per `h2` section,
matching each section's `id=`.

| Placeholder | What to put |
|---|---|
| `{{SECTION_1_HEADING_SHORT}}` | 3–5 word version of the section heading for TOC |
| `{{WHO_NEEDS_HEADING_SHORT}}` | e.g. `Who needs this` |
| `{{CHECKLIST_HEADING_SHORT}}` | e.g. `Self-diagnostic` |
| `{{CONCLUSION_HEADING_SHORT}}` | e.g. `Conclusion` |
| `{{WHO_NEEDS_HEADING}}` | Full heading, e.g. `Who Needs This — and When` |
| `{{WHO_ROW_1_PROFILE}}` / `{{WHO_ROW_1_RISKS}}` / `{{WHO_ROW_1_ACTIONS}}` | One row of the who-needs-this table. Copy the `<tr>` for additional rows/profiles. |
| `{{CHECKLIST_HEADING}}` | Full heading, e.g. `Pre-Engagement Checklist` |
| `{{CHECKLIST_ITEM_1}}`, `{{CHECKLIST_ITEM_2}}` | One self-diagnostic question per `<li>`. Add more `<li>` as needed. |
| `{{CONCLUSION_HEADING}}` | Full heading, e.g. `Conclusion` |
| `{{CONCLUSION_TEXT}}` | Closing paragraph(s) before the LexWin CTA callout. |
| `{{LEXWIN_CTA_CALLOUT}}` | 1–2 sentences on how LexWin helps with this specific topic. |
| `{{TAG_1}}`, `{{TAG_2}}`, `{{TAG_3}}` | Article tags (6–10 recommended — copy the `<span class="tag">` for more). |

**Note:** every `<table>` must be wrapped in `<div class="table-wrapper">...</div>` (already done around the who-needs-this table in the template) — this is what makes wide tables scroll on mobile instead of breaking the layout. Keep this wrapper on any additional tables you add.

---

## GA4 rules — never change this block

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-995KV4HXM1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag('js', new Date());
  if (!document.cookie.split(';').some(function(c){ return c.trim().startsWith('lexwin_notrack='); })) {
    gtag('config', 'G-995KV4HXM1');
  }
</script>
```

- Async loader → **always unconditional**
- `window.dataLayer`, `function gtag()`, `gtag('js', new Date())` → **always outside any if-block**
- `gtag('config', ...)` → **only inside the `lexwin_notrack` cookie check**
- Never rewrite this block from memory — copy from template exactly.

---

## Fixed values — never change

| Item | Value |
|---|---|
| GA4 Measurement ID | `G-995KV4HXM1` |
| Google site verification | `61C6F194U8QSocNUBvV7N2gDyIar_2zgtFRcAHBigbw` |
| Calendly URL | `https://calendly.com/sadanand-sonar/30min` |
| WhatsApp number | `https://wa.me/919823385085` |
| OG image | `https://www.lexwin.co.in/assets/lexwin-og.png` |
| Canonical base | `https://www.lexwin.co.in/blog/` |

---

## Checklist before publishing

- [ ] Run `python3 scripts/check_seo_meta.py` from the repo root — must report "All N pages OK" with no new failures
- [ ] All `{{PLACEHOLDER}}` values replaced — none remaining in file
- [ ] `<title>` is 60–65 characters max, including ` | LexWin`, and unique across the site — Google truncates longer titles in search results
- [ ] `META_DESCRIPTION` is 120–160 characters — Google truncates the search snippet past ~155-160 chars, so anything longer just gets cut off mid-sentence
- [ ] JSON-LD `"headline"` matches the `<title>` text with the ` | LexWin` suffix removed
- [ ] JSON-LD `"description"` matches `META_DESCRIPTION` exactly (same string, both places — single source of truth)
- [ ] Canonical URL matches actual file path
- [ ] `datePublished` in JSON-LD is correct
- [ ] All `h2` elements have unique `id=` attributes
- [ ] TOC `li` links match `h2` ids
- [ ] Stat strip has 4 relevant stats
- [ ] At least one diagram (`.icon-flow` or `.icon-grid`) where the content has a genuine process or category structure — with hand-drawn inline SVG icons, never external images. (Skip only if the content truly has neither; delete the unused example blocks either way.)
- [ ] Minimum 2,500 words in article body
- [ ] Every `<table>` is wrapped in `<div class="table-wrapper">...</div>`
- [ ] Tags section populated (6–10 tags)
- [ ] Related articles links are valid and live
- [ ] No broken internal links
- [ ] GA4 block matches template exactly — not rewritten
