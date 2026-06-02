# LexWin Blog Template — Usage Guide

## File to copy for every new article
`BLOG_TEMPLATE.html` → copy to `/blog/{{ARTICLE_SLUG}}.html`

---

## Mandatory fills — EVERY article

| Placeholder | What to put |
|---|---|
| `{{ARTICLE_SLUG}}` | URL-safe filename, e.g. `legal-consultant-corporate` |
| `{{ARTICLE_TITLE}}` | Full title. Wrap accent word in `<em>` tag in the `<h1>`. Use plain text in `<title>` and meta tags. |
| `{{META_DESCRIPTION}}` | 140–160 chars. Action-oriented. Summarise the reader's benefit. |
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

---

## Sidebar placeholders

| Placeholder | What to put |
|---|---|
| `{{SECTION_1_HEADING_SHORT}}` | 3–5 word version of the section heading for TOC |
| `{{WHO_NEEDS_HEADING_SHORT}}` | e.g. `Who needs this` |
| `{{CHECKLIST_HEADING_SHORT}}` | e.g. `Self-diagnostic` |
| `{{CONCLUSION_HEADING_SHORT}}` | e.g. `Conclusion` |
| `{{CTA_CARD_HEADER}}` | e.g. `Get Expert Legal Advice` |
| `{{CTA_CARD_INTRO}}` | 1–2 sentences explaining the offer. |
| `{{CTA_BULLET_1–3}}` | What LexWin covers for this specific topic. |
| `{{RELATED_1–3_URL}}` | Full path, e.g. `/blog/posh-complete-guide.html` |
| `{{RELATED_1–3_TITLE}}` | Article title (short form). |

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

- [ ] All `{{PLACEHOLDER}}` values replaced — none remaining in file
- [ ] `<title>` includes article title + `| LexWin`
- [ ] Canonical URL matches actual file path
- [ ] `datePublished` in JSON-LD is correct
- [ ] All `h2` elements have unique `id=` attributes
- [ ] TOC `li` links match `h2` ids
- [ ] Stat strip has 4 relevant stats
- [ ] Minimum 2,500 words in article body
- [ ] Tags section populated (6–10 tags)
- [ ] Related articles links are valid and live
- [ ] No broken internal links
- [ ] GA4 block matches template exactly — not rewritten
