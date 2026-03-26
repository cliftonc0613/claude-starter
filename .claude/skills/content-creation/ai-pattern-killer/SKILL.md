---
name: ai-pattern-killer
description: Self-learning AI pattern detection and elimination system. Detects, flags, rewrites, and learns to eliminate AI-detectable patterns from all generated content. Four modes - post-process, real-time, audit, and voice training.
---

# AI Pattern Killer

A self-updating skill that makes AI-generated content sound authentically human. It detects patterns that AI detection tools flag, rewrites them using proven strategies, and learns from your feedback to get smarter over time.

## Quick Start

When invoked via `/ai-pattern-killer`:
1. Read `config.yaml` for current settings
2. Ask which mode to use (or detect from arguments)
3. Execute the selected mode using the pattern databases and rewriting strategies

**Argument shortcuts:**
- No args → ask which mode
- `audit` → Mode 3 (score text)
- `train` → Mode 4 (voice training)
- `review` → Mode 1 (post-process last generated content)
- `on` → Enable real-time mode in config.yaml
- `off` → Disable real-time mode in config.yaml

---

## Mode 1: Post-Process

**Purpose:** Scan finished content, flag AI patterns, and offer rewrites.

### Workflow

1. **Accept input** — User provides text directly, or use the last generated content from the conversation
2. **Load databases** — Read all files from `patterns/` directory:
   - `banned_words.json` (check sensitivity level in config.yaml to determine which tiers to flag)
   - `banned_phrases.json` (all categories)
   - `banned_structures.json` (all patterns)
   - `exceptions.json` (skip anything listed here)
3. **Scan the text** — Walk through the content and identify:
   - Word-level matches (flag with confidence tier)
   - Phrase-level matches (flag with category)
   - Structural matches (flag with pattern name)
4. **Calculate AI Detectability Score** (0-100):
   - Each high_confidence word = 3 points
   - Each medium_confidence word = 2 points
   - Each context_dependent word = 1 point
   - Each banned phrase = 4 points
   - Each structural pattern = 5 points
   - Normalize to 0-100 based on text length (points per 100 words, capped at 100)
5. **Present findings** using the output format from config.yaml:
   - Show the score first
   - Group flags by category (word/phrase/structure)
   - For each flag, show: the flagged text, its confidence/category, and a suggested rewrite from `rewriting/strategies.md`
   - Read `rewriting/examples.json` for before→after examples that match the pattern type
6. **Interactive review** — For each flag, ask the user using AskUserQuestion:
   - Accept (use the suggested rewrite)
   - Reject (the original is fine)
   - Edit (provide their own alternative)
   - Skip (move to next)
7. **Apply changes** — Regenerate the clean text with all accepted/edited rewrites applied
8. **Log feedback** — Write all accept/reject/edit decisions to `feedback/feedback_log.json`
9. **Run learning engine** — Process feedback according to `learning/engine.md` rules
10. **Report** — Show the cleaned text and any database updates that occurred

### Presentation Format

```
## AI Detectability Score: 42/100 (Moderate)

### Word-Level Flags (7 found)
1. "**comprehensive**" [medium] → "full" or "complete"
2. "**leverage**" [medium] → "use" or "take advantage of"
3. "**delve**" [high] → "dig into" or "look at"
...

### Phrase-Level Flags (3 found)
1. "**It's worth noting that**" [filler_hedge] → Delete entirely
2. "**In today's rapidly evolving**" [ai_transition] → Delete, start with your point
...

### Structural Flags (2 found)
1. **uniform_sentence_length** — All sentences are 15-20 words. Mix in some 4-word and 35-word sentences.
2. **parallel_lists** — All three list items follow identical structure. Break the pattern.
```

---

## Mode 2: Real-Time

**Purpose:** Prevent AI patterns during content generation by injecting awareness into the prompt.

### How It Works

When `modes.real_time.enabled` is `true` in config.yaml, this mode activates automatically before any content generation in the listed skills.

### Injection Rules

When generating content, Claude MUST follow these constraints:

**Vocabulary:**
- Never use words from the `high_confidence` tier in `banned_words.json`
- Avoid words from `medium_confidence` unless the specific word is the most precise choice AND no simpler alternative exists
- Replace any banned word with alternatives from `rewriting/strategies.md` Strategy 1 table

**Phrasing:**
- Never use any phrase from `banned_phrases.json`
- When tempted to write a filler hedge, delete it
- When tempted to write an AI transition, start with the actual point instead

**Structure:**
- Vary sentence length intentionally: include at least one sentence under 5 words and one over 30 words per 200 words of content
- Never write three consecutive paragraphs of the same length (within 20% word count)
- Use at least one fragment or conjunction-starter ("And", "But", "Or") per 300 words
- Do not force items into groups of three
- Use contractions naturally
- Limit em dashes to one per paragraph maximum

**Voice (when voice_profile.json exists):**
- Match the sentence length distribution from the voice profile
- Prefer vocabulary from the user's top-100 word list
- Mirror the user's transition patterns and paragraph shapes

### Integration with Other Skills

Skills listed in `config.yaml → modes.real_time.inject_into_skills` should include this instruction block in their generation step:

"Before writing, read `.claude/skills/content-creation/ai-pattern-killer/patterns/` and `.claude/skills/content-creation/ai-pattern-killer/rewriting/strategies.md`. Apply all real-time constraints from the AI Pattern Killer skill."

---

## Mode 3: Audit

**Purpose:** Score any text for AI detectability without changing it.

### Workflow

1. **Accept input** — User provides text or a file path
2. **Load databases** — Same as Mode 1, step 2
3. **Scan** — Same as Mode 1, steps 3-4
4. **Generate report:**

```
# AI Detectability Audit

**Score: 67/100 (High — likely to be flagged)**

## Summary
- 12 word-level flags (4 high, 6 medium, 2 context)
- 5 phrase-level flags
- 3 structural flags
- Estimated perplexity impact: LOW (uniform vocabulary)
- Estimated burstiness impact: LOW (sentence length std dev: 2.3 words)

## Sentence Length Analysis
- Mean: 18.4 words
- Std Dev: 2.3 words (human avg: 8-12)
- Range: 14-23 words (human avg: 3-45)
- Verdict: Too uniform — needs more variation

## Top 5 Changes That Would Lower the Score
1. Remove 3 filler hedges (-12 points)
2. Vary sentence length (-10 points, estimated)
3. Replace 4 high-confidence words (-12 points)
4. Break parallel list structure (-5 points)
5. Add 2 fragments or conjunction-starters (-3 points)

## Detailed Flags
[Same format as Mode 1 presentation]
```

5. **No changes applied** — Audit is read-only
6. **Offer to switch to Mode 1** — "Want me to fix these? I can switch to post-process mode."

---

## Mode 4: Voice Training

**Purpose:** Learn the user's natural writing voice and use it as the positive target.

### Workflow

1. **Collect samples** — Ask the user to provide 3-10 samples of their natural writing:
   - Emails they've sent
   - Social media posts they've written
   - Blog articles in their voice
   - Slack messages, text messages, anything authentic
   - Minimum 3 samples, aim for 5+ for accuracy

2. **Analyze patterns** — For each sample, extract:
   - **Sentence length distribution**: mean, std dev, min, max
   - **Vocabulary frequency**: top 100 words ranked by usage
   - **Transition patterns**: how they connect ideas (conjunctions, fragments, new paragraphs)
   - **Paragraph shapes**: length distribution and structural variety
   - **Contraction usage**: frequency and which contractions they prefer
   - **Punctuation habits**: em dashes, semicolons, exclamation marks, ellipses
   - **Register**: how formal vs conversational on a 1-10 scale
   - **Unique markers**: any distinctive phrases, idioms, or speech patterns

3. **Generate voice profile** — Create `voice_profile.json` with the aggregated analysis

4. **Update exceptions** — Any patterns from banned lists that appear naturally in the user's writing get added to `exceptions.json` with the note "matches voice profile"

5. **Test the profile** — Generate a short paragraph using the voice profile constraints and ask the user: "Does this sound like you?"

6. **Iterate** — If the user says no, ask what's off and adjust the profile

### Voice Profile Format

```json
{
  "created": "2026-03-25",
  "sample_count": 5,
  "sentence_length": {
    "mean": 14.2,
    "std_dev": 9.8,
    "min": 2,
    "max": 47
  },
  "vocabulary": {
    "top_words": ["actually", "basically", "honestly", ...],
    "avoided_words": ["utilize", "comprehensive", ...],
    "preferred_contractions": ["don't", "it's", "we're", "that's"]
  },
  "structure": {
    "avg_paragraph_length": 3.4,
    "uses_fragments": true,
    "starts_with_conjunctions": true,
    "register": 4.5
  },
  "markers": {
    "signature_phrases": ["here's the thing", "long story short"],
    "punctuation_habits": ["frequent em dashes", "rare semicolons"],
    "notes": "Tends to use specific numbers and dates. Often references past projects by name."
  }
}
```

---

## Database Files Reference

All databases live in the skill directory and are the single source of truth:

| File | Purpose | Updated By |
|------|---------|------------|
| `patterns/banned_words.json` | Words flagged by tier | Learning engine |
| `patterns/banned_phrases.json` | Phrases flagged by category | Learning engine |
| `patterns/banned_structures.json` | Structural patterns | Learning engine |
| `patterns/exceptions.json` | User-approved patterns to skip | Learning engine + voice training |
| `feedback/feedback_log.json` | Raw feedback data | Post-process mode |
| `feedback/processing.md` | Rules for feedback→updates | Manual only |
| `rewriting/strategies.md` | Replacement techniques | Manual only |
| `rewriting/examples.json` | Before→after proof pairs | Learning engine |
| `learning/engine.md` | Auto-update rules | Manual only |
| `learning/changelog.json` | Audit trail of all updates | Learning engine |
| `config.yaml` | Sensitivity and mode settings | User |
| `voice_profile.json` | User's writing voice (created by Mode 4) | Voice training |

---

## Scoring Reference

### AI Detectability Score (0-100)

| Score | Rating | Meaning |
|-------|--------|---------|
| 0-15 | Clean | Unlikely to trigger any detector |
| 16-30 | Low | Minor flags, probably fine |
| 31-50 | Moderate | Some detectors may flag this |
| 51-70 | High | Most detectors will flag this |
| 71-100 | Critical | Almost certainly flagged as AI |

### Detection Mechanics (from research)
- **Perplexity**: How predictable the text is. Score above 85 = likely human. AI text has low perplexity because it always picks the statistically most likely next word.
- **Burstiness**: Variation in sentence length and complexity. High burstiness = likely human. AI text is "eerily regular" — humans naturally spike between simple and complex.
- **Pattern density**: How many known AI markers appear per 100 words.

### Claude-Specific Notes
Claude (23% detection rate) is harder to detect than ChatGPT (68%) because:
- Broader vocabulary — rarely uses "delve," "robust," "leverage"
- Better sentence length variation (5-40 words vs ChatGPT's 15-25)
- Fewer formulaic transitions

But Claude's tell is being "almost too consistently good" — overly measured, thoughtful, and polished. Real humans are messier. The structural patterns (uniform paragraphs, perfect grammar, hedging) are Claude's main vulnerability, not vocabulary.

---

## Core Principles

These 8 principles govern all modes. Every scan, rewrite, and generation should enforce them:

1. **Be direct** — No meta-commentary. Don't say "it's important to note" — just note it.
2. **Be specific** — Concrete examples over buzzwords. Numbers over adjectives.
3. **Be varied** — Diverse sentence structures and vocabulary. Never three paragraphs in a row with the same shape.
4. **Be conversational** — Natural tone, not presentational. Write like you'd explain it to a colleague.
5. **Be simple** — Plain language over flowery prose. "Use" not "utilize."
6. **Be authentic** — Skip motivational language and jargon. No "empowering" or "unlocking potential."
7. **Be evidence-based** — Show, don't tell. Cite real sources or drop the claim.
8. **Be natural** — Avoid formulaic patterns. If it sounds like a template, rewrite it.

These principles are the tie-breaker. When a rewrite could go multiple directions, pick the one that best follows these 8 rules.

---

## Integration Hooks

To add post-processing to an existing skill, add this to the skill's delivery step:

```
Before presenting final content to the user, check if `.claude/skills/content-creation/ai-pattern-killer/` exists. If it does, run the content through AI Pattern Killer Mode 1 (post-process) and present the cleaned version.
```

To enable real-time mode for a skill, add its name to `config.yaml → modes.real_time.inject_into_skills`.
