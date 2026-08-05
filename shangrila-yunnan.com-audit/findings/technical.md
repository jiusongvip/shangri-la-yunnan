## Technical SEO Findings — shangri-la-yunnan.com

### Critical

**C1: All detail-page canonicals resolve to localhost**
All 14 detail pages (8 attractions + 6 food) have `<link rel="canonical" href="http://localhost:4321/…">` because `DetailLayout.astro` uses `Astro.url.href` which resolves to the dev server URL during `astro build`. Google will index production pages with these wrong canonicals if deployed as-is. **Fix**: replace `Astro.url.href` with `https://shangri-la-yunnan.com${Astro.url.pathname}` in [DetailLayout.astro](D:\workspaces\website\shangri-la-yunnan\shangri-la-yunnan-site\src\layouts\DetailLayout.astro:36), and apply the same fix for the homepage in [BaseLayout.astro](D:\workspaces\website\shangri-la-yunnan\shangri-la-yunnan-site\src\layouts\BaseLayout.astro:30).

**C2: No robots.txt**
The `dist/` directory contains no `robots.txt`. Without one, crawlers have no guidance on which paths to prioritize or avoid. This is a mandatory file for any production site.

**C3: No XML sitemap**
No `sitemap.xml` exists in the build output. Search engines rely on sitemaps to discover all 15 pages efficiently. Given the site has only 15 HTML pages, this is a straightforward fix — generate a static sitemap or use `@astrojs/sitemap`.

### High

**H1: No 404 error page**
There is no fallback `404.html` page. Users following broken links or mistyped URLs see the default hosting error page, which degrades UX and signals poor site quality to search engines.

**H2: No cache-control or security headers**
A static deployment has no mechanism to deliver `Cache-Control`, `X-Content-Type-Options`, or `Strict-Transport-Security` headers. These should be configured at the CDN or hosting layer (Cloudflare, Vercel, Netlify, etc.).

**H3: Trailing-slash inconsistency risk**
The Astro config does not specify a `trailingSlash` preference. Detail pages are built at `/attractions/pudacuo-national-park/index.html`, so they resolve both with and without trailing slashes. Without a redirect rule, this creates duplicate-content risk.

### Medium

**M1: External render-blocking fonts**
Two Google Fonts preconnect hints and a blocking `<link>` to Outfit from `fonts.googleapis.com` add a third-party dependency that delays first paint. Consider self-hosting the font or using `font-display: swap`.

**M2: Multiple schema blocks**
The homepage emits 5 separate `<script type="application/ld+json">` blocks (Organization, WebSite, FAQPage, TouristDestination, ItemList). While valid, this bloats the `<head>`. Merging into a single `@graph` wrapper or a single array would be cleaner.

**M3: Static HTML page weight**
The homepage is ~131 KB of raw HTML (uncompressed). With gzip/brotli this will compress well, but it is substantially larger than a typical landing page due to all sections being on a single page. This is a design choice but worth monitoring.

### Low

**L1: No security.txt**
A `/security.txt` or `/.well-known/security.txt` file is recommended for vulnerability disclosure.

**L2: No hreflang tags**
For a single-language (English) site, hreflang is not strictly required, but an `x-default` hreflang self-reference is good practice for international SEO clarity.

**L3: SVG favicon**
Using `favicon.svg` is modern and fine for most browsers, but adding a `.ico` fallback ensures compatibility with older crawlers and bookmark systems.

### Score

| Sub-category | Score | Notes |
|---|---|---|
| Crawlability | 40/100 | No robots.txt, no sitemap, canonical bug |
| Indexability | 45/100 | Wrong canonicals = duplicate-index risk |
| Security | 50/100 | No security headers, no TLS enforcement |
| URL Structure | 85/100 | Clean paths, good hierarchy |
| Mobile | 100/100 | Responsive viewport, mobile-first |
| Core Web Vitals | 75/100 | Light CSS, but render-blocking fonts |
| **Technical SEO Score** | **66/100** | |
