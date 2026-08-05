# SEO Audit Report: shangri-la-yunnan.com

**Date**: 2026-08-05
**Business Type**: Travel / Tourism — Destination Guide & Content Hub
**Overall SEO Health Score**: **72 / 100**
**Pages Audited**: 15 (1 homepage + 8 attractions + 6 food)

---

## Executive Summary

Shangri-La Yunnan Travel Guide is a well-structured Astro-built static site with genuinely useful content. The content quality and schema coverage are strong, and the single-page architecture serves travelers well. However, the site has three critical issues that must be fixed before production deployment, and several high-impact improvements that will meaningfully boost search visibility.

### Top 5 Critical Issues

1. **All 14 detail-page canonicals point to `http://localhost:4321`** — a build artifact that will cause Google to index wrong URLs
2. **No `robots.txt`** — crawlers have zero guidance on what to crawl or avoid
3. **No XML sitemap** — 15 pages lack a discovery mechanism for search engines
4. **OG image is SVG** — social sharing previews will break on Facebook, Twitter, and LinkedIn
5. **Detail pages are orphaned** — each links only to `/`, creating poor PageRank flow and dead-end UX

### Top 5 Quick Wins

1. Fix canonical URLs — replace `Astro.url.href` with the production URL in two layout files
2. Generate a `robots.txt` and `sitemap.xml` (trivial for a 15-page static site)
3. Replace `og-image.svg` with a 1200x630 PNG
4. Add `BreadcrumbList` schema to detail pages (breadcrumb UI already exists)
5. Create `/llms.txt` and `/llms-full.txt` for AI crawler discovery

---

## Category Scores

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 66 | 22% | 14.5 |
| Content Quality | 79 | 23% | 18.2 |
| On-Page SEO | 75 | 20% | 15.0 |
| Schema / Structured Data | 83 | 10% | 8.3 |
| Performance | 73 | 10% | 7.3 |
| AI Search Readiness | 56 | 10% | 5.6 |
| Images | 78 | 5% | 3.9 |
| **Overall** | **72** | **100%** | **72.8** |

---

## 1. Technical SEO — Score: 66/100

### Critical

**C1: Detail-page canonicals resolve to localhost**
All 14 detail pages (8 `/attractions/*`, 6 `/food/*`) emit `<link rel="canonical" href="http://localhost:4321/...">`. Root cause: `DetailLayout.astro` uses `Astro.url.href`, which resolves to the dev server URL during `astro build`. This must be fixed before any production deployment — Google will index these pages with wrong canonical signals, creating duplicate-content chaos.

**Fix**: Replace `Astro.url.href` with `` `https://shangri-la-yunnan.com${Astro.url.pathname}` ``. Apply the same fix to `BaseLayout.astro`.

**C2: No robots.txt**
The `dist/` directory contains no `robots.txt`. This is a mandatory file. Without it, crawlers have no guidance on crawl priority or which paths to avoid.

**C3: No XML sitemap**
No `sitemap.xml` exists. For 15 pages, this is a straightforward fix: install `@astrojs/sitemap` or generate a static XML sitemap manually.

### High

**H1: No 404 error page** — broken links trigger the hosting default, degrading UX and quality signals.
**H2: No cache or security headers** — CDN-level `Cache-Control`, `X-Content-Type-Options`, and HSTS headers need configuration.
**H3: Trailing-slash inconsistency risk** — Astro config does not set `trailingSlash`, so URLs resolve both with and without trailing slash without redirect rules.

---

## 2. Content Quality — Score: 79/100

### Strengths

- Comprehensive single-page coverage of every traveler need: attractions, weather, altitude, hotels, transport, costs, packing, visas, food, solo travel, FAQ
- All 14 detail pages carry substantial, practical content (10-15 KB each) with ticket prices, transport options, best seasons, altitude data
- Original comparison content (Shangri-La vs Tibet table) targets a real comparison-intent keyword
- Marked "Updated August 2026" — strong freshness signal

### High

**H1: Detail pages orphaned from each other** — each page links only to `/`. A user on Pudacuo cannot navigate to Songzanlin without going to the homepage. This creates poor internal PageRank flow and dead-end UX. Add "Related Attractions" cross-links.

**H2: No author or expertise signals** — no author name, bio, or About page. For YMYL-adjacent travel content (altitude health advice, safety guidance), E-E-A-T demands visible authorship.

### Medium

**M1: H1 contains HTML tags** — the homepage H1 uses `<br>` and `<span>` tags, diluting semantic heading signal. Use plain text: "Shangri-La Yunnan Travel Guide 2026".
**M2: Single-page trade-off** — weather, altitude guide, and transport sections could rank better as standalone pages targeting specific high-volume keywords.

---

## 3. On-Page SEO — Score: 75/100

### Strengths

- 100% alt text coverage on all 19 homepage images
- 18/19 images use `loading="lazy"` correctly
- Keyword-rich title tags across all pages
- Breadcrumb navigation UI on all detail pages

### High

**H1: OG image is SVG** — `og-image.svg` will not render on Facebook, Twitter, or LinkedIn. Social shares will show blank previews. Replace with a 1200x630 PNG.

### Medium

**M1: Formulaic title tags** — every detail page uses `"Page Title | Shangri-La Yunnan Travel Guide"`. Restructure to front-load unique content.
**M2: 38 H4 tags** — many card titles and labels are marked as H4 when they should be `<strong>` or `<dt>` elements.
**M3: Meta descriptions describe the page rather than the search intent** — "Complete guide to..." is weaker than "Plan your visit to...".

---

## 4. Schema — Score: 83/100

### Strengths

- 5 schema types on homepage: Organization, WebSite (with SearchAction), FAQPage (15 Q&As), TouristDestination (with GeoCoordinates), ItemList (6 TouristAttraction items)
- TouristAttraction schema with GeoCoordinates on all 14 detail pages
- Coordinates are accurate and match actual locations
- FAQPage targets real, high-intent traveler queries — strong rich-result candidate

### High

**H1: Missing BreadcrumbList schema** — visible breadcrumbs exist but no BreadcrumbList structured data. Add to DetailLayout.astro.
**H2: No `@id` cross-referencing** — Organization and TouristDestination schemas are not linked via `@id`, weakening the knowledge graph signal.

---

## 5. Performance — Score: 73/100

### Strengths

- All images in modern `.webp` format
- CSS is hashed for cache-busting (~45 KB total across 2 files)
- Minimal client-side JS; Leaflet map loads lazily

### High

**H1: No server-side compression** — the 131 KB homepage needs brotli/gzip compression configured at the CDN layer.

### Medium

**M1: Several images exceed 200 KB** — balagezong-canyon (384 KB), daocheng-yading (348 KB), lijiang-old-town (336 KB), yubeng-village (308 KB), tiger-leaping-gorge (268 KB). Compress further or serve responsive srcset variants.
**M2: Hero image missing `fetchpriority="high"`** — the hero image is the LCP element.
**M3: External Google Fonts block first paint** — verify `&display=swap` is enabled, or self-host the font.

### Estimated CWV (Lab)

| Metric | Estimate | Threshold |
|---|---|---|
| LCP | 1.8-2.5s | Good < 2.5s |
| INP | < 50ms | Good < 200ms |
| CLS | 0.02 | Good < 0.1 |

---

## 6. AI Search Readiness — Score: 56/100

### Strengths

- Rich structured data makes content highly parseable by AI crawlers
- Factual, structured answers align with how AI search engines select sources
- Single-page format allows efficient one-fetch content extraction

### High

**H1: No `llms.txt` or `llms-full.txt`** — AI crawlers (OpenAI, Anthropic, Google Extended) look for these files to discover content for AI-generated answers per the llmstxt.org standard.
**H2: No robots.txt means no AI crawler control** — cannot selectively allow/block `GPTBot`, `Claude-Web`, `PerplexityBot`, or `Google-Extended`.

---

## 7. Images — Score: 78/100

### Strengths

- 100% alt text coverage (19/19 homepage images)
- All images in .webp format
- Correct lazy-loading strategy (hero eager, others lazy)

### Medium

**M1: Several images exceed 200 KB** — balagezong (384 KB), daocheng (348 KB), lijiang (336 KB), yubeng (308 KB).
**M2: No responsive srcset** — all images use fixed `src` with no viewport-adaptive variants. Generate 400w, 800w, 1200w variants.

---

## Site Inventory

| # | Page | Type | Title | H1 | Schema | Canonical Issue |
|---|---|---|---|---|---|---|
| 1 | `/` | Homepage | Shangri-La Yunnan Travel Guide 2026 | H1 with HTML tags | 5 types | No |
| 2 | `/attractions/pudacuo-national-park/` | Attraction | Pudacuo National Park | Clean | TouristAttraction | Yes |
| 3 | `/attractions/songzanlin-monastery/` | Attraction | Songzanlin Monastery | Clean | TouristAttraction | Yes |
| 4 | `/attractions/dukezong-old-town/` | Attraction | Dukezong Old Town | Clean | TouristAttraction | Yes |
| 5 | `/attractions/napa-lake/` | Attraction | Napa Lake | Clean | TouristAttraction | Yes |
| 6 | `/attractions/tiger-leaping-gorge/` | Attraction | Tiger Leaping Gorge | Clean | TouristAttraction | Yes |
| 7 | `/attractions/meili-snow-mountain/` | Attraction | Meili Snow Mountain | Clean | TouristAttraction | Yes |
| 8 | `/attractions/balagezong-canyon/` | Attraction | Balagezong Canyon | Clean | TouristAttraction | Yes |
| 9 | `/attractions/baishuitai-terraces/` | Attraction | Baishuitai Terraces | Clean | TouristAttraction | Yes |
| 10 | `/food/matsutake-mushrooms/` | Food | Matsutake Mushrooms | Clean | Recipe/Food | Yes |
| 11 | `/food/morning-chanting/` | Food | Morning Chanting | Clean | Event | Yes |
| 12 | `/food/tibetan-barley-wine/` | Food | Tibetan Barley Wine | Clean | Recipe/Food | Yes |
| 13 | `/food/tsampa/` | Food | Tsampa | Clean | Recipe/Food | Yes |
| 14 | `/food/yak-butter-tea/` | Food | Yak Butter Tea | Clean | Recipe/Food | Yes |
| 15 | `/food/yak-hotpot/` | Food | Yak Hotpot | Clean | Recipe/Food | Yes |

---

*Report generated by Codex SEO Audit — 2026-08-05*
