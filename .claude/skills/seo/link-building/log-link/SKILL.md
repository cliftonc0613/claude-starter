---
name: log-link
description: Log a completed backlink or citation placement to the monthly tracking file. Use when a directory submission goes live, a backlink is placed, or a citation is confirmed. Appends a row to knowledge/tracking/YYYY-MM/YYYY-MM-links.md and creates the file if it doesn't exist.
disable-model-invocation: true
---

# Log Link

Record a backlink or citation placement in the monthly tracking log.

## What You Need From the User

Ask for any information not provided:
1. **Type** — `backlink` or `citation`
2. **Site** — name of the site (e.g. Manta, Yelp, Medium)
3. **URL** — the direct URL to the listing or post
4. **Anchor Text** — the link text (for citations: business name; for backlinks: descriptive anchor)
5. **Status** — `submitted`, `live`, or `indexed` (default: `submitted`)
6. **Date** — defaults to today (2026-05-28 format)

## Steps

1. Determine the current month file path: `knowledge/tracking/YYYY-MM/YYYY-MM-links.md` (create the `YYYY-MM/` folder if it doesn't exist)
2. If the file does not exist, create it with this header:
   ```
   # Key Kings Locksmith — Link & Citation Log: YYYY-MM
   
   **Monthly Target:** 10 backlinks + 10 citations  
   **Last Updated:** [today's date]
   
   | Date | Type | Site | URL | Anchor Text | Status |
   |------|------|------|-----|-------------|--------|
   ```
3. If the file exists, read it to check current counts and update **Last Updated**.
4. Append the new row in this format:
   ```
   | 2026-05-28 | citation | Manta | https://manta.com/c/example | Key Kings Locksmith | submitted |
   ```
5. After appending, count current backlinks and citations and report:
   - "Backlinks this month: X / 10"
   - "Citations this month: X / 10"
   - Whether either target is now met

## Rules

- NAP on every citation row must match exactly:
  - Name: **Key Kings Locksmith**
  - Address: **4105 Liberty Highway Unit B, Anderson, SC 29621**
  - Phone: **(864) 900-9597**
- Never overwrite existing rows — append only
- Keep the Status column updated as placements progress from submitted → live → indexed
