# Social Skills Reference

Skills from `charlie947/social-media-skills`.

> **Note:** The installer names the plugin but not its internal skill list, beyond flagging that `voice-builder` must run first ("Every other social skill reads its output") and that `post-scorer` and `reels-scripting` need `APIFY_API_TOKEN` and `GOOGLE_AI_API_KEY`. Categories below are inferred from those installer notes and standard social-media skill coverage — verify exact command names after installing (`claude plugin install social-media-skills@social-media-skills`) and update this file to match.

---

## 1. Foundation
- `voice-builder` — Establishes brand voice profile that every other social skill reads from. **Must run first.**

## 2. Platform Content
- `instagram-content` — Caption, carousel, and Reels content for Instagram
- `tiktok-content` — Short-form video scripts and captions for TikTok
- `linkedin-content` — Thought leadership and professional posts for LinkedIn
- `x-content` — Thread and post drafting for X/Twitter
- `reels-scripting` — Short-form video scripting across Reels/Shorts/TikTok (needs `GOOGLE_AI_API_KEY`)

## 3. Analytics & Optimization
- `post-scorer` — Score post performance and predict engagement (needs `APIFY_API_TOKEN`, `GOOGLE_AI_API_KEY`)
- `engagement-analysis` — Analyze engagement patterns across platforms and time periods

## 4. Scheduling
- `content-calendar` — Plan and schedule posts across platforms

---

## Related Existing Tools

This repo already has adjacent social coverage worth cross-referencing instead of duplicating:
- `marketing-skills:social-content` — social post creation (Marketing team, Content Writer agent)
- `blog-repurpose` — converts blog posts into social formats (Blog team, Distribution Manager agent)
- `marketing-skills:ab-test-setup` — applicable to social post A/B testing
