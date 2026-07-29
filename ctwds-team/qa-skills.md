# QA Skills — Persona-Based Site Testing

Runs 5 parallel QA agents — each embodying a distinct visitor archetype — and synthesizes findings into a consolidated report.
Powered by the `/qa-personas` skill.

---

## How to Run

```
/qa-personas
```

Provide a live URL when prompted (or include it in the command). The skill will:
1. Fetch the homepage to identify business type, audience signals, and primary conversion goal
2. Generate 5 personas specific to the site (not generic templates)
3. Launch 5 parallel QA agents — each testing the site in character
4. Synthesize all findings into a prioritized report

---

## What Gets Tested (Per Persona)

| Area | What's Evaluated |
|------|-----------------|
| First impression | Does the hero immediately speak to this persona's needs? |
| Navigation | Can they find what they're looking for intuitively? |
| Content & copy | Does it address their specific concerns and pain points? |
| Trust signals | Reviews, credentials, proof — enough to convert this persona? |
| CTA clarity | Obvious next step? Appropriate ask for their journey stage? |
| Mobile experience | How it feels on a phone for this persona type |
| Forms / conversion | Contact, booking, or purchase flow quality |
| Load & performance | Anything slow, broken, or missing |
| Information gaps | What this persona needed to see that wasn't there |

---

## Persona Archetypes (Pick 5 Most Relevant Per Site)

| Archetype | Profile |
|-----------|---------|
| The Skeptical Researcher | Reads everything, distrusts claims, looks for proof |
| The Mobile Skimmer | On phone, impatient, scanning headlines only |
| The Ready Buyer | Already decided, just needs to find the CTA fast |
| The First-Time Visitor | No context, confused by jargon, needs hand-holding |
| The Comparison Shopper | Has 3 tabs open, comparing against competitors |
| The Returning Visitor | Came back, looking for something specific |
| The Referral Arrival | Sent by someone, slightly trusts the brand but needs confirmation |
| The Budget-Conscious | Scrutinizes pricing, looking for hidden costs |
| The Technical Evaluator | Wants specs, details, credentials, proof |
| The Local/Geo-Specific Visitor | Cares about location, service area, local trust signals |

> Always name personas to match the business context — e.g., for a flooring company: "The Homeowner Mid-Renovation", not just "The Researcher".

---

## Report Output

| Section | Contents |
|---------|----------|
| Executive Summary | Overall score (avg of 5), would-convert rate (X/5), top 3 strengths, top 3 critical issues |
| Critical Issues | All critical issues grouped by type, with which personas flagged each |
| Minor Issues | Same structure as above |
| Persona Breakdown | Score + would convert (Y/N) + key insight per persona |
| Patterns & Themes | Issues appearing across multiple personas; what consistently worked |
| Priority Fix List | Ranked, specific, actionable improvements — most impactful first |

---

## When to Use

| Trigger | Notes |
|---------|-------|
| New site launch | Run after `/post-launch` to catch UX gaps |
| New landing page live | Validate before driving paid traffic |
| Redesign or major update | Catch regressions from the user's perspective |
| Conversion rate drop | Identify friction points across persona types |
| Pre-campaign validation | Ensure landing pages convert before ad spend |
| Client deliverable | Add persona QA report to onboarding or monthly reporting |

---

## Integration with Agency Playbooks

| Playbook | Where QA Fits |
|----------|--------------|
| New Client Onboarding | Run after Day 3-4 technical baseline — before strategy |
| Paid Ads Launch | Pre-launch validation step alongside `/ads landing` |
| Site Update / Redesign | On-demand trigger after any major site change |
| Lead Gen Drops | Run alongside CRO Specialist when conversion drops |

---

## Notes

- Generates personas specific to the site — not generic archetypes applied blindly
- At least 2 personas should attempt the form/CTA if one exists
- Flags broken links, 404s, and console errors found during testing
- Works on any live URL — local business, SaaS, e-commerce, landing page
