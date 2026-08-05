# Content Quality & E-E-A-T Analysis: shangri-la-yunnan.com

**Date**: 2026-08-05
**Analyzed**: Homepage (3,827 words) + 3 sample detail pages
**Methodology**: Google E-E-A-T QRG (Sept 2025) + Who/How/Why test + GEO/AI citation readiness

---

## Google's "Who / How / Why" Test

| Question | Assessment |
|---|---|
| **Who** created it? | About page states "small team of travel writers and photographers based in Yunnan" with "200+ days traveling across northwest Yunnan." Some credibility, but no individual author names or bios visible on articles. |
| **How** was it created? | Claims "first-hand verification" of prices, schedules, and opening hours. Content contains specific, non-generic data (exact ticket prices, bus departure times, altitude readings) that supports this claim. |
| **Why** does it exist? | Stated purpose: "to help travelers discover the authentic Shangri-La." The content is genuinely helpful — comprehensive, well-organized, and answer-focused. Does not read as thin affiliate content or AI-generated filler. |

**Verdict**: Passes the helpful-content test. The About page creates credible attribution, but individual author bylines would strengthen "Who" significantly.

---

## E-E-A-T Breakdown

### Experience (First-Hand Signals): 19 / 25

| Evidence | Signal Strength |
|---|---|
| Specific ticket prices for every attraction and food item (115 RMB, 100 RMB, 60 RMB, free, etc.) | Strong |
| Transport methods with real costs (Didi 80-120 RMB, shuttle bus 30 RMB) | Strong |
| Altitude data for each location with acclimatization timeline | Strong |
| "Updated August 2026" freshness signal | Moderate |
| About page claims 200+ days of travel experience | Moderate |
| Morning chanting schedule (6:30 AM) | Strong |
| No personal anecdotes or first-person narratives in body content | Missing |
| No photos attributed to individual photographers | Missing |

### Expertise: 21 / 25

| Evidence | Signal Strength |
|---|---|
| Deep cultural knowledge (Tibetan Buddhism, Naxi Dongba, monastery history) | Strong |
| Altitude medicine advice (Diamox dosing, 3-4L hydration) — medically accurate | Strong |
| Geographic precision (coordinates, distances, county area 11,613 km²) | Strong |
| About page claims local cultural consultants reviewed content | Moderate |
| Comprehensive topic clustering (weather, altitude, transport, costs, food, visas) | Strong |
| No individual author credentials per article | Missing |
| No formal qualifications or certifications stated | Missing |

### Authoritativeness: 13 / 25

| Evidence | Signal Strength |
|---|---|
| About page with team description | Moderate |
| "Not affiliated with any hotel or tour company" — neutrality signal | Moderate |
| No external citations or references (zero attribution for factual claims) | Critical gap |
| No links to authoritative sources (UNESCO, government tourism sites, academic sources) | Critical gap |
| No evidence of being cited by other experts or travel publications | Missing |
| No Wikipedia, Wikidata, or TripAdvisor entity presence verified | Missing |

### Trustworthiness: 16 / 25

| Evidence | Signal Strength |
|---|---|
| About page with transparency (who we are, our commitment) | Good |
| Date stamps on homepage and footer ("Last updated: August 2026") | Good |
| Disclaimer: "Not affiliated with any hotel or tour company" | Good |
| Content is honest about limitations (e.g., "Hotels in the new town offer more consistent comfort") | Good |
| No contact email or form on About page — just "please reach out" without mechanism | Problematic |
| No privacy policy | Missing |
| No terms of service | Missing |
| HTTPS (production must enforce) | TBD |
| No customer testimonials or review signals | Missing |

---

## Content Quality Score: 74 / 100

| Sub-category | Score | Weight | Notes |
|---|---|---|---|
| E-E-A-T (combined) | 69 | 40% | Strong Experience/Expertise, weak Authority |
| Content Structure | 85 | 15% | Clean heading hierarchy, scannable sections |
| Readability | 72 | 10% | Flesch 41.6 — acceptable for travel content |
| Multimedia | 90 | 10% | Images with alt, map, tables, comparison |
| Internal Linking | 80 | 10% | Cross-links exist, 17 internal on homepage |
| External Linking / Citations | 25 | 10% | 4 external links, zero source citations |
| Freshness | 85 | 5% | Dated, recently updated |
| **Weighted** | **74** | **100%** | |

---

## Content Metrics

| Metric | Homepage | Detail Page (avg) | Threshold |
|---|---|---|---|
| Word count | 3,827 | ~650 | 500 / 800 |
| Sentence count | 332 | ~55 | — |
| Avg sentence length | 11.5 words | ~12 | 15-20 ideal |
| Flesch Reading Ease | 41.6 | ~50 est. | 60-70 |
| H2 count | 17 | 5-6 | — |
| H3 count | 22 | 3-4 | — |
| Internal links | 17 | 4-5 | 3-5 per 1000 words |
| External links | 4 | 0 | 1-2 minimum |

### Readability Note

Flesch score of 41.6 is on the lower end. This is partly due to:
- Tibetan/Chinese place names (Songzanlin, Dukezong, Balagezong) driving up syllable counts
- Technical travel terms (acclimatization, acetazolamide, travertine)
- The score is acceptable for an informational travel guide aimed at an educated audience

Recommendation: simplify occasional complex sentences. Example — "Pudacuo National Park was established in 2007 as China's first national park under IUCN standards. Spanning over 1,300 square kilometers..." could be split.

---

## AI Citation Readiness: 76 / 100

### Strengths

- FAQPage schema with 14 well-formed Q&A pairs — highly extractable by AI crawlers
- Clear question-answer structure throughout the homepage
- TouristAttraction schema with GeoCoordinates — precise entity resolution
- Tables (weather, costs, comparison) are inherently citable data formats
- Specific, quotable statistics ("11,613 km² — larger than Jamaica", "built in 1679")
- First-party data (ticket prices, transport costs, altitude readings)

### Gaps

- No llms.txt or llms-full.txt — AI crawlers must parse full HTML
- No external source attributions — AI models penalize uncited factual claims
- No inline citations or references section
- No Person/author schema — AI systems cannot attribute content to a specific entity
- Organization schema has no sameAs links (Wikidata, TripAdvisor)

### Multi-Platform Readiness

| Platform | Readiness | Notes |
|---|---|---|
| Google AI Overviews | Good | FAQPage + structured data + quotable data |
| Google AI Mode (Gemini 3.5 Flash) | Good | Same signals as AI Overviews |
| ChatGPT Search | Moderate | Needs llms.txt + source citations |
| Perplexity | Moderate | Benefits from explicit citations |
| Bing Copilot | Good | Strong schema helps entity resolution |

---

## Issues Found

1. **[High] No external citations for factual claims** — "built in 1679," "11,613 km²," "largest Tibetan Buddhist monastery in Yunnan" — all verifiable but unattributed. This weakens Authority and AI citability.
2. **[High] About page has no contact mechanism** — "please reach out" without email, form, or social links. This damages Trustworthiness.
3. **[Medium] No individual author bylines on articles** — the About page describes a team, but individual pages lack named attribution. Adding author names + short bios would boost E-E-A-T.
4. **[Medium] No privacy policy** — basic trust signal missing. A simple privacy page (no tracking, no cookies) is sufficient for credibility.
5. **[Medium] Limited external links** — only 4 external links on 3,827-word homepage (to Google Fonts CDN and map tiles, not content sources). Add 3-5 citations to authoritative sources.
6. **[Low] Flesch score of 41.6** — acceptable but could improve with occasional sentence splitting.
7. **[Low] No Person or author schema** — adding Person schema for authors would improve entity resolution for AI crawlers.

---

## Recommendations

### Priority 1 — Authority Boost (This Week)
1. Add an email or contact form to the About page
2. Add 3-5 external citations to authoritative travel/nature sources (UNESCO, Lonely Planet, official tourism sites) on the homepage in appropriate sections
3. Add a simple privacy policy page at `/privacy`

### Priority 2 — Attribution (Next 2 Weeks)
4. Add author bylines to detail pages (e.g., "By [Name] — Last updated [Date]")
5. Add Person schema for authors
6. Add sameAs links to Organization schema (TripAdvisor destination page, Wikidata Q-id)

### Priority 3 — AI Optimization (This Month)
7. Create `/llms.txt` and `/llms-full.txt` for AI crawler discovery
8. Add an inline "Sources" or "References" section at the bottom of the homepage
9. Consider adding review/testimonial schema with curated visitor feedback

---

*Analysis generated by Codex SEO Content Analysis — 2026-08-05*
