## Schema & Structured Data Findings — shangri-la-yunnan.com

### What Works Well

- Homepage deploys 5 schema types: Organization, WebSite (with SearchAction), FAQPage (15 Q&As), TouristDestination (with GeoCoordinates), and ItemList (6 TouristAttraction items)
- All 14 detail pages carry `TouristAttraction` schema with geo coordinates
- Coordinates are realistic and match the actual locations
- FAQPage is well-populated with real, high-intent traveler questions — this is a strong candidate for rich results

### High

**H1: No BreadcrumbList schema on detail pages**
Detail pages have visible breadcrumbs (`Home > Attractions > Pudacuo National Park`) rendered in the UI but no corresponding `BreadcrumbList` structured data. Adding this is a straightforward win for rich-result eligibility.

**H2: No `@id` cross-referencing**
The Organization and TouristDestination schemas share an entity but are not linked via `@id`. Adding `@id` values and cross-referencing them (e.g., `"publisher": {"@id": "#org"}`) strengthens the knowledge graph signal.

### Medium

**M1: Homepage emits 5 separate `<script>` blocks**
While all valid, merging them into a single `@graph` array (or at least reducing the block count) is cleaner and easier to validate.

**M2: No `aggregateRating` or `review` schema**
For a travel destination hub, review/rating signals (even a manually curated "Visitors rate Shangri-La 4.7/5") would add social proof and qualify for star-rich results.

**M3: Organization schema has a logo but no `sameAs` links**
Adding `sameAs` for social profiles (TripAdvisor, Instagram, etc.) would strengthen entity identity.

### Low

**L1: SearchAction `target` URL may not exist**
`"target": "https://shangri-la-yunnan.com/search?q={search_term_string}"` — if no search page exists at that path, this schema becomes misleading. Either implement a search page or remove the SearchAction.

**L2: No `openingHours` on TouristAttraction schemas**
Minor for natural attractions, but venues like Songzanlin Monastery and Pudacuo have ticketed hours that could benefit from `openingHours` schema.

### Score

| Sub-category | Score | Notes |
|---|---|---|
| Presence | 95/100 | Excellent coverage across all page types |
| Validation | 90/100 | All schemas appear well-formed |
| Rich Result Potential | 80/100 | FAQPage is strong; missing BreadcrumbList |
| Entity Identity | 65/100 | No @id linking, no sameAs |
| **Schema Score** | **83/100** | |
