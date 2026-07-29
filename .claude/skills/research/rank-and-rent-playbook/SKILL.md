---
name: rank-and-rent-playbook
description: Researches a candidate local-service niche and city for a rank-and-rent (lead generation website rental) business, then produces a go/no-go playbook covering niche fit, tech stack, content plan, backlink plan, and a rental pricing pitch. Use this whenever Clifton names a service and a city and asks whether it's worth building a lead-gen site for it, or asks for a rank-and-rent / website landlord / local SEO rental playbook, business plan, or niche evaluation. Also trigger on phrases like "is towing in Greenville a good niche," "build me a lead gen playbook for," "should I rank and rent this," or any request to evaluate, compare, or plan a local lead-generation website business, even if the words "rank and rent" never come up.
---

# Rank-and-rent playbook builder

## What this is for

This skill runs the vetting process from two sources: Luke Van Der Veer's framework on The Koerner Office (see `koerner-office-luke-vander-lead-gen-rentals.md` if it's in the workspace) and Kyle the Website Landlord's interview on AI Rabbit Holes (see `OUTPUTS/research/kyle-website-landlord-rank-and-rent-interview.md`). The model: pick a local service niche and a city, build a website that ranks for it, then rent the leads to the actual business owner instead of running an agency. The skill's job is to do the research that decides whether a specific niche + city combo is worth building, and then hand back an execution playbook, not just a summary of the idea.

Don't skip straight to writing the playbook from general knowledge. The whole value of this skill is checking real competition data before committing content and money to a niche. If the research tools come back empty or fail, say so in the output rather than filling the gap with a guess dressed up as a finding.

One framing to carry through every playbook: this is an asset, not a business. Two to six months to rank and rent is a normal timeline, and a site that ends up paying $1,000 to $2,000 a month for years justifies that. In genuinely weak markets it can move much faster (the Des Moines septic test site hit page one in about a week), but never promise that pace in a playbook.

## Inputs to collect first

Ask if these aren't already in the request:

1. **Service/niche** - be specific. "Home services" is too broad; "radon mitigation" or "concrete driveway repair" is usable. If Clifton names a broad trade (plumbing, HVAC, roofing), check the niche-of-a-niche angle before writing it off: septic pumping instead of plumbing, gutter installation instead of roofing, popcorn ceiling removal instead of drywall. The sub-niche cuts competition, and the leads still sell to the broader trade (a plumber will happily buy septic leads).
2. **City** (and state/country if it's not obvious). If Clifton gives a niche with no city, or asks "where should I look," pick 2-3 candidate mid-size cities (see population guidance below) and run the fit check on each before recommending one.
3. Whether he wants one candidate fully vetted, or several candidates compared side by side (his live-demo style: try 2-3 niches in the same city and rank them).

Don't ask more than needed to get started. Everything else (tech stack, pricing model, content plan) follows a standard playbook and doesn't need extra input.

If comparing multiple candidates (several niches, several cities, or both), open the response with a one-line-per-candidate scoreboard before the full playbooks, so Clifton can see the calls at a glance:

```
Towing, Greenville SC   - Caution Build Rank/Rent ⚠️🟡
Towing, Mauldin SC      - Good Build Rank/Rent ✅🟢
```

Then write the full playbook for each candidate underneath, in the same order.

## Step 1: Niche and city fit check

This is the part that actually determines whether the rest of the playbook is worth writing. Run all of these before rendering a verdict:

**Population signal.** Web search the city's population. The sweet spot Luke found is roughly 60,000 to 400,000-500,000. Kyle works the same band and counts 800+ US cities above 50,000 as viable territory. Below that, search volume is usually too thin to support a rental business. Above it (major metros), competition is usually too entrenched for a new site to break in within a reasonable timeframe. Treat this as a guide, not a hard cutoff. A wealthy suburb of 40,000 can outperform a poor city of 300,000 for a high-ticket service, and a niched-down service can work in a bigger city than the broad trade could.

**Maps competition audit.** Call `mcp__dataforseo__business_data_business_listings_search` with the niche as a category (or `mcp__dataforseo__serp_organic_live_advanced` with the keyword `"<service> <city>"` and read the local pack in the results) to see who's currently ranking. Look for:
- Review counts under 10 on the top few listings (weak local SEO effort, easy target)
- Listings with no real website, or a Facebook/Instagram profile standing in for one
- Whether anyone already owns the exact-match name (e.g. a business literally named "[City] [Service]")
- How many genuinely competent-looking competitors are in the pack. A handful of well-reviewed, well-optimized businesses is a red flag, not a reason to try harder.

**Organic competition audit.** Pull the organic results from the same `serp_organic_live_advanced` call. For the top 5-10 results, check whether they're a dedicated site for that exact service, or an "inner page," a single subpage buried inside a broader multi-service company site. Inner pages are beatable: a purpose-built site with real depth on the topic will usually outrank a page that's one of twenty services crammed onto someone's homepage. Use `mcp__dataforseo__on_page_content_parsing` on the top 2-3 competitor URLs to check actual word count and page structure rather than guessing from the snippet.

**Aggregator signal.** While reading those organic results, flag any national aggregator or franchise directory page holding a top-three organic spot: Yelp, Angi, Thumbtack, HomeAdvisor, a Safelite-style national brand's city page. This is a green flag, not competition. Kyle's read, proven on his New Orleans auto glass site: Google shows aggregators when it has no local specialist to show, and it swaps in a purpose-built local site over an aggregator's city page fast. His site outranked both Safelite and Yelp and sits pinned above the map pack. Two or more aggregators on page one usually means the market is wide open.

Don't count a business as a competitor until its review count and primary service are confirmed. WebSearch or check each named result directly, then sort every confirmed competitor into one of three tiers: heavyweight (100+ reviews, or a recognized national franchise with a real dedicated local site, effectively unbeatable for local pack position on any reasonable timeline), independent specialist (roughly 10-50 reviews, a real but beatable operator), or generalist inner page (this service is a subpage on a broader multi-service site, treat as beatable regardless of the parent company's overall size or review count in its main category). Aggregator city pages don't get a tier at all; per the aggregator signal above, they count as evidence for building, not against. A field of five names on page one that turns out to be two heavyweights and three beatable operators is a different call than five heavyweights, don't collapse that distinction.

**Keyword validation.** Don't assume you know the phrase people actually search. Use `mcp__dataforseo__kw_data_google_trends_explore` to compare the two or three plausible phrasings of the service (Luke's example: "radon removal" vs. "radon mitigation," turned out only one of them had real search volume). Follow up with `mcp__dataforseo__dataforseo_labs_google_keyword_overview` on the winning phrase plus the city name to get actual monthly search volume. If volume is near zero everywhere, that's a kill signal regardless of how weak the competition looks. Keep the bar honest, though: the goal is 1 to 5% of daily demand for the service, not market domination. A site sitting at spot four or five in a mid-size market can still pull 50-80 calls a month, and one to three calls a day is enough to rent at $1,000 a month. Also remember that "best <service> <city>," "affordable <service> <city>," and "<service> near me" each produce different results pages; a strong incumbent on the head term doesn't own the variations.

**Owner-reachability check.** This one doesn't need a tool call, it's a judgment call based on the service type. Services where you can usually reach the actual owner by phone (towing, tree service, pest control, high-end landscaping/landscape design) rent more easily than services with a gatekeeper between you and the decision-maker (HVAC, plumbing, limo services, anything with a receptionist or national call center). Note this in the output so Clifton knows what the outreach conversation will actually look like.

**Structural red flags.** Before giving a green light, think through whether the leads you'd generate are actually high-intent and switchable, the way Luke had to learn the hard way. Two examples he ran into: elevator repair (owners are locked into long-term service contracts with steep early-termination fees, so better leads don't convert to switched customers) and luxury jet rental (too many broker/middleman layers between a lead and an actual sale). Apply the same logic to whatever niche is being evaluated: is there a real reason a warm lead wouldn't convert, even if the site ranks perfectly?

**Verdict.** Every playbook ends with exactly one of these three ratings, always in this exact wording so Clifton can scan a folder of playbooks and know the call at a glance without opening each one:

- `Good Build Rank/Rent ✅🟢` - real demand, a beatable competitive picture (thin reviews, no dedicated site, weak or missing GMB, aggregators holding top organic spots, and/or a strong-but-unclaimed local business), no structural red flags.
- `Caution Build Rank/Rent ⚠️🟡` - workable but with a real catch: population or search volume on the thin side, at least one strong dedicated-site competitor to out-build, a domain that costs real money, or a signal that's mixed rather than clean. Say exactly what the catch is and what would need to be true to upgrade it to a green. If the catch is competition on the broad trade, name the niche-of-a-niche pivot that would likely flip it (septic instead of plumbing) and offer to run the fit check on that instead.
- `Don't Build Rank/Rent 🛑🔴` - a genuine kill signal: near-zero search volume, multiple heavyweight-tier competitors (100+ reviews or a recognized national franchise) holding both local pack and organic position with no independent-specialist or generalist-inner-page gap left to build against, or a structural problem like elevator-repair-style contract lock-in that undermines lead conversion even with a #1 ranking.

Pick the rating from the evidence, don't soften a caution into a green or a red into a caution to be encouraging. State the two or three reasons that actually drove the call right after the rating, not a hedge. For a caution call, always name the specific thing that would tip it to green.

## Step 2: Tech stack recommendation

This part doesn't need live research unless Clifton asks for current pricing on something. Recommend, don't just list options:

- **Site build:** Claude Code + Astro + GitHub, deployed on Cloudflare Pages. This is the stack that put the Des Moines septic test site on page one in about a week, and it fits how Clifton already works: static output, near-perfect Core Web Vitals out of the box, free hosting, no plugin surface to maintain, no page builders. The real advantage is the saved skill file: once the first site's build context is captured as a skill, every following site stamps out in minutes instead of hours. Custom WordPress (custom PHP + ACF Pro, never a page builder) is the fallback only when a specific renter situation demands a WP admin they can log into.
- **Domain:** exact match if available (city + service, e.g. `WoodsideTowing.com`). If it's taken, add one word that keeps both the city and the service in the name (e.g. `WoodsideTowingPros.com`) rather than dropping either. This is maybe 5-10% of what makes the site succeed, worth getting right but not worth agonizing over.
- **Hosting:** Cloudflare Pages, free tier. If the WP fallback is in play, any low-cost managed WP plan at roughly $10-25/month per site.
- **Forms and lead capture:** GoHighLevel forms wired to a webhook rather than a generic form plugin. The webhook drops every submission straight into the GHL pipeline in real time, which keeps the lead flow out of an inbox nobody checks.
- **Call tracking:** GoHighLevel's call tracking and dynamic number insertion. Kyle runs CallRail for the same job and it's a fine standalone alternative, but running forms and calls through one platform gives Clifton a single dashboard to prove lead volume to a prospective renter, and once a site is rented, handing over or restricting GHL sub-account access is the same lever he already uses on WP client work. Whichever tool, the tracked number goes live the day the site does, because recorded calls are the sales pitch.
- **Rank tracking:** any standard rank tracker, checked during the ranking push only. Once a site is rented, call volume is the metric that matters (see Step 6), not position.
- **Billing:** Stripe with card-on-file autopay rather than manual invoicing. This keeps control with the site owner and avoids payment friction being an opening for a renter to stall or renegotiate.
- **Images:** AI-generated, localized. Generate a logo for the site's brand, then generate service photos that put that logo on the truck, the uniform, the equipment, with backdrops that look like the actual city. The Des Moines site did this across every image and it reads as a real local company. Nobody hiring a septic pump inspects photos for AI artifacts; they find the phone number and call.
- **Content drafting help:** an AI assistant (Claude included) to draft copy, always human-edited before it ships. Note this explicitly rather than assuming it's understood.

## Step 3: Content plan

Content is the biggest lever after niche/city selection, bigger than the domain name. One principle governs all of it, and it should be stated in the playbook: the words on the site are for Google's crawler, not the customer. A visitor reads one sentence and dials the number. The copy's job is to tell the algorithm, bluntly and repeatedly, what the business does and where it does it. "Windshield repair and replacement service in New Orleans, Louisiana" on the service page is not clumsy writing, it's the mechanism. And the target identity is narrow: not the expert on the service, the expert on the service in this city.

Build the plan from the competitor audit already done in Step 1:

1. List every sub-service and topic the top competitors in this niche and city (and in a more competitive city for the same niche, to see what a tougher market looks like) actually cover.
2. For each topic, note whether it clears roughly 500 monthly searches (via `dataforseo_labs_google_keyword_ideas` or `dataforseo_labs_google_keyword_overview`). Above that line, it earns its own dedicated page. Below it, fold it into a related page instead of giving it a standalone one.
3. Set a target word count per page that's meaningfully deeper than the strongest competitor page found in Step 1, not an arbitrary round number. If the best competitor page runs 400 words, target 1,000+ with real detail, not padding.
4. Structure the site with a clear page for every service (not one page with a bullet list of six services), plus home, about, and contact pages. A single bulleted list of services signals to Google (and to a reader) that the business doesn't actually specialize in any of them. Roughly 10 pages covers most markets; Kyle has one-page sites ranking #1 where competition is thin enough. Match the depth to the competition read, don't default to maximum.
5. **Location pages for adjacent suburbs.** One page per neighboring town the "business" would plausibly serve (the Metairie and Kenner pages on Kyle's New Orleans site are the template). Each one closes with a paragraph of real local geography: what the town borders, the lake it sits on, the canal that separates it from the core city. That paragraph does nothing for a customer and everything for local relevance. Pull the facts from real sources during research, don't let the draft invent them.
6. **Long-tail qualifier coverage.** AI search has people typing full sentences: a roofer who does Spanish tile, is affordable, licensed and insured. Work the qualifiers people actually add (affordable, licensed, insured, emergency, same-day, the material and sub-type names) into the service page copy naturally. Nobody can cover every variation and the playbook shouldn't try; cover the obvious ones and stop.
7. **One AI-surfacing blog post.** A "5 best [service] companies in [city]" listicle with the site's own brand included. The Des Moines site's version started showing up in AI search results within a month. One or two of these per site, not a blog treadmill.
8. For FAQ content, don't guess at questions. Draft a prompt for pulling real customer language from Reddit, Yelp, and social threads (e.g. "what are the common questions consumers ask about <service> in <city>, including from Yelp and Reddit"), and use the actual phrasing that comes back rather than generic filler questions.

Output this as a page list (topic, target word count, priority) plus 2-3 sentences on the overall content angle for this niche.

## Step 4: Backlink plan

Content tells Google what the site is; links tell Google it can trust the answer. In low-competition local SEO the bar is low. No CNN or Forbes links, no mass guest-post outreach. Google just needs to see that someone knows the site exists.

The core move is Kyle's copycat method. Pull the backlink profile of a ranking competitor in the same niche in a different city (a tree service in Houston when building tree service in Savannah) using `mcp__dataforseo__backlinks_backlinks` or `mcp__dataforseo__backlinks_referring_domains`, or Ahrefs/Majestic if he's in one of those. Scan the list for links that are free and easy to replicate: directory listings, citation sites, blog comments, local association pages. Skip anything that would require paying or pitching. List the 10-15 easiest targets in the playbook with the URL and link type for each.

Round it out with the standard citation set (Google Business Profile if the model allows for it, Bing Places, Yelp, the big data aggregators) and note that citations are maybe 5-10% of the outcome. If the DataForSEO backlink tools fail, name 5-10 likely targets from knowledge of the niche's typical directories and mark them as unverified.

## Step 5: Renting the leads

Give a specific recommendation, not a menu:

- **The pitch sequence.** Kyle's close, use it as the default: call the owner, say the site is already getting calls for their service in their city, and offer a free 7-day trial with the calls forwarded to them. No contract talk, no selling. After the week, call back and ask how many jobs they closed. If the trial worked, pitch the monthly number and take a card on file that day. The recorded calls in CallRail or GHL are the proof if they hesitate.
- **Pricing model, tiered by call volume.** Flat monthly fee ($1,000 to $2,000 depending on job value) when the site delivers roughly one to three calls a day. That volume makes the fee an easy yes and the arrangement fully passive. If the site ranks but volume is still thin (a few calls a week, like the early Des Moines site), don't force a flat fee; pitch per-lead pricing or a roughly 10% commission deal instead, and convert to flat fee once volume supports it. Revenue share at roughly 20% of gross (or net for niches with heavy material costs like landscaping or concrete) stays a later-stage option for an established relationship, and flag that it requires read access to the renter's CRM or books to verify closings, so it's not a first-conversation structure.
- **Trust verification.** The free trial does double duty here: watch how fast and how professionally the business answers the forwarded calls before charging them anything. A secret-shopper style test call is a legitimate way to check this before committing to a renter.

## Step 6: Running the portfolio

Keep this section short in the output, but include it. It sets expectations for what "done" looks like:

- **Watch call volume, not rankings.** Once a site is rented, the CallRail or GHL number is the only dashboard that matters. Kyle stopped checking rankings entirely; sites sitting at spot four or five still pay. Investigate only when calls drop off hard, which is rare. His five-year-old auto glass site hasn't been touched since it ranked, and he says that's true of about 98% of his portfolio.
- **Ignore Google core updates.** They target large affiliate and content sites, not a ten-page septic site in a mid-size market. Google makes almost nothing on ad space for these queries and has no reason to shake them up. A ranked local site riding out an update untouched is the norm, not luck.
- **Saturation isn't the risk.** The math Kyle uses: call it 1,000 rentable niches across 800+ cities over 50,000 population, times three or more rentable positions per results page, plus the query variations ("best," "affordable," "near me") that each rank differently. The constraint is Clifton's build time, not available markets. Which is the argument for the saved skill file in Step 2: the operators who win rinse and repeat one proven template instead of reinventing each build.
- **Tax note.** Once rental income becomes a meaningful tax event, buying an existing business (using the new income to offset it) is a strategy some rank-and-rent operators use, and lead-gen skills transfer directly to growing whatever gets bought. This is not tax or legal advice; say so explicitly and suggest he confirm specifics with his CPA before acting on it, consistent with how Lawyer Mode documents close out.

## Reference examples

Before writing a new playbook, read one file from `references/` that matches the verdict you're heading toward, or skim all three if unsure:

- `references/example-good-towing-mauldin-sc.md` - Good Build Rank/Rent. Shows how to write the pitch paragraph and verdict when the field is genuinely beatable.
- `references/example-caution-towing-berea-sc.md` - Caution Build Rank/Rent. Shows how to name the specific catch and the exact condition that would flip it to green, including a pivot recommendation to a different city.
- `references/example-stop-emergency-septic-tank-berea-sc.md` - Don't Build Rank/Rent. Shows how a kill call still gets a full research writeup (population, maps, organic, keyword, structural), just with the content/backlink/renting sections explicitly marked skipped instead of padded out with generic filler.

Match these on: evidence density (every claim traces to a named competitor, a real review count, an actual search volume figure, not vague characterizations), the "Sources" section citing the actual tool calls and queries run, and the way each section stays in prose rather than collapsing into bullet lists except where the format calls for a list. If a new playbook reads thinner than these on any of those fronts, the research wasn't done deeply enough yet.

## Output format

Render the final playbook as a single markdown document with this structure. Use sentence case headers, prose paragraphs (not bullet-heavy) except where a list is genuinely the clearest format, like the content page plan or the tool stack:

```
# [Service] in [City]: rank-and-rent playbook

**Researched:** [date]
**Verdict:** Good Build Rank/Rent ✅🟢 / Caution Build Rank/Rent ⚠️🟡 / Don't Build Rank/Rent 🛑🔴 (pick one)

## The pitch in one paragraph

## Niche & city fit assessment
(population signal, Maps competition findings, organic competition findings
including the aggregator signal, keyword validation with the 1-5% demand
framing, owner-reachability read, structural red flags, verdict rating
restated with the reasons that drove it)

## Tech stack to use

## Content plan
(page list with target word counts and priority, location pages, long-tail
qualifiers, the AI-surfacing listicle, plus the content angle)

## Backlink plan
(copycat targets pulled from a same-niche competitor in another city, plus
the citation set)

## Renting the leads
(free-trial pitch sequence, pricing tier matched to expected call volume,
trust verification steps)

## Running the portfolio

## Sources
(what was actually pulled: search queries run, tools used, URLs checked)
```

## Where to save it

Save the finished playbook under `OUTPUTS/[niche]/[niche]-[city]-[state]/playbook.md` (create both folders if needed), for example `OUTPUTS/towing/towing-mauldin-sc/playbook.md` or `OUTPUTS/radon-mitigation/radon-mitigation-greenville-sc/playbook.md`. The niche folder groups every city tested for that same service so Clifton can see a whole niche's results at a glance. Don't leave it in a scratch location, and don't reuse an old flat `OUTPUTS/[niche-city]/` path.

## If the research tools fail

`mcp__dataforseo__*` tools can fail on insufficient account credits (a 402 error) or auth issues. If that happens, don't silently skip the research step. Fall back to `WebSearch` and `mcp__workspace__web_fetch` (or the Firecrawl connector if connected) to manually check the Google results page, competitor sites, and Google Trends (trends.google.com) for the same signals. Note in the Sources section which method was actually used, so Clifton knows how much to trust the competition read.
