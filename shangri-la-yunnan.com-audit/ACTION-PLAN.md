# Action Plan — shangri-la-yunnan.com

**Generated:** 2026-08-05 | **Health Score:** 82/100

---

## Phase 1: Critical Fixes — Today

### 1.1 Convert PNG to WebP (🔴 Critical)
**File:** `public/images/snub-nosed-monkey.png` (2.34 MB → target ~180 KB)
```
sharp-cli -i public/images/snub-nosed-monkey.png -o public/images/snub-nosed-monkey.webp --quality 80
```
Then update `src/pages/index.astro` line 382: `snub-nosed-monkey.png` → `snub-nosed-monkey.webp`

### 1.2 Recompress 3 Oversized Images (🟠 High)
Target <200 KB each:
- `public/images/balagezong-canyon.webp` (290 KB)
- `public/images/lijiang-old-town.webp` (259 KB)
- `public/images/daocheng-yading.webp` (256 KB)

### 1.3 Add `decoding="async"` (🟠 High)
Add `decoding="async"` to all 4 `<img>` tags in `index.astro` that have `loading="lazy"`:
- Line 335 (attraction thumbnails)
- Line 382 (snub-nosed monkey)
- Line 822 (food images)
- Line 978 (nearby destinations)

### 1.4 Delete Unused PNG (🟠 High)
Remove `public/og-image.png` (9.4 KB legacy file).

---

## Phase 2: High-Impact — This Week

### 2.1 Self-Host Google Fonts (🟠 High)
Move Outfit font to local `public/fonts/` and replace Google Fonts `<link>` with local `@font-face` declarations.

### 2.2 Add Sitemap Metadata (🔴 Critical)
Customize `astro.config.mjs`:
```js
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://shangri-la-yunnan.com",
  integrations: [
    sitemap({
      serialize(item) {
        item.lastmod = new Date("2026-08-05");
        if (item.url === "https://shangri-la-yunnan.com/") item.priority = 1.0;
        else if (item.url.includes("/attractions/")) item.priority = 0.8;
        else if (item.url.includes("/food/")) item.priority = 0.7;
        else item.priority = 0.5;
        return item;
      },
    }),
  ],
});
```

### 2.3 Add TouristAttraction Schema (🟡 Medium)
Add JSON-LD `TouristAttraction` to each of 9 attraction pages.

### 2.4 Create llms.txt (🟡 Medium)
Create `public/llms.txt`:
```
# Shangri-La Yunnan Travel Guide
> Complete travel planning hub for Shangri-La, Yunnan, China.

## Core Pages
- [Home]: https://shangri-la-yunnan.com - Complete travel guide with attractions, weather, altitude, hotels, transport, food, FAQs
- [About]: https://shangri-la-yunnan.com/about - Team credentials, first-hand experience in Yunnan

## Attractions
- [Pudacuo]: https://shangri-la-yunnan.com/attractions/pudacuo-national-park
- [Songzanlin]: https://shangri-la-yunnan.com/attractions/songzanlin-monastery
...
```

---

## Phase 3: Content & Authority — This Month

### 3.1 Visible Breadcrumbs (🟡 Medium)
Add breadcrumb component matching the JSON-LD BreadcrumbList schema.

### 3.2 Comment System (🟡 Medium)
Integrate Giscus (GitHub Discussions-based, no tracking) or Disqus.

### 3.3 Sub-Page Heading Structure (🟡 Medium)
Add `<h2>` subsections to attraction and food page templates.

### 3.4 Responsive Images (🟠 High)
Add `srcset` to hero and key images for mobile optimization.

---

## Phase 4: Monitoring — Ongoing

- Set up Google Search Console for indexation tracking
- Monitor Core Web Vitals via PageSpeed Insights / CrUX
- Track keyword rankings for target terms
- Set up SEO drift baseline for regression detection
