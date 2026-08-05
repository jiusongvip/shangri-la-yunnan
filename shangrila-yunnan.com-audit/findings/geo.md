## AI Search Readiness Findings — shangri-la-yunnan.com

### What Works Well

- Rich structured data (Organization, FAQPage, TouristDestination, TouristAttraction with GeoCoordinates) makes the site highly parseable by AI crawlers
- Content is factual, structured, and answers real traveler questions — this aligns well with how AI search engines (ChatGPT, Perplexity, Google AI Overviews) select and cite sources
- Single-page comprehensive format means an AI crawler can extract nearly all site knowledge from one fetch

### High

**H1: No llms.txt or llms-full.txt**
There is no `/llms.txt` file at the root. AI crawlers (Anthropic, OpenAI, Google Extended) increasingly look for `llms.txt` (per llmstxt.org) to discover what content to crawl and index for AI-generated answers. Create both `/llms.txt` (structured index) and `/llms-full.txt` (full content for AI ingestion).

**H2: No `robots.txt` — AI crawlers cannot be directed**
Without a robots.txt, you cannot selectively allow/block AI-specific crawlers like `GPTBot`, `Claude-Web`, `PerplexityBot`, or `Google-Extended`. This means you have no control over whether or how AI companies use your content for training or real-time search.

### Medium

**M1: Brand mentions not reinforced with external citations**
AI models cite sources with high authority signals. The site would benefit from being referenced on Wikipedia, Wikidata, TripAdvisor, and travel media — external signals that increase the likelihood of AI citation.

**M2: No JSON-LD `citation` or `sameAs` linking**
Connecting the Organization schema to external profiles (TripAdvisor destination page, Wikidata Q-id, Google Knowledge Graph ID) would strengthen entity resolution for AI systems.

**M3: Factual claims lack inline citations**
Several claims (e.g., "Shangri-La County covers 11,613 km² — larger than Jamaica", "Songzanlin Monastery was built in 1679") are specific and verifiable but have no source attribution. AI models prefer content with clear provenance.

### Score

| Sub-category | Score | Notes |
|---|---|---|
| Structured Data | 90/100 | Excellent schema coverage |
| AI Crawler Access | 30/100 | No llms.txt, no robots.txt guidance |
| Citability | 55/100 | Strong content, weak external signals |
| Authority Signals | 50/100 | No author, no citations, no sameAs |
| **AI Readiness Score** | **56/100** | |
