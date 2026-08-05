# SEO Action Plan: shangri-la-yunnan.com

**Overall Health Score**: 72/100
**Generated**: 2026-08-05

---

## Phase 1: Critical Fixes — Week 1

These issues directly impact indexability and social sharing. Fix before production deployment.

### 1.1 Fix canonical URLs (Critical)

**Issue**: All 14 detail page canonicals resolve to `http://localhost:4321/...`
**Files to edit**:
- `DetailLayout.astro` line 36 — change `Astro.url.href` to `` `https://shangri-la-yunnan.com${Astro.url.pathname}` ``
- `BaseLayout.astro` line 30 — same fix
**Effort**: 5 minutes

### 1.2 Create robots.txt (Critical)

**Issue**: No `robots.txt` in the build output.
**Action**: Add `public/robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://shangri-la-yunnan.com/sitemap.xml

User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /
```
**Effort**: 5 minutes

### 1.3 Generate sitemap.xml (Critical)

**Issue**: No sitemap for 15 pages.
**Action**: Install `@astrojs/sitemap` and add to `astro.config.mjs`:
```js
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  integrations: [tailwind(), sitemap()],
  site: 'https://shangri-la-yunnan.com',
});
```
**Effort**: 10 minutes

### 1.4 Replace OG image (High)

**Issue**: `og-image.svg` breaks on Facebook, Twitter, LinkedIn.
**Action**: Create a 1200x630 PNG (use the hero image or generate one) and update references in both layout files.
**Effort**: 15 minutes

### 1.5 Add fetchpriority to hero image (Medium)

**Action**: Add `fetchpriority="high"` to the hero `<img>` in `index.astro`.
**Effort**: 1 minute

---

## Phase 2: High-Impact Improvements — Weeks 2-3

These changes meaningfully improve search visibility and crawl efficiency.

### 2.1 Add BreadcrumbList schema (High)

**Action**: In DetailLayout.astro, add JSON-LD BreadcrumbList alongside the existing TouristAttraction schema. The breadcrumb UI is already rendered — just add the structured data.
**Effort**: 20 minutes

### 2.2 Add @id cross-referencing (High)

**Action**: Add `@id` values to homepage schema blocks and cross-reference them (e.g., `"publisher": {"@id": "#org"}`).
**Effort**: 15 minutes

### 2.3 Create llms.txt and llms-full.txt (High)

**Action**: Create `/public/llms.txt` (AI crawler index) and `/public/llms-full.txt` (full content for AI ingestion). See llmstxt.org for format.
**Effort**: 30 minutes

### 2.4 Build 404 page (High)

**Action**: Create `src/pages/404.astro` with navigation back to the homepage and links to key sections.
**Effort**: 15 minutes

### 2.5 Add cross-links between detail pages (High)

**Action**: Add "Related Attractions" or "You Might Also Like" sections on each detail page, linking to 2-3 related pages. This improves internal PageRank flow and user navigation.
**Effort**: 1 hour

### 2.6 Compress large images (Medium)

**Action**: Re-compress these images at quality 75-80:
- balagezong-canyon.webp (384 KB to ~200 KB)
- daocheng-yading.webp (348 KB to ~190 KB)
- lijiang-old-town.webp (336 KB to ~180 KB)
- yubeng-village.webp (308 KB to ~170 KB)
- tiger-leaping-gorge.webp (268 KB to ~150 KB)
**Effort**: 15 minutes

---

## Phase 3: Content & Authority — Month 2

These changes build long-term authority and improve content signal strength.

### 3.1 Add author byline and About page

Create an About page with author credentials, expertise, and site purpose. Add author byline to detail pages.
**Effort**: 1 hour

### 3.2 Restructure homepage H1 to plain text

Replace `<h1>Shangri-La<br><span>Travel Guide</span></h1>` with `<h1>Shangri-La Yunnan Travel Guide 2026</h1>` and style via CSS.
**Effort**: 10 minutes

### 3.3 Add source citations

Add links or references for key factual claims (monastery construction date, county area, peak elevation).
**Effort**: 30 minutes

### 3.4 Create responsive srcset for images

Generate 400w, 800w, 1200w variants for each image and use `srcset` + `sizes` attributes.
**Effort**: 1 hour (with automation)

### 3.5 Add sameAs links

Add TripAdvisor destination page, Wikidata Q-id, and social profiles to Organization schema.
**Effort**: 15 minutes

### 3.6 Self-host fonts or fix font-display

Either download Outfit font files to `/public/fonts/` and reference locally, or verify `&display=swap` is active on the Google Fonts URL.
**Effort**: 20 minutes

### 3.7 Reduce H4 count

Audit homepage headings. Replace decorative H4s (card titles, labels) with `<strong>`, `<dt>`, or styled `<p>` elements.
**Effort**: 45 minutes

---

## Phase 4: Monitoring & Iteration — Ongoing

### 4.1 Set up Google Search Console

Submit sitemap, monitor index coverage, fix any crawl errors.

### 4.2 Deploy with CDN compression

Ensure brotli/gzip is enabled at the CDN layer (Cloudflare, Vercel, Netlify). Configure security headers: `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.

### 4.3 Monitor Core Web Vitals

Once live, monitor CrUX data in Google Search Console for real-user LCP, INP, and CLS.

### 4.4 Build external citations

Get the site referenced on Wikipedia (Shangri-La City article), Wikidata, TripAdvisor, travel blogs, and news media to strengthen entity identity.

### 4.5 Consider topic-specific standalone pages

If traffic data shows high demand for specific subtopics (weather, altitude guide), spin them into dedicated pages targeting high-volume keywords.

### 4.6 Set up SEO drift monitoring

Capture baselines of critical SEO elements (title tags, canonicals, schema) and monitor for unintended changes during deployments.

---

## Estimated Total Effort

| Phase | Items | Estimated Time |
|---|---|---|
| Phase 1: Critical Fixes | 5 items | ~35 minutes |
| Phase 2: High-Impact | 6 items | ~3 hours |
| Phase 3: Content & Authority | 7 items | ~4 hours |
| Phase 4: Ongoing | 6 items | Continuous |
| **Total (one-time)** | **18 items** | **~7.5 hours** |
