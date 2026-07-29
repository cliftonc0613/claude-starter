#!/usr/bin/env bash
#
# Claude Company OS Installer
# Installs all 7 departments of skills from the Company OS chart.
#
# Usage:
#   bash install-claude-company-os.sh                 # install everything
#   bash install-claude-company-os.sh --dry-run       # show commands, change nothing
#   bash install-claude-company-os.sh --only dev,design
#   bash install-claude-company-os.sh --skip dev
#
# Groups: work (small business + legal + finance), marketing, social, dev, design
#
# Requires: claude CLI, git. Node 22.12+ needed for Impeccable and Transitions.
#
# Note: Impeccable and Taste both install into the Designers group. They
# overlap on frontend design, so try both and drop whichever you don't use.

set -uo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ALL_GROUPS="work marketing social dev design"
SELECTED_GROUPS="$ALL_GROUPS"
DRY_RUN=0

SKILLS_DIR="${HOME}/.claude/skills"
TMP_DIR="$(mktemp -d)"

SUCCEEDED=()
FAILED=()
SKIPPED=()

# Anthropic example skills pulled from anthropics/skills (no marketplace needed)
ANTHROPIC_SKILLS=(
  "skill-creator"
  "mcp-builder"
  "web-artifacts-builder"
  "brand-guidelines"
)

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

if [ -t 1 ]; then
  BOLD=$'\033[1m'; DIM=$'\033[2m'; GREEN=$'\033[32m'
  YELLOW=$'\033[33m'; RED=$'\033[31m'; BLUE=$'\033[34m'; RESET=$'\033[0m'
else
  BOLD=""; DIM=""; GREEN=""; YELLOW=""; RED=""; BLUE=""; RESET=""
fi

header()  { printf "\n%s%s%s\n" "$BOLD$BLUE" "$1" "$RESET"; }
info()    { printf "  %s\n" "$1"; }
ok()      { printf "  %s%s%s\n" "$GREEN" "$1" "$RESET"; }
warn()    { printf "  %s%s%s\n" "$YELLOW" "$1" "$RESET"; }
err()     { printf "  %s%s%s\n" "$RED" "$1" "$RESET"; }
dim()     { printf "  %s%s%s\n" "$DIM" "$1" "$RESET"; }

cleanup() { rm -rf "$TMP_DIR"; }
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Arg parsing
# ---------------------------------------------------------------------------

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1; shift ;;
    --only)
      SELECTED_GROUPS="$(printf '%s' "${2:-}" | tr ',' ' ')"; shift 2 ;;
    --skip)
      SKIP_LIST="$(printf '%s' "${2:-}" | tr ',' ' ')"
      NEW=""
      for g in $ALL_GROUPS; do
        keep=1
        for s in $SKIP_LIST; do [ "$g" = "$s" ] && keep=0; done
        [ $keep -eq 1 ] && NEW="$NEW $g"
      done
      SELECTED_GROUPS="$NEW"; shift 2 ;;
    -h|--help)
      sed -n '2,18p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)
      err "Unknown option: $1"; exit 1 ;;
  esac
done

has_group() {
  for g in $SELECTED_GROUPS; do [ "$g" = "$1" ] && return 0; done
  return 1
}

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

run() {
  local label="$1"; shift
  if [ $DRY_RUN -eq 1 ]; then
    dim "would run: $*"
    return 0
  fi

  local step_start
  step_start=$(wc -l < "$TMP_DIR/install.log" 2>/dev/null || echo 0)

  if "$@" >>"$TMP_DIR/install.log" 2>&1; then
    ok "$label"
    SUCCEEDED+=("$label")
    return 0
  fi

  # Command exited nonzero. Check whether that's because it's already
  # installed, not a real failure, before reporting it as one.
  local step_output
  step_output=$(tail -n +"$((step_start + 1))" "$TMP_DIR/install.log" 2>/dev/null)

  if printf '%s' "$step_output" | grep -qiE \
    'already installed|already exists|already added|is already present'; then
    ok "$label (already installed, skipped)"
    SUCCEEDED+=("$label")
    return 0
  fi

  err "$label failed. See log below."
  FAILED+=("$label")
  return 1
}

add_marketplace() {
  local repo="$1"
  claude plugin marketplace add "$repo" >>"$TMP_DIR/install.log" 2>&1
  return 0   # already-added is not a real failure
}

install_plugin() {
  local label="$1" repo="$2" spec="$3"
  add_marketplace "$repo"
  run "$label" claude plugin install "$spec"
}

# ---------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------

header "Claude Company OS Installer"
[ $DRY_RUN -eq 1 ] && warn "DRY RUN. Nothing will be installed."
info "Groups: $(echo $SELECTED_GROUPS | tr ' ' ',')"

header "Checking prerequisites"

if ! command -v claude >/dev/null 2>&1; then
  err "claude CLI not found on PATH."
  err "Install Claude Code first, then re-run this script."
  exit 1
fi
ok "claude CLI found"

if ! command -v git >/dev/null 2>&1; then
  err "git not found on PATH. Required for the Anthropic example skills."
  exit 1
fi
ok "git found"

HAS_NPX=0
NODE_OK=0
if command -v npx >/dev/null 2>&1; then
  HAS_NPX=1
  ok "npx found"
  if command -v node >/dev/null 2>&1; then
    NODE_RAW="$(node --version 2>/dev/null)"
    NODE_MAJOR="$(printf '%s' "$NODE_RAW" | sed 's/^v//' | cut -d. -f1)"
    NODE_MINOR="$(printf '%s' "$NODE_RAW" | sed 's/^v//' | cut -d. -f2)"
    if [ "${NODE_MAJOR:-0}" -gt 22 ] 2>/dev/null; then
      NODE_OK=1
    elif [ "${NODE_MAJOR:-0}" -eq 22 ] && [ "${NODE_MINOR:-0}" -ge 12 ] 2>/dev/null; then
      NODE_OK=1
    fi
    if [ $NODE_OK -eq 1 ]; then
      ok "node $NODE_RAW"
    else
      warn "node $NODE_RAW found. Impeccable needs 22.12 or newer."
    fi
  else
    warn "node not found. Impeccable will be skipped."
  fi
else
  warn "npx not found. Impeccable, Taste, and Transitions will be skipped."
fi

mkdir -p "$SKILLS_DIR"

# ---------------------------------------------------------------------------
# 1. Small Business + Legal + Finance (Anthropic knowledge-work-plugins)
# ---------------------------------------------------------------------------

if has_group work; then
  header "Small Business, Legal, Finance"
  info "Source: anthropics/knowledge-work-plugins"
  add_marketplace "anthropics/knowledge-work-plugins"
  run "small-business plugin"  claude plugin install small-business@knowledge-work-plugins
  run "legal plugin"           claude plugin install legal@knowledge-work-plugins
  run "finance plugin"         claude plugin install finance@knowledge-work-plugins
else
  SKIPPED+=("work")
fi

# ---------------------------------------------------------------------------
# 2. Marketing (Corey Haines)
# ---------------------------------------------------------------------------

if has_group marketing; then
  header "Marketing"
  info "Source: coreyhaines31/marketingskills"
  install_plugin "marketing-skills" \
    "coreyhaines31/marketingskills" \
    "marketing-skills@marketingskills"
else
  SKIPPED+=("marketing")
fi

# ---------------------------------------------------------------------------
# 3. Social Media (Charlie Hills)
# ---------------------------------------------------------------------------

if has_group social; then
  header "Social Media"
  info "Source: charlie947/social-media-skills"
  install_plugin "social-media-skills" \
    "charlie947/social-media-skills" \
    "social-media-skills@social-media-skills"
  dim "Run voice-builder first. Every other social skill reads its output."
else
  SKIPPED+=("social")
fi

# ---------------------------------------------------------------------------
# 4. Developers
# ---------------------------------------------------------------------------

if has_group dev; then
  header "Developers"

  info "Superpowers (obra/superpowers-marketplace)"
  install_plugin "superpowers" \
    "obra/superpowers-marketplace" \
    "superpowers@superpowers-marketplace"

  info "Context7 (upstash/context7)"
  install_plugin "context7" \
    "upstash/context7" \
    "context7@context7-marketplace"

  info "Claude-Mem (thedotmack/claude-mem)"
  install_plugin "claude-mem" \
    "thedotmack/claude-mem" \
    "claude-mem@thedotmack"

  info "97-dev (DeevsDeevs/agent-system) scoped, single skill only"
  if [ $DRY_RUN -eq 1 ]; then
    dim "would run: curl -fsSL https://raw.githubusercontent.com/DeevsDeevs/agent-system/main/scripts/install.sh | bash -s -- --non-interactive --platform claude --skills 97-dev"
  else
    run "97-dev" bash -c \
      'curl -fsSL https://raw.githubusercontent.com/DeevsDeevs/agent-system/main/scripts/install.sh | bash -s -- --non-interactive --platform claude --skills 97-dev'
    dim "Scoped to 97-dev only. The Deevs marketplace also ships anti-ai-slop,"
    dim "golang-pro, polars-expertise, and persona workflow systems, not installed here."
  fi
else
  SKIPPED+=("dev")
fi

# ---------------------------------------------------------------------------
# 5. Designers
# ---------------------------------------------------------------------------

if has_group design; then
  header "Designers"

  info "UI UX Pro Max (nextlevelbuilder)"
  install_plugin "ui-ux-pro-max" \
    "nextlevelbuilder/ui-ux-pro-max-skill" \
    "ui-ux-pro-max@ui-ux-pro-max-skill"

  info "Impeccable (pbakaus/impeccable)"
  if [ $HAS_NPX -eq 1 ] && [ $NODE_OK -eq 1 ]; then
    run "impeccable" npx --yes impeccable install
    dim "Run /impeccable init inside Claude Code on first use."
  else
    warn "Skipped. Needs Node 22.12+. Then: npx impeccable install"
    SKIPPED+=("impeccable")
  fi

  if [ $HAS_NPX -eq 1 ]; then
    info "Taste (Leonxlnx/taste-skill)"
    run "taste-skill" npx --yes skills add Leonxlnx/taste-skill \
      --skill design-taste-frontend -a claude-code
  else
    warn "Skipping Taste. Install Node, then re-run with --only design."
  fi

  if [ $HAS_NPX -eq 1 ]; then
    info "Transitions (Jakubantalik/transitions.dev)"
    run "transitions.dev" npx --yes skills add Jakubantalik/transitions.dev \
      -a claude-code
  else
    warn "Skipping Transitions. Install Node, then re-run with --only design."
  fi

  dim "Impeccable and Taste both install. They overlap on the same job,"
  dim "polishing and steering frontend design, so Claude may reach for"
  dim "either one on a design request. Try both, then remove whichever"
  dim "you don't reach for. Neither uninstall damages your project files."
else
  SKIPPED+=("design")
fi

# ---------------------------------------------------------------------------
# 6. Anthropic example skills (direct copy, no marketplace)
# ---------------------------------------------------------------------------

if has_group dev || has_group design; then
  header "Anthropic example skills"
  info "Source: anthropics/skills"

  if [ $DRY_RUN -eq 1 ]; then
    dim "would clone anthropics/skills and copy: ${ANTHROPIC_SKILLS[*]}"
  else
    if git clone --depth 1 --quiet \
        https://github.com/anthropics/skills.git \
        "$TMP_DIR/anthropic-skills" >>"$TMP_DIR/install.log" 2>&1; then
      for skill in "${ANTHROPIC_SKILLS[@]}"; do
        SRC="$TMP_DIR/anthropic-skills/skills/$skill"
        if [ -d "$SRC" ]; then
          rm -rf "${SKILLS_DIR:?}/$skill"
          cp -R "$SRC" "$SKILLS_DIR/$skill"
          ok "$skill"
          SUCCEEDED+=("$skill")
        else
          err "$skill not found in repo. It may have been renamed."
          FAILED+=("$skill")
        fi
      done
    else
      err "Could not clone anthropics/skills."
      FAILED+=("anthropics/skills clone")
    fi
  fi
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

header "Summary"

if [ $DRY_RUN -eq 1 ]; then
  info "Dry run complete. Re-run without --dry-run to install."
  exit 0
fi

printf "  %sInstalled: %d%s\n" "$GREEN" "${#SUCCEEDED[@]}" "$RESET"
for s in "${SUCCEEDED[@]:-}"; do [ -n "$s" ] && dim "  $s"; done

if [ "${#FAILED[@]}" -gt 0 ]; then
  printf "\n  %sFailed: %d%s\n" "$RED" "${#FAILED[@]}" "$RESET"
  for f in "${FAILED[@]}"; do err "  $f"; done
  printf "\n"
  warn "Last 25 log lines:"
  tail -n 25 "$TMP_DIR/install.log" | sed 's/^/    /'
  printf "\n"
  info "Full log copied to: ${HOME}/claude-os-install.log"
  cp "$TMP_DIR/install.log" "${HOME}/claude-os-install.log" 2>/dev/null || true
fi

header "Next steps"
info "1. Restart Claude Code so the new plugins load."
info "2. Run /plugin to confirm everything shows up."
if has_group dev; then
  info "3. Claude-Mem needs its worker started. Run: npx claude-mem install"
fi
if has_group social; then
  info "4. Social skills need voice-builder run first, plus APIFY_API_TOKEN"
  info "   and GOOGLE_AI_API_KEY for post-scorer and reels-scripting."
fi
if has_group dev; then
  info "5. Context7 works anonymously. For higher limits, set CONTEXT7_API_KEY."
fi
if has_group design; then
  info "6. Run /impeccable init once per project. It reads your tokens and"
  info "   components instead of overwriting them, so run it from the repo root."
  info "7. Optional: npx impeccable detect src/ as a PR gate. Exits nonzero on findings."
  info "8. Optional: Impeccable Chrome extension runs the detector on any live page."
fi
printf "\n"

[ "${#FAILED[@]}" -gt 0 ] && exit 1
exit 0
