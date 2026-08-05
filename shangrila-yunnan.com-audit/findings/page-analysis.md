# Single Page SEO Analysis: shangri-la-yunnan.com

**URL**: https://shangri-la-yunnan.com/
**Analyzed**: 2026-08-05
**Page Type**: Homepage / Destination Hub (travel)

---

## Page Score Card

```
Overall Score: 87/100

On-Page SEO:     84/100  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱▱
Content Quality: 85/100  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱
Technical:       89/100  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
Schema:          90/100  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
Images:          93/100  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
```

---

## On-Page SEO — 84/100

### Title Tag
```
Shangri-La Yunnan Travel Guide 2026 | Complete Destination Hub
```
- **Length**: 62 characters (optimal: 50-60, slightly over but acceptable)
- **Pattern**: Brand name + Year + Pipe + Value proposition
- **Verdict**: Strong — includes primary keyword (Shangri-La Yunnan), year freshness signal, and a compelling hook. The pipe separator is well-chosen for clarity.

### Meta Description
```
Everything you need to plan the perfect Shangri-La Yunnan trip. Attractions, weather, altitude guide, hotels, transport, costs, food, and FAQs — all on one page.
```
- **Length**: 161 characters (optimal: 150-160, right at the limit)
- **Verdict**: Excellent — clearly communicates the single-page value prop, lists specific topics, ends with a compelling promise. Natural keyword integration without stuffing.

### Headings
| Tag | Count | Assessment |
|-----|-------|------------|
| H1 | 1 | "Shangri-La Yunnan Travel Guide 2026" — plain text, strong semantic signal |
| H2 | 17 | Well-distributed across sections: Attractions, Weather, Altitude, Stay, Transport, Costs, FAQ, etc. |
| H3 | 22 | Good sub-section structure (individual attractions, itinerary types) |
| H4 | 38 | Excessive — many card titles and labels marked as H4 where `<strong>` or `<dt>` would be more appropriate |

### URL
```
https://shangri-la-yunnan.com/
```
- Clean, descriptive root domain. No parameters, no subfolders. Ideal.

### Internal Links: 17
Well-distributed across sections. Main nav anchors + attraction/food links + footer links + sources. Good descriptive anchor text throughout.

### External Links: 10
- 4 service links (Google Fonts, CARTO tiles)
- 6 authoritative references (UNESCO, Wikipedia x3, TripAdvisor) in Sources section
- **Verdict**: Good — authoritative sources cited, proper `target="_blank" rel="noopener"` on external links.

### Issues
1. **[Medium] 38 H4 tags** — flatten decorative H4s to `<strong>` or `<dt>` elements. This would improve heading hierarchy clarity for both users and search engines.
2. **[Low] Title slightly long at 62 chars** — consider trimming to 58-60 chars for guaranteed full display in SERPs.

---

## Content Quality — 85/100

### Word Count: 3,827
Well above the 500-word homepage minimum. Comprehensive topical coverage across 17 sections.

### Readability
- **Flesch Reading Ease**: 41.6 (below 60-70 ideal range)
- **Avg sentence length**: 11.5 words (within 15-20 target)
- **Verdict**: Acceptable for travel content. The lower score is driven by Tibetan/Chinese place names (Songzanlin, Dukezong, Balagezong) and technical terms (acclimatization, acetazolamide). Sentence-level readability is good.

### Keyword Density (natural, 1-3%)
| Keyword | Density |
|---------|---------|
| shangri-la | 1.26% |
| altitude | 0.67% |
| tibetan | 0.59% |
| travel | 0.46% |
| guide | 0.46% |

No keyword stuffing detected. Semantic variations present across sections.

### E-E-A-T Signals
| Factor | Signal |
|--------|--------|
| Experience | First-hand price data, transport costs, altitude readings, specific times (6:30 AM chanting) |
| Expertise | Cultural depth (Tibetan Buddhism, Naxi), altitude medicine advice, geographic precision |
| Authority | About page with team credentials, 6 external citations to UNESCO/Wikipedia/TripAdvisor |
| Trust | Privacy policy page, contact email, "not affiliated" disclaimer, date stamps, author byline |

### Content Freshness
- **Published**: Implicit (site created 2024)
- **Last updated**: August 2026 (visible in footer and hero)
- **Verdict**: Strong freshness signal. No stale content detected.

### Issues
1. **[Low] Flesch score 41.6** — acceptable for travel niche. Occasional sentence splitting could improve readability for non-native English speakers.

---

## Technical — 89/100

### Canonical
```
https://shangri-la-yunnan.com/
```
Self-referencing, correct URL. No issues.

### Meta Robots
Not explicitly set — defaults to `index, follow`. Consider adding `<meta name="robots" content="index, follow">` for explicitness.

### Open Graph
| Tag | Content | Status |
|-----|---------|--------|
| og:title | Shangri-La Yunnan Travel Guide 2026 \| Complete Destination Hub | ✓ |
| og:description | Everything you need to plan the perfect Shangri-La Yunnan trip... | ✓ |
| og:image | https://shangri-la-yunnan.com/og-image.png | ✓ PNG format |
| og:image:width | 1200 | ✓ |
| og:image:height | 630 | ✓ |
| og:url | https://shangri-la-yunnan.com/ | ✓ |
| og:type | website | ✓ |

### Twitter Card
| Tag | Content | Status |
|-----|---------|--------|
| twitter:card | summary_large_image | ✓ |
| twitter:image | https://shangri-la-yunnan.com/og-image.png | ✓ |

### Hreflang
Not present. For a single-language (English) site, `x-default` hreflang self-reference is ideal but not critical.

### Performance Signals (lab estimates)

| Signal | Status |
|--------|--------|
| Hero image has `fetchpriority="high"` | ✓ |
| CSS is hashed for cache-busting | ✓ |
| Minimal client JS (~5 KB minified) | ✓ |
| Google Fonts with `display=swap` | ✓ |
| Leaflet map lazy-loaded | ✓ |
| Missing explicit `meta robots` tag | Minor |

### Core Web Vitals Estimates

| Metric | Estimate | Threshold |
|--------|----------|-----------|
| LCP | 1.8-2.5s | Good < 2.5s |
| INP | < 50ms | Good < 200ms |
| CLS | 0.02 | Good < 0.1 |

Note: these are static-analysis estimates. Real CrUX field data requires live traffic in Google Search Console.

### Issues
1. **[Low] No explicit `<meta name="robots">` tag** — add for clarity.
2. **[Low] No hreflang `x-default`** — optional but recommended even for single-language sites.
3. **[Low] No structured `datePublished` / `dateModified` meta tags** — consider adding for explicit freshness signals.

---

## Schema Markup — 90/100

### Detected Types (JSON-LD)

| # | Type | Required Properties | Status |
|---|------|---------------------|--------|
| 1 | Organization | name, url, logo | ✓ All present |
| 2 | WebSite | name, url, potentialAction | ✓ SearchAction configured |
| 3 | FAQPage | mainEntity (14 items) | ✓ Well-formed Q&A pairs |
| 4 | TouristDestination | name, description, geo, address | ✓ GeoCoordinates present |
| 5 | ItemList | itemListElement (6 TouristAttraction items) | ✓ Each has position + name + geo |

### Schema Opportunities
1. **[Medium] Add BreadcrumbList** — for the homepage itself: `Home` as the single item. Minor value-add but completes schema coverage.
2. **[Medium] Add `sameAs` to Organization** — link to TripAdvisor, Wikidata, social profiles for entity resolution strength.
3. **[Low] SearchAction target `/search?q=` may not exist** — implement a search page or remove the SearchAction to avoid misleading schema.

### FAQPage Note
Google retired FAQ *rich results* in May 2026, but FAQPage markup remains valuable as an AI citation signal — particularly for AI Overviews and AI Mode (Gemini 3.5 Flash). Keep the markup. Do not replace with QAPage unless the page transforms into genuine user-submitted Q&A.

---

## Images — 93/100

### Coverage
- **19 images total** on homepage
- **100% alt text coverage** — all 19 images have descriptive alt attributes
- **1 hero image** (eager, no lazy load, has `fetchpriority="high"`)
- **18 below-fold images** with `loading="lazy"`

### Format & Size
All images are `.webp` — excellent format choice.

| Image | Size | Status |
|-------|------|--------|
| shangri-la-hero.webp | 194 KB | ✓ Good |
| balagezong-canyon.webp | 297 KB | ⚠ Warning (>200 KB) |
| daocheng-yading.webp | 269 KB | ⚠ Warning |
| lijiang-old-town.webp | 265 KB | ⚠ Warning |
| yubeng-village.webp | 224 KB | ⚠ Warning |
| 14 remaining images | 100-215 KB | ✓ Acceptable |

### CLS Prevention
All images have explicit `width` and `height` attributes set — good CLS prevention.

### Issues
1. **[Medium] 4 images exceed 200 KB** — while no image exceeds the 500 KB critical threshold, compression to sub-200 KB is recommended for mobile performance. Already compressed from 300-384 KB originals — further optimization would require `cwebp` with quality 65 or responsive `srcset`.
2. **[Low] No responsive `srcset`** — serving fixed-resolution images to all viewports. Consider generating 400w/800w/1200w variants.

---

## Keyword & Topic Coverage

The page comprehensively covers the following topic clusters:

| Topic | Coverage | Format |
|-------|----------|--------|
| Attractions | 8 locations with details | Cards with links to detail pages |
| Weather | 12-month table | Structured table |
| Altitude guide | 8 locations + acclimatization timeline | Data table + timeline |
| Accommodation | 3 areas (Old Town, New Town, Countryside) | Descriptive sections |
| Transport | Flight routes + bus/taxi/expressway | Structured options |
| Costs | Budget/Mid-range/Luxury tiers | Tiered breakdown |
| Packing | Essential items list | Bulleted list |
| China visa entry | 38+ countries, transit visas | Informational section |
| Food & culture | 6 items with detail page links | Cards |
| Travel tips | VPN, cash, language, photography | Bulleted tips |
| Solo travel | Safety, social tips | Section |
| FAQ | 14 questions | FAQPage schema + accordion |
| Shangri-La vs Tibet | 9-row comparison table | Comparison table |
| Nearby destinations | 4 locations | Cards |
| Sources | 6 authoritative references | Link list |

**Verdict**: Excellent topical breadth. The page answers nearly every question a traveler would ask before visiting Shangri-La.

---

## Issues Summary

| # | Priority | Issue | Expected Impact |
|---|----------|-------|-----------------|
| 1 | Medium | 38 H4 tags — flatten decorative headings to semantic elements | Improves heading hierarchy for SEO + accessibility |
| 2 | Medium | 4 images still >200 KB (balagezong, daocheng, lijiang, yubeng) | Marginal LCP improvement on mobile |
| 3 | Medium | Add BreadcrumbList schema to homepage | Completes schema coverage |
| 4 | Low | Title 62 chars — slightly over 60-char SERP display limit | Minor: may truncate on some SERPs |
| 5 | Low | No explicit `<meta name="robots">` tag | Minor: defaults are correct but explicit is better |
| 6 | Low | No hreflang `x-default` self-reference | Minor for single-language site |
| 7 | Low | No responsive `srcset` for images | Minor: affects mobile bandwidth only |
| 8 | Low | No `datePublished`/`dateModified` meta tags | Minor: freshness signals could be stronger |
| 9 | Low | SearchAction `/search?q=` may be a dead URL | Minor: implement or remove |

---

## Recommendations

### Quick Wins (This Week)
1. Add explicit `<meta name="robots" content="index, follow">` to BaseLayout.astro
2. Trim title to 58-60 chars: "Shangri-La Yunnan Travel Guide 2026 — Complete Destination Hub"
3. Add hreflang `x-default` self-reference

### Short Term (This Month)
4. Flatten decorative H4 elements to `<strong>` or `<p class="...">` — target reducing from 38 to ~15 genuine H4s
5. Add `datePublished` and `dateModified` meta tags
6. Add BreadcrumbList schema for homepage

### Longer Term
7. Generate responsive `srcset` for all images (400w, 800w, 1200w variants)
8. Replace SearchAction schema with a real search implementation, or remove if not planned

---

*Analysis generated by Codex SEO Page Analysis — 2026-08-05*
