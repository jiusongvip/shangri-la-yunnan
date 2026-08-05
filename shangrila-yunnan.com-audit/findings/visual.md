## Visual & On-Page SEO Findings — shangri-la-yunnan.com

### What Works Well

- All 19 homepage images have descriptive `alt` text — 100% coverage
- 18 of 19 images use `loading="lazy"` (the hero image correctly omits it)
- Tailwind-based responsive design with mobile-first viewport
- Clean, readable typography with clear visual hierarchy
- Dark hero section with legible white text on a gradient overlay
- Quick Facts card is a smart UX pattern — scannable data at a glance

### High

**H1: All 14 detail-page canonicals point to localhost**
This is the same critical issue from the Technical SEO audit. The `Astro.url.href` in [DetailLayout.astro](D:\workspaces\website\shangri-la-yunnan\shangri-la-yunnan-site\src\layouts\DetailLayout.astro:36) resolves to `http://localhost:4321/…` during build. Same fix applies.

**H2: OG image is an SVG**
`<meta property="og:image" content="https://shangri-la-yunnan.com/og-image.svg">` — Facebook, Twitter, LinkedIn, and WhatsApp do not reliably render SVG OG images. They expect PNG or JPEG. This means social shares will show either a blank preview or fallback to the first body image, which is a missed branding opportunity on every share.

### Medium

**M1: Title tags are formulaic across detail pages**
Every detail page uses `"Page Title | Shangri-La Yunnan Travel Guide"`. While consistent, the brand suffix adds characters without differentiation. Consider front-loading the unique part: for example, `"Pudacuo National Park Guide (2026) — Tickets, Trails, Tips"`.

**M2: Meta descriptions could target intent more sharply**
Descriptions describe what the page contains ("Complete guide to…") rather than the user's search intent ("Plan your visit to Pudacuo National Park: tickets from ¥100, best hiking trails, and how to get there from Shangri-La in 40 minutes"). Action-oriented descriptions tend to drive higher CTR.

**M3: 38 H4 tags on homepage — heading hierarchy is shallow**
The homepage jumps from H2 → H3 → many H4s. Many of those H4s (card titles, labels) would be more semantically appropriate as `<strong>` or `<dt>` elements. A flatter, more intentional heading structure helps both accessibility and SEO.

### Low

**L1: No `aria-label` on navigation links**
The main nav uses text labels so this is minor, but the mobile menu button and logo link would benefit from `aria-label` for screen readers.

### Score

| Sub-category | Score | Notes |
|---|---|---|
| Title Tags | 82/100 | Formulaic but keyword-rich |
| Meta Descriptions | 80/100 | Descriptive but could target intent better |
| Heading Structure | 70/100 | H4 overuse, H1 has HTML tags |
| Internal Linking | 55/100 | Detail pages orphaned from each other |
| Alt Text Coverage | 100/100 | Perfect |
| Social Meta | 60/100 | SVG OG image will break on most platforms |
| **On-Page Score** | **75/100** | |
