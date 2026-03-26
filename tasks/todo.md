# AI Pattern Killer - Style Guide Integration

## Plan

Integrate 38 rules from the AI Writing Style Guide into the existing ai-pattern-killer skill databases and documentation.

### What Changes

1. **banned_words.json** - Add ~150+ new words from rules 8, 15, 16, 20, 21, 33, 34, 35, 36, 37, 38. Deduplicate against existing entries. Assign to proper confidence tiers.

2. **banned_phrases.json** - Add ~80+ new phrases. Create 8 new categories:
   - `ai_self_reference` (rule 1)
   - `knowledge_cutoff` (rule 2)
   - `placeholder_text` (rule 4)
   - `data_jargon` (rule 6)
   - `vague_attribution` (rule 12)
   - `orchestra_metaphors` (rule 18)
   - `deep_noun_construction` (rule 22)
   - `artificial_range` (rule 30)
   - Expand existing categories with new entries from rules 3, 5, 7, 9, 14, 17, 19, 23, 24, 25, 26, 27, 29

3. **banned_structures.json** - Add 4 new structural patterns:
   - `emoji_in_headings` (rule 28)
   - `broken_citations` (rule 27)
   - `deep_noun_pattern` (rule 22)
   - `artificial_range_pattern` (rule 30)

4. **rewriting/strategies.md** - Add Strategy 8 (Jargon Replacement) with business/tech jargon alternatives from rule 8

5. **rewriting/examples.json** - Add 5+ new before/after examples for new categories

6. **SKILL.md** - Add "Core Principles" section (8 principles from the style guide) to guide all modes

7. **config.yaml** - No changes needed

### Approach

- Deduplicate everything against existing entries
- Preserve existing tier assignments (don't demote anything already classified)
- New words go to the tier matching their detection risk
- Keep all existing categories, only add new ones

## Checklist

- [ ] Update banned_words.json with new words from rules 8, 15, 16, 20, 21, 33-38
- [ ] Update banned_phrases.json with new phrases and categories from rules 1-7, 9, 12-14, 17-19, 22-27, 29-30
- [ ] Update banned_structures.json with new structural patterns from rules 22, 27, 28, 30
- [ ] Update rewriting/strategies.md with Strategy 8 (jargon replacement)
- [ ] Update rewriting/examples.json with new before/after pairs
- [ ] Update SKILL.md with core principles section
- [ ] Review for completeness against all 38 rules
