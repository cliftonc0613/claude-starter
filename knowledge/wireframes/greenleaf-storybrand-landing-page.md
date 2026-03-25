# GreenLeaf Lawn Care - StoryBrand Landing Page

## Overview

A high-converting local business landing page built on Donald Miller's StoryBrand framework. The page positions the **customer as the hero** and the business as the **guide** who helps them achieve a beautiful lawn and reclaim their weekends. Every section maps to one of the 7 StoryBrand elements.

---

## Design System

### Color Palette (Nature Green + Urgency Orange)

| Role | Hex | Tailwind | Usage |
|------|-----|----------|-------|
| **Primary** | `#059669` | `emerald-600` | Headers, nav active states, trust indicators |
| **Secondary** | `#10B981` | `emerald-500` | Hover states, icons, secondary elements |
| **CTA** | `#F97316` | `orange-500` | All "Get My Free Quote" buttons, urgency accents |
| **Background** | `#ECFDF5` | `emerald-50` | Alternating section backgrounds |
| **Text** | `#064E3B` | `emerald-900` | Body text, headings |
| **Text Muted** | `#475569` | `slate-600` | Subheadings, descriptions |
| **White** | `#FFFFFF` | `white` | Card backgrounds, main sections |
| **Dark** | `#0F172A` | `slate-900` | Footer background |
| **Star Gold** | `#FBBF24` | `amber-400` | Star ratings |
| **Error/Failure** | `#DC2626` | `red-600` | Failure section accent border |

### Typography

| Role | Font | Weight | Size (Desktop) | Size (Mobile) |
|------|------|--------|-----------------|---------------|
| **H1 (Hero)** | Outfit | 700 (Bold) | 56px / 3.5rem | 36px / 2.25rem |
| **H2 (Section)** | Outfit | 600 (SemiBold) | 40px / 2.5rem | 28px / 1.75rem |
| **H3 (Card)** | Outfit | 600 (SemiBold) | 24px / 1.5rem | 20px / 1.25rem |
| **Body** | Work Sans | 400 (Regular) | 18px / 1.125rem | 16px / 1rem |
| **Body Small** | Work Sans | 400 (Regular) | 16px / 1rem | 14px / 0.875rem |
| **CTA Button** | Outfit | 600 (SemiBold) | 18px / 1.125rem | 16px / 1rem |
| **Nav Links** | Work Sans | 500 (Medium) | 16px / 1rem | 14px / 0.875rem |

**Google Fonts Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Work+Sans:wght@300;400;500;600;700&display=swap');
```

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `section-y` | 80px (desktop) / 48px (mobile) | Vertical section padding |
| `container` | max-width: 1200px, px: 24px | Content container |
| `card-gap` | 24px | Gap between cards in grids |
| `card-padding` | 32px | Internal card padding |
| `stack-gap` | 16px | Vertical gap between stacked elements |

### Effects & Interactions

| Effect | Implementation | Duration |
|--------|----------------|----------|
| **Scroll reveal** | Elements fade-in + slide up on scroll | 600ms, ease-out |
| **CTA hover** | Scale 1.02 + shadow increase | 200ms |
| **Card hover** | Subtle shadow elevation + border color | 200ms |
| **Stat counter** | Number count-up animation on scroll | 1500ms |
| **Star rating** | Sequential star fill animation | 100ms per star |
| **Navbar scroll** | Transparent to solid white + shadow | 300ms |
| **Progress bar** | Scroll progress indicator at top | Real-time |

### Icons

Use **Lucide Icons** (SVG) throughout. No emojis in production.

| Wireframe Emoji | Production Icon | Lucide Name |
|-----------------|-----------------|-------------|
| 🌿 | Leaf SVG | `leaf` |
| 🌳 | Tree SVG | `trees` |
| 🍂 | Leaf off SVG | `leaf` (autumn variant) |
| 📋 | Clipboard SVG | `clipboard-list` |
| 📐 | Ruler SVG | `ruler` |
| 📞 | Phone SVG | `phone` |
| 📧 | Mail SVG | `mail` |
| 📍 | Map pin SVG | `map-pin` |
| 🔒 | Lock SVG | `lock` |
| ☰ | Menu SVG | `menu` |
| ✕ | X SVG | `x` |
| ★ | Star SVG | `star` (filled) |

---

## StoryBrand Section Breakdown

### Section 1: NAVBAR (Fixed)
**Height:** 72px | **Behavior:** Transparent on load, solid white + shadow on scroll

**Elements:**
- Logo (left): GreenLeaf wordmark + leaf icon
- Nav links (center): Services, How It Works, Reviews
- CTA (right): Phone number (click-to-call) + hamburger on mobile

**Design notes:**
- Phone number should be a tap-to-call link on mobile
- Hamburger triggers slide-out drawer (not dropdown)
- Active link gets `emerald-600` underline accent
- Z-index: 50 (above all content)

---

### Section 2: CHARACTER (Hero)
**StoryBrand element:** The customer is the hero
**Height:** 520px desktop / auto mobile | **Background:** Full-bleed image with dark overlay (50% opacity)

**Headline:** "You Deserve a Lawn That Makes the Neighbors Jealous"
- This positions the CUSTOMER as the hero, not the business
- Speaks to their desire (beautiful lawn + status)

**Subheadline:** "Stop spending your weekends mowing. We'll handle it so you can enjoy your yard instead of working in it."
- Addresses the internal frustration (wasted weekends)

**CTAs:**
- Primary: `[ Get My Free Quote ]` (orange-500, large, centered)
- Secondary: `( See Our Work )` (ghost/outline button)

**Social proof line:** Star rating + review count below CTAs

**Design notes:**
- Hero image: Professional photo of a lush, freshly mowed lawn
- Text overlay on left 60% of image (desktop) or centered (mobile)
- CTA button min-height 52px, min-width 220px
- Animate headline with staggered fade-in (title, subtitle, CTAs)

---

### Section 3: PROBLEM
**StoryBrand element:** The problem the customer faces (external, internal, philosophical)
**Background:** `emerald-50` | **Layout:** 3-column cards (desktop), stacked (mobile)

**Headline:** "Sound Familiar?"

**Three cards:**
1. **External Problem** - "Your lawn is overgrown, patchy and the HOA just sent another notice."
2. **Internal Problem** - "You feel embarrassed when neighbors pull into their perfect yards."
3. **Philosophical Problem** - "You shouldn't have to choose between a great lawn and your free time."

**Design notes:**
- Each card has a subtle Lucide icon at top (not emoji)
- Cards use white background with soft shadow
- Border-left accent in `emerald-500` for visual hierarchy
- Stagger reveal animation on scroll (200ms delay between cards)
- Copy should feel empathetic, not salesy

---

### Section 4: GUIDE (Empathy + Authority)
**StoryBrand element:** Position the business as the guide
**Layout:** 50/50 split (text left, image right on desktop), stacked on mobile

**Empathy headline:** "We Get It. Your Time Matters."
**Empathy copy:** "We've been in your shoes - that's why we started GreenLeaf 12 years ago."

**Authority stats (2x2 grid):**
- 2,400+ Lawns Served
- 12 Years in Business
- 4.9/5 Google Rating
- 100% Licensed & Insured

**Image:** Team photo (professional, friendly, on a job site)

**Design notes:**
- Stats use count-up animation when scrolled into view
- Each stat card has a soft `emerald-50` background
- Image should have rounded corners (12px)
- On mobile: image stacks above text, stats become 2x2 grid

---

### Section 5: PLAN (3-Step Process)
**StoryBrand element:** Give the customer a clear plan
**Background:** White | **Layout:** Stepper + 3-column cards

**Headline:** "Getting Started Is Easy"

**Steps:**
1. **Request a Quote** - "Fill out our quick form or call us. Takes under 2 minutes."
2. **We Assess & Schedule** - "We visit your property, give a fair price, and book your first service."
3. **Enjoy Your Perfect Lawn** - "Sit back and relax while we keep your yard looking its absolute best."

**Design notes:**
- Horizontal stepper connecting dots above the cards (desktop)
- Vertical stepper on mobile
- Step numbers in `emerald-600` circles
- Active step (step 1) filled, others outlined
- Cards have matching Lucide icons (clipboard-list, ruler, leaf)
- This section reduces anxiety - makes the process feel simple

---

### Section 6: CALL TO ACTION (Direct + Transitional)
**StoryBrand element:** Call to action
**Background:** `emerald-800` (dark green) | **Text:** White

**Headline:** "Your Dream Lawn Is One Call Away"

**Two CTAs:**
- **Direct CTA:** `[ Get My Free Quote ]` (orange-500, large)
- **Transitional CTA:** `( Download Lawn Care Guide )` (ghost/outline, white border)

**Design notes:**
- Full-width section, centered content
- Direct CTA is for buyers ready now
- Transitional CTA captures leads not ready to buy (email gate for PDF guide)
- Add subtle background pattern or gradient overlay
- This section should be visually bold and impossible to scroll past

---

### Section 7: SUCCESS (Transformation)
**StoryBrand element:** Show what success looks like
**Layout:** 3-column cards with before/after imagery

**Headline:** "Imagine Your Weekends Back"

**Three transformation stories:**
1. **Before** - No more weekend mowing, HOA complaints, equipment hassle
2. **After** - Lush green lawn, neighbors compliment, property value increases
3. **Enjoying** - Weekends free for family, pride in curb appeal

**Design notes:**
- Use actual before/after photos if available
- Cards should have image at top, bullet points below
- Checkmark icons in `emerald-500` for each benefit
- This section paints the picture of the transformation
- Consider a subtle parallax effect on the images

---

### Section 8: FAILURE (Stakes)
**StoryBrand element:** What happens if they don't act
**Background:** `gray-100` | **Accent:** Red left border (4px)

**Headline:** "Don't Let Another Season Pass You By"

**Copy:** "Every week you wait, your lawn falls further behind. Weeds spread. HOA fines stack up. Your home's curb appeal - and value - drops. Most customers wish they called us sooner."

**CTA:** `[ Get My Free Quote Today ]` (orange-500)

**Design notes:**
- This section should feel urgent but NOT fear-mongering
- Red left border creates visual tension
- Keep it concise - 2-3 sentences max
- Single CTA reinforces the action
- Slightly muted background separates this from success section

---

### Section 9: SOCIAL PROOF (Reviews)
**Layout:** Aggregate rating + stacked testimonial cards

**Aggregate:** Star rating + "4.9/5 from 320+ Google Reviews"

**Testimonials (3 minimum):**
- Include real names, neighborhoods, star ratings
- Stacked card layout (not carousel - better for conversion)

**Design notes:**
- Google review integration badge if available
- Testimonial cards: white bg, soft shadow, quotation mark accent
- Each card: star rating, quote text (italic), name + location
- Stagger reveal on scroll
- Link to Google reviews at bottom

---

### Section 10: CONTACT FORM (Final CTA)
**Background:** `emerald-800` | **Text:** White

**Headline:** "Claim Your Free Lawn Assessment"
**Subheadline:** "We'll respond within 24 hours. No obligation."

**Form fields:**
- Name (required)
- Phone (required)
- Email (required)
- Service (dropdown: Mowing, Landscaping, Cleanup, Sod Install, Other)
- Address (required)

**Submit:** `[ Get My Free Quote ]` (orange-500, full-width on mobile)
**Trust line:** Lock icon + "Your info is safe. We never spam."

**Design notes:**
- Form inputs: white background, rounded, 48px height
- Labels above inputs (not placeholders only - accessibility)
- Real-time validation with inline error messages
- Success state: Replace form with confirmation message + next steps
- On mobile: single column, full-width inputs

---

### Section 11: FOOTER
**Background:** `slate-900` | **Text:** White/gray

**4-column layout (desktop):**
1. Logo + tagline + contact info
2. Services list
3. Hours of operation
4. Social links

**Design notes:**
- Social icons use Lucide or Simple Icons SVGs
- Include schema.org LocalBusiness structured data
- Copyright + Privacy + Terms + Sitemap links
- On mobile: single column, stacked sections

---

## Mobile-Specific Design Notes

### Bottom Tab Bar (Sticky)
**Height:** 64px | **Background:** White + top shadow

| Icon | Label | Action |
|------|-------|--------|
| Home | Home | Scroll to top |
| Clipboard | Services | Scroll to services |
| Phone | Call | tel: link (opens dialer) |
| Star | Reviews | Scroll to reviews |
| Menu | More | Opens mobile menu |

### Mobile Adaptations
- All 3-column grids become single column stacks
- Hero headline reduces from 56px to 36px
- CTA buttons become full-width
- Form inputs stack vertically with labels above
- Stepper becomes vertical
- Navbar collapses to logo + hamburger
- Images reduce to 16:9 aspect ratio
- Section padding reduces from 80px to 48px

---

## CTA Placement Strategy

The primary CTA "Get My Free Quote" appears **4 times** on the page:

| Location | Context | Conversion Psychology |
|----------|---------|----------------------|
| Hero | First impression, high intent | Captures ready buyers immediately |
| Mid-page CTA bar | After seeing guide + plan | Captures after trust is established |
| Failure section | After urgency/stakes | Captures through fear of loss |
| Contact form | Final section | Captures with lowest friction (form right there) |

The transitional CTA "Download Lawn Care Guide" appears once (mid-page) to capture leads not ready to buy.

---

## Technical Implementation Notes

### Stack Recommendation
- **Framework:** Astro 5 or Next.js 14
- **Styling:** Tailwind CSS v4
- **Icons:** Lucide React / Astro
- **Animations:** CSS scroll-driven animations or Framer Motion
- **Forms:** React Hook Form + server action or Formspree
- **Hosting:** Cloudflare Pages or Vercel

### Performance Targets
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1
- Total page weight: < 500KB (excluding images)
- Images: WebP format, srcset for responsive, lazy load below fold

### SEO Requirements
- Schema.org `LocalBusiness` structured data
- Open Graph + Twitter Card meta tags
- Semantic HTML (header, main, section, footer, nav)
- Unique title + meta description
- Alt text on all images
- Internal linking to service pages

### Accessibility Requirements
- WCAG 2.1 AA compliance
- Color contrast ratio 4.5:1 minimum
- Focus rings on all interactive elements
- Skip-to-content link
- Form labels (not just placeholders)
- `prefers-reduced-motion` media query
- Keyboard navigable (tab order matches visual)
- Screen reader friendly (aria-labels on icon buttons)

---

## Desktop Wireframe

```
// === StoryBrand Local Business Landing Page @desktop (1100px) ===
// Framework: Character -> Problem -> Guide -> Plan -> CTA -> Success -> Failure

+--- browser: www.greenleaflawncare.com -------------------------------------------+
|                                                                                   |
|  // [NAVBAR] fixed, h:72px                                                        |
|  GREENLEAF        Services   How It Works   Reviews       (864) 555-0142    =     |
|                                                                                   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  // [1. CHARACTER -- Hero identifies the customer as the hero]                    |
|  // h:520px, background-image with overlay                                        |
|  +-------------------------------------------------------------------------------+|
|  |                                                                               ||
|  |         You Deserve a Lawn That Makes the                                     ||
|  |         Neighbors Jealous                                                     ||
|  |                                                                               ||
|  |         Stop spending your weekends mowing. We'll handle it                   ||
|  |         so you can enjoy your yard instead of working in it.                   ||
|  |                                                                               ||
|  |         [### Get My Free Quote ###]     ( See Our Work )                      ||
|  |                                                                               ||
|  |         *****  4.9 rating - 320+ reviews on Google                            ||
|  |                                                                               ||
|  +-------------------------------------------------------------------------------+|
|                                                                                   |
|  // [2. PROBLEM -- External, internal, philosophical]                             |
|  // p:64px, bg:emerald-50                                                         |
|                                                                                   |
|                     Sound Familiar?                                               |
|                                                                                   |
|  +-------------------+  +-------------------+  +-------------------+              |
|  |                   |  |                   |  |                   |              |
|  |  [ico] External   |  |  [ico] Internal   |  |  [ico] Philosoph  |              |
|  |                   |  |                   |  |                   |              |
|  |  Your lawn is     |  |  You feel         |  |  You shouldn't    |              |
|  |  overgrown,       |  |  embarrassed when |  |  have to choose   |              |
|  |  patchy and the   |  |  neighbors pull   |  |  between a great  |              |
|  |  HOA just sent    |  |  into their       |  |  lawn and your    |              |
|  |  another notice.  |  |  perfect yards.   |  |  free time.       |              |
|  |                   |  |                   |  |                   |              |
|  +-------------------+  +-------------------+  +-------------------+              |
|                                                                                   |
|  // [3. GUIDE -- Empathy + Authority]                                             |
|  // p:64px, flex-row 50/50                                                        |
|  +--------------------------------------+----------------------------------------+|
|  |                                      |                                        ||
|  |  We Get It. Your Time Matters.       |  +----------------------------------+  ||
|  |                                      |  |                                  |  ||
|  |  We've been in your shoes --         |  |        [ Team Photo ]            |  ||
|  |  that's why we started GreenLeaf     |  |        [ 400 x 350  ]            |  ||
|  |  12 years ago.                       |  |                                  |  ||
|  |                                      |  +----------------------------------+  ||
|  |  +----------+  +----------+          |                                        ||
|  |  |  2,400+  |  |  12 yrs  |          |                                        ||
|  |  |  Lawns   |  |  in Biz  |          |                                        ||
|  |  +----------+  +----------+          |                                        ||
|  |  +----------+  +----------+          |                                        ||
|  |  |  *****   |  |  100%    |          |                                        ||
|  |  |  4.9/5   |  |  Insured |          |                                        ||
|  |  +----------+  +----------+          |                                        ||
|  +--------------------------------------+----------------------------------------+|
|                                                                                   |
|  // [4. PLAN -- Simple 3-step process]                                            |
|  // p:64px, bg:white                                                              |
|                                                                                   |
|                    Getting Started Is Easy                                        |
|                                                                                   |
|        (o1)=================(2)=================(3)                               |
|                                                                                   |
|  +-------------------+  +-------------------+  +-------------------+              |
|  |                   |  |                   |  |                   |              |
|  |   [ico] Step 1    |  |   [ico] Step 2    |  |   [ico] Step 3    |              |
|  |                   |  |                   |  |                   |              |
|  |   Request a Quote |  |   We Assess &     |  |   Enjoy Your      |              |
|  |                   |  |   Schedule         |  |   Perfect Lawn    |              |
|  |   Fill out our    |  |                   |  |                   |              |
|  |   quick form or   |  |   We visit your   |  |   Sit back and    |              |
|  |   call us. Takes  |  |   property, give  |  |   relax while we  |              |
|  |   under 2 mins.   |  |   a fair price,   |  |   keep your yard  |              |
|  |                   |  |   and book you.   |  |   looking great.  |              |
|  +-------------------+  +-------------------+  +-------------------+              |
|                                                                                   |
|  // [5. CALL TO ACTION -- Direct + Transitional]                                  |
|  // p:48px, bg:emerald-800, text:white                                            |
|  +-------------------------------------------------------------------------------+|
|  |                                                                               ||
|  |                Your Dream Lawn Is One Call Away                                ||
|  |                                                                               ||
|  |       [### Get My Free Quote ###]         ( Download Lawn Care Guide )        ||
|  |       // direct CTA                       // transitional CTA                 ||
|  |                                                                               ||
|  +-------------------------------------------------------------------------------+|
|                                                                                   |
|  // [6. SUCCESS -- Paint the picture of transformation]                           |
|  // p:64px                                                                        |
|                                                                                   |
|                 Imagine Your Weekends Back                                        |
|                                                                                   |
|  +-------------------+  +-------------------+  +-------------------+              |
|  |  [ Before photo ] |  |  [ After photo ]  |  |  [ Enjoy photo ]  |              |
|  |                   |  |                   |  |                   |              |
|  |  v No more        |  |  v Lush, green    |  |  v Weekends free  |              |
|  |    weekend mowing |  |    carpet lawn    |  |    for family     |              |
|  |  v No more HOA    |  |  v Neighbors      |  |  v Pride in your  |              |
|  |    complaints     |  |    compliment you |  |    curb appeal    |              |
|  |  v No equipment   |  |  v Property value |  |                   |              |
|  |    hassle         |  |    increases      |  |                   |              |
|  +-------------------+  +-------------------+  +-------------------+              |
|                                                                                   |
|  // [7. FAILURE -- Stakes without fear-mongering]                                 |
|  // p:48px, bg:gray-100, border-left:4px red                                     |
|  +-------------------------------------------------------------------------------+|
|  |  |                                                                            ||
|  |  |  Don't Let Another Season Pass You By                                      ||
|  |  |                                                                            ||
|  |  |  Every week you wait, your lawn falls further behind. Weeds spread.        ||
|  |  |  HOA fines stack up. Your home's curb appeal -- and value -- drops.        ||
|  |  |  Most customers wish they called us sooner.                                ||
|  |  |                                                                            ||
|  |  |                  [### Get My Free Quote Today ###]                          ||
|  |  |                                                                            ||
|  +-------------------------------------------------------------------------------+|
|                                                                                   |
|  // [REVIEWS -- Social proof reinforcement]                                       |
|  // p:48px                                                                        |
|                                                                                   |
|         ***** 4.9/5 from 320+ Google Reviews                                     |
|                                                                                   |
|  +-------------------------------------------------------------------+            |
|  |  "I got my weekends back. Best decision I made this year."        |            |
|  |                                               -- Mike T., 29601   |            |
|  +-------------------------------------------------------------------+            |
|  +-------------------------------------------------------------------+            |
|  |  "They transformed our yard. We actually use it now!"             |            |
|  |                                       -- Sarah M., Simpsonville   |            |
|  +-------------------------------------------------------------------+            |
|  +-------------------------------------------------------------------+            |
|  |  "Professional, on time, and honest pricing. Can't ask more."     |            |
|  |                                            -- David K., Mauldin   |            |
|  +-------------------------------------------------------------------+            |
|                                                                                   |
|  // [CONTACT FORM -- Final CTA with form]                                         |
|  // p:48px, bg:emerald-800, text:white                                            |
|  +-------------------------------------------------------------------------------+|
|  |                                                                               ||
|  |              Claim Your Free Lawn Assessment                                  ||
|  |              We'll respond within 24 hours. No obligation.                    ||
|  |                                                                               ||
|  |   Name: [________________]        Phone: [________________]                   ||
|  |   Email: [________________]       Service: [  Select service   v]             ||
|  |   Address: [______________________________________________]                   ||
|  |                                                                               ||
|  |                       [### Get My Free Quote ###]                              ||
|  |                                                                               ||
|  |              [lock] Your info is safe. We never spam.                         ||
|  +-------------------------------------------------------------------------------+|
|                                                                                   |
|  // [FOOTER]                                                                      |
|  +-------------------------------------------------------------------------------+|
|  |  GREENLEAF Lawn Care     Services       Hours            Connect              ||
|  |  Family-owned since 2012 - Mowing        Mon-Fri 7a-6p   Facebook             ||
|  |  (864) 555-0142          - Landscaping   Sat 8a-2p       Instagram            ||
|  |  info@greenleaf.com      - Cleanup       Sun Closed      Google               ||
|  |  Greenville, SC 29601    - Sod Install                   Nextdoor             ||
|  |  -----------------------------------------------------------------            ||
|  |  (c) 2026 GreenLeaf Lawn Care LLC    Privacy    Terms    Sitemap              ||
|  +-------------------------------------------------------------------------------+|
+-----------------------------------------------------------------------------------+
```

## Mobile Wireframe

```
// === StoryBrand Local Business @mobile (375px) ===

.--------------------------------------.
|           [----notch----]            |
|  GREENLEAF                       =   |
|--------------------------------------|
|                                      |
|  // [1. CHARACTER]                   |
|  +----------------------------------+|
|  |                                  ||
|  |  You Deserve a Lawn              ||
|  |  That Makes the                  ||
|  |  Neighbors Jealous               ||
|  |                                  ||
|  |  Stop spending your              ||
|  |  weekends mowing.               ||
|  |                                  ||
|  |  [## Get My Free Quote ##]       ||
|  |                                  ||
|  |  ***** 4.9 - 320+ reviews       ||
|  +----------------------------------+|
|                                      |
|  // [2. PROBLEM]                     |
|  Sound Familiar?                     |
|                                      |
|  +----------------------------------+|
|  |  [ico] External                  ||
|  |  Your lawn is overgrown,         ||
|  |  patchy and the HOA just         ||
|  |  sent another notice.            ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  [ico] Internal                  ||
|  |  You feel embarrassed when       ||
|  |  neighbors pull into their       ||
|  |  perfect yards.                  ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  [ico] Philosophical             ||
|  |  You shouldn't have to           ||
|  |  choose between a great          ||
|  |  lawn and your free time.        ||
|  +----------------------------------+|
|                                      |
|  // [3. GUIDE]                       |
|  +----------------------------------+|
|  |       [ Team Photo ]             ||
|  +----------------------------------+|
|                                      |
|  We Get It. Your Time               |
|  Matters.                            |
|                                      |
|  +----------+  +----------+         |
|  |  2,400+  |  |  12 yrs  |         |
|  |  Lawns   |  |  in Biz  |         |
|  +----------+  +----------+         |
|  +----------+  +----------+         |
|  |  *****   |  |  100%    |         |
|  |  4.9/5   |  |  Insured |         |
|  +----------+  +----------+         |
|                                      |
|  // [4. PLAN]                        |
|  Getting Started Is Easy             |
|                                      |
|  (o1)===(2)===(3)                     |
|                                      |
|  +----------------------------------+|
|  |  [ico] Step 1                    ||
|  |  Request a Quote                 ||
|  |  Quick form or call.             ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  [ico] Step 2                    ||
|  |  We Assess & Schedule            ||
|  |  We visit and give fair price.   ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  [ico] Step 3                    ||
|  |  Enjoy Your Perfect Lawn         ||
|  |  Sit back while we handle it.    ||
|  +----------------------------------+|
|                                      |
|  // [5. CTA] bg:emerald-800         |
|  +----------------------------------+|
|  |  Your Dream Lawn Is              ||
|  |  One Call Away                   ||
|  |                                  ||
|  |  [## Get My Free Quote ##]       ||
|  |  ( Download Lawn Guide )         ||
|  +----------------------------------+|
|                                      |
|  // [6. SUCCESS]                     |
|  Imagine Your Weekends Back          |
|                                      |
|  +----------------------------------+|
|  |  [ Before photo ]               ||
|  |  v No more weekend mowing       ||
|  |  v No more HOA complaints       ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  [ After photo ]                ||
|  |  v Lush, green lawn             ||
|  |  v Neighbors compliment you     ||
|  +----------------------------------+|
|                                      |
|  // [7. FAILURE] border-left:red     |
|  +----------------------------------+|
|  | | Don't Let Another              ||
|  | | Season Pass You By             ||
|  | |                                ||
|  | | Every week you wait, your      ||
|  | | lawn falls further behind.     ||
|  | |                                ||
|  | | [## Get My Free Quote ##]      ||
|  +----------------------------------+|
|                                      |
|  // [REVIEWS]                        |
|  ***** 4.9/5 - 320+ reviews         |
|                                      |
|  +----------------------------------+|
|  |  "I got my weekends back."       ||
|  |        -- Mike T., 29601         ||
|  +----------------------------------+|
|  +----------------------------------+|
|  |  "They transformed our yard."    ||
|  |   -- Sarah M., Simpsonville      ||
|  +----------------------------------+|
|                                      |
|  // [FORM] bg:emerald-800            |
|  +----------------------------------+|
|  |  Claim Your Free                 ||
|  |  Lawn Assessment                 ||
|  |                                  ||
|  |  Name:                           ||
|  |  [____________________________]  ||
|  |  Phone:                          ||
|  |  [____________________________]  ||
|  |  Email:                          ||
|  |  [____________________________]  ||
|  |  Service:                        ||
|  |  [  Select service            v] ||
|  |  Address:                        ||
|  |  [____________________________]  ||
|  |                                  ||
|  |  [## Get My Free Quote ##]       ||
|  |                                  ||
|  |  [lock] We never spam.           ||
|  +----------------------------------+|
|                                      |
|  // [FOOTER]                         |
|  GREENLEAF Lawn Care                 |
|  (864) 555-0142                      |
|  info@greenleaf.com                  |
|  Greenville, SC 29601               |
|                                      |
|  (c) 2026 GreenLeaf LLC             |
|  Privacy - Terms - Sitemap           |
|                                      |
|--------------------------------------|
|  [home] [services] [call] [reviews]  |
'--------------------------------------'
```

---

## UI/UX Pro Max Design Prompt

Use this prompt when implementing the landing page with the frontend-design or ultimate-developer skill:

```
Build a StoryBrand local business landing page for "GreenLeaf Lawn Care" - a lawn care
service in Greenville, SC.

DESIGN SYSTEM:
- Style: Social Proof-Focused with scroll-triggered storytelling
- Colors: Primary #059669 (emerald-600), Secondary #10B981 (emerald-500),
  CTA #F97316 (orange-500), Background #ECFDF5 (emerald-50), Text #064E3B (emerald-900)
- Typography: Outfit (headings, 700/600 weight) + Work Sans (body, 400/500 weight)
- Icons: Lucide SVGs only (NO emojis)
- Stack: Astro 5 + Tailwind CSS v4

STORYBRAND SECTIONS (in order):
1. NAVBAR - Fixed, transparent-to-white on scroll, logo + links + phone CTA
2. CHARACTER (Hero) - Full-bleed image, "You Deserve a Lawn That Makes the Neighbors Jealous",
   primary + secondary CTA, star rating social proof
3. PROBLEM - 3 cards: external, internal, philosophical problems
4. GUIDE - 50/50 layout: empathy copy + authority stats (2400+ lawns, 12 years, 4.9 rating,
   100% insured) with team photo
5. PLAN - 3-step process with stepper: Request Quote -> We Assess -> Enjoy Your Lawn
6. CTA BAR - Dark green, direct CTA + transitional CTA (Download Lawn Care Guide)
7. SUCCESS - 3 transformation cards with before/after imagery and checkmark bullet points
8. FAILURE - Gray background, red left border accent, urgency copy, single CTA
9. REVIEWS - Aggregate rating + 3 stacked testimonial cards with names and locations
10. CONTACT FORM - Dark green, 5-field form, trust line with lock icon
11. FOOTER - 4-column: company info, services, hours, social links

EFFECTS:
- Scroll-triggered fade-in + slide-up reveals (600ms, stagger 200ms between elements)
- Stat counter count-up animation on scroll
- Navbar transparent -> solid white + shadow on scroll (300ms)
- CTA hover: scale 1.02 + shadow increase (200ms)
- prefers-reduced-motion: disable all animations

MOBILE:
- Sticky bottom tab bar: Home, Services, Call (tel: link), Reviews, More
- All grids collapse to single column
- Hero headline 36px, body 16px
- Full-width CTA buttons
- Vertical stepper
- Section padding 48px (vs 80px desktop)

PERFORMANCE:
- LCP < 2.5s, CLS < 0.1
- WebP images with srcset, lazy load below fold
- Schema.org LocalBusiness structured data

ACCESSIBILITY:
- WCAG 2.1 AA, 4.5:1 contrast ratio
- Focus rings, skip-to-content, keyboard navigable
- Form labels (not just placeholders), aria-labels on icon buttons

CTA STRATEGY:
- "Get My Free Quote" appears 4x: hero, mid-CTA, failure, form
- "Download Lawn Care Guide" transitional CTA appears 1x mid-page
- Phone number is click-to-call on mobile
```
