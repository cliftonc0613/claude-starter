# Learning Engine

## Purpose

Automatically evolves the pattern databases based on accumulated user feedback. Runs at the end of every post-process session.

## Execution Steps

1. Read feedback/feedback_log.json
2. Group entries by pattern_value
3. Count accepts, rejects, and edits per pattern
4. Check against thresholds in config.yaml
5. Apply any qualifying updates to pattern files
6. Write changes to changelog.json
7. Report what changed to the user

## Threshold Rules

### Promotion (pattern becomes stricter)

- **5+ net accepts** -> If in medium_confidence, move to high_confidence
- **10+ net accepts** -> If in context_dependent, move to medium_confidence
- **Pattern not in any list + 3 accepts** -> Add to medium_confidence

### Demotion (pattern becomes less strict)

- **3+ net rejections** -> Add to exceptions.json (stop flagging)
- **Pattern in high_confidence + 5 rejections** -> Move to medium_confidence
- **Pattern in medium_confidence + 3 rejections** -> Move to context_dependent

### Rewrite Learning

- **3+ edits with same user alternative** -> Add before/after to examples.json
- **5+ edits with different alternatives** -> Add all alternatives as options

## Safety Rails

- Never delete from banned lists — only move between tiers or to exceptions
- All changes require a changelog entry
- User can undo any automated change by editing the JSON directly
- Maximum 5 automated changes per session to prevent runaway updates
- Changes only apply to patterns with sufficient sample size (min 3 data points)

## Voice Profile Updates (Mode 4)

When voice training provides new samples:
- Extract sentence length distribution (mean, std dev, range)
- Extract vocabulary frequency (top 100 words by usage)
- Extract structural preferences (paragraph shapes, transition patterns)
- Save to voice_profile.json alongside exceptions.json
- Real-time mode uses voice_profile as positive targets during generation
