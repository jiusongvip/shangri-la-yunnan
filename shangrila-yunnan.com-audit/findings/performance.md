## Performance Findings — shangri-la-yunnan.com

### What Works Well

- All images are in modern `.webp` format with `loading="lazy"` on below-fold images
- Total CSS is ~45 KB across 2 files — compact for a site of this scope
- CSS is hashed (`index.Bjcc5Ay6.css`, `baishuitai-terraces.CHvqPn9Q.css`) for cache-busting
- No heavy JavaScript framework on the client; only minimal vanilla JS for smooth scroll, mobile menu toggle, and Leaflet map
- The Leaflet map is loaded lazily — it won't block initial render

### High

**H1: No server-side compression configured**
The deployment stack (unknown — could be Cloudflare Pages, Vercel, Netlify, or raw static hosting) must deliver gzip or brotli compression. The 131 KB homepage will compress to roughly 25–35 KB with brotli, but without it, first-byte time suffers.

**H2: External Google Fonts block first paint**
Three external requests (`fonts.googleapis.com` CSS + two `fonts.gstatic.com` font files) are render-blocking. The Outfit font is used for display headings — a `font-display: swap` strategy (already supported by Google Fonts `&display=swap` parameter) should be explicitly verified. Better yet, self-host the font subset.

### Medium

**M1: Several images exceed 200 KB**
| Image | Size |
|---|---|
| balagezong-canyon.webp | 384 KB |
| daocheng-yading.webp | 348 KB |
| lijiang-old-town.webp | 336 KB |
| yubeng-village.webp | 308 KB |
| tiger-leaping-gorge.webp | 268 KB |

These contribute significantly to LCP on their respective pages. Compress further or serve responsive `srcset` variants.

**M2: No resource hints for key origins**
Adding `<link rel="dns-prefetch">` for `unpkg.com` (Leaflet) and `<link rel="preload">` for the hero image would improve perceived load time.

**M3: Homepage hero image has no explicit `fetchpriority="high"`**
The hero image is the LCP element. Adding `fetchpriority="high"` tells the browser to prioritize it.

### Low

**L1: No `<meta name="theme-color">`**
A minor PWA-ready signal that also avoids a flash of white background on mobile browsers.

### Estimated Core Web Vitals (Lab)

| Metric | Estimate | Threshold |
|---|---|---|
| LCP | 1.8–2.5s | Good < 2.5s |
| INP | < 50ms | Good < 200ms |
| CLS | 0.02 | Good < 0.1 |

Note: these are static-analysis estimates. Real CrUX field data requires the site to be live and receiving traffic.

### Score

| Sub-category | Score | Notes |
|---|---|---|
| Resource Optimization | 70/100 | Large images, no responsive srcset |
| Render Performance | 72/100 | Font blocks, no fetchpriority |
| CWV Readiness | 78/100 | Light JS, good CLS, LCP improvable |
| **Performance Score** | **73/100** | |
