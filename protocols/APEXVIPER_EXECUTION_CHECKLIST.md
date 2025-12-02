# ✅ APEXVIPER EXECUTION CHECKLIST v1.0
**Operation Protocol:** MATRIX-FORGE  
**Purpose:** Pre-wager verification checklist for systematic execution  
**Owner:** Project Lead (Bam082608)

---

## OVERVIEW

This checklist MUST be completed before any bets are placed. No exceptions.

> **Cardinal Rule:** No wagers are placed until the slate file is complete and verified.

---

## STEP 1: BUILD THE FULL SLATE INTEL FILE

**Time Window:** Pre-market (before 2:00 PM ET)  
**Agent:** GEMINI "THE EYE"

### Checklist

- [ ] Create/update: `nhl/daily-intel/YYYY-MM-DD-slate.md`

For **each NHL game** you might touch:

- [ ] `## GAME: AWAY @ HOME (TIME)` block created
- [ ] `**Status:** ACTIVE` set
- [ ] `**DNA Link:** [[away-dna]] | [[home-dna]]` added
- [ ] `### TARGETS` section with:
  - [ ] Player/Market/Line/Price/Avg/Logic/Result `[PENDING]`
  - [ ] Tier tags assigned
  - [ ] Anchor tags where applicable

**Verification:** If a game/target is not in this file → **NO BET.**

---

## STEP 2: DESIGN THE MULTI-ANCHOR SET

**Time Window:** 2:00-4:00 PM ET  
**Agent:** APEX-MATRIX

### Checklist

- [ ] Identify **4-5 anchors** across the slate
  - Typically Tier 1, high-consistency, high-usage props
  - Example: high SOG studs, safe point props

- [ ] Mark each anchor with `[ANCHOR]` tag in `DAILY INTEL` file

### Anchor Sanity Check (each anchor must pass):

| Check | Anchor 1 | Anchor 2 | Anchor 3 | Anchor 4 | Anchor 5 |
|-------|----------|----------|----------|----------|----------|
| Aligns with team DNA? | [ ] | [ ] | [ ] | [ ] | [ ] |
| Price reflects value? | [ ] | [ ] | [ ] | [ ] | [ ] |
| No invalidating injury? | [ ] | [ ] | [ ] | [ ] | [ ] |
| Tier 1 classification? | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## STEP 3: CONSTRUCT MATRICES AND PARLAYS

**Time Window:** 4:00-5:30 PM ET  
**Agent:** APEX-MATRIX

### Single-Game Matrices (for each game):

- [ ] Build 1-3 **single-game matrices** per game:
  - [ ] Matrix A: One team's stars heavy
  - [ ] Matrix B: Other team's stars heavy
  - [ ] Matrix C (optional): Hybrid "both sides go off"

### Cross-Game Matrices:

- [ ] Build **cross-game parlays** using anchors:
  - [ ] Multiple small parlays using various anchor combinations
  - [ ] No oversized "everything rides on this" structure
  - [ ] Spread exposure across 4-5 different parlays minimum

### Double-Edged Design Verification:

For each key game, verify structure allows:
- [ ] Win if one read is right
- [ ] Win BIG if both reads are right (middle ground)
- [ ] Limited exposure if entirely wrong (small stakes)

---

## STEP 4: DEFINE STAKE DISTRIBUTION

**Time Window:** 5:30-5:45 PM ET  
**Agent:** LEDGER-KNIGHT

### Stake Limits

- [ ] Set **max risk per individual ticket**: $_____ (recommended: $1-3)
- [ ] Set **max total daily risk**: $_____ (recommended: 10% bankroll)
- [ ] Set **per-game exposure cap**: $_____ (recommended: $10-15 per game)
- [ ] Set **per-anchor exposure cap**: $_____ (recommended: $6-8 per anchor)

### Distribution Verification

- [ ] Confirm you are NOT recreating "core bet" exposure pattern:
  - [ ] No single parlay has >20% of daily exposure
  - [ ] Anchors distributed across multiple tickets
  - [ ] At least 10-15 total tickets planned

### Exposure Table (fill in before execution):

| Game | Max Exposure | Planned | Status |
|------|--------------|---------|--------|
| Game 1 | $_____ | $_____ | [ ] |
| Game 2 | $_____ | $_____ | [ ] |
| Game 3 | $_____ | $_____ | [ ] |
| Game 4 | $_____ | $_____ | [ ] |

| Anchor | Max Exposure | Planned | Status |
|--------|--------------|---------|--------|
| Anchor 1 | $_____ | $_____ | [ ] |
| Anchor 2 | $_____ | $_____ | [ ] |
| Anchor 3 | $_____ | $_____ | [ ] |
| Anchor 4 | $_____ | $_____ | [ ] |
| Anchor 5 | $_____ | $_____ | [ ] |

---

## STEP 5: FINAL PRE-GAME VERIFICATION

**Time Window:** 5:45-6:00 PM ET  
**Agent:** VIPER-ZERO

### Last-Minute Checks

- [ ] **Goalie Confirmation:** Verify starting goalies via DailyFaceoff.com
- [ ] **Late Scratch Check:** Review Twitter/beat writers for last-minute changes
- [ ] **Odds Movement:** Check for line movement >10% (re-evaluate if detected)
- [ ] **Anchor Validation:** All anchors still playing, no late scratches

### Go/No-Go Decision

| Item | Status | Action if Failed |
|------|--------|------------------|
| Slate file complete | [ ] | STOP - Complete file first |
| Anchors validated | [ ] | STOP - Remove invalid anchors |
| Exposure within caps | [ ] | STOP - Reduce positions |
| Goalies confirmed | [ ] | ADJUST - Re-evaluate affected games |
| No late scratches | [ ] | ADJUST - Remove affected legs |

**FINAL APPROVAL:** [ ] CLEARED FOR EXECUTION

---

## STEP 6: EXECUTE AND LOG

**Time Window:** 6:00-6:45 PM ET (Window 1) / 9:30-10:00 PM ET (Window 2)  
**Agent:** LEDGER-KNIGHT

### Execution Protocol

- [ ] Only after Steps 1-5 are complete:
  - [ ] Place bets in priority order (anchors first)
  - [ ] Screenshot/record all tickets

### Logging Requirements

Log each bet in `executions/YYYY-MM-DD-nhl-executions.md`:

- [ ] Book name
- [ ] Market type
- [ ] Line/Selection
- [ ] Price/Odds
- [ ] Stake amount
- [ ] Parlay composition (if applicable)
- [ ] Reference ID back to `DAILY INTEL` targets

### Log Entry Template:

```markdown
### Ticket #X

| Field | Value |
|-------|-------|
| **Book** | [Name] |
| **Type** | Single / SGP / Cross-Game |
| **Legs** | [List legs with IDs] |
| **Odds** | [Combined odds] |
| **Stake** | $X.XX |
| **Potential** | $X.XX |
| **Intel Refs** | DAL-1, OTT-3, TB-1 |
| **Status** | ⏳ PENDING |
```

---

## STEP 7: POST-GAME TRACKING

**Time Window:** After games complete  
**Agent:** LEDGER-KNIGHT

### Result Updates

- [ ] Update `Result:` fields in `DAILY INTEL` to `WIN` / `LOSS` / `PUSH`
- [ ] Record final stats for each target

### Summary Statistics

- [ ] Calculate ROI by:
  - [ ] Anchor vs non-anchor performance
  - [ ] Tier 1 vs Tier 2 vs Tier 3
  - [ ] Market type (SOG, Points, Period Props)
  - [ ] Single vs SGP vs Cross-Game

### Tracking File Updates

Update `tracking/bet-log.md`:
- [ ] Add all bets to Active/Completed section
- [ ] Update monthly summary
- [ ] Calculate running totals

---

## QUICK REFERENCE: EXECUTION TIMELINE

| Time (ET) | Phase | Agent | Action |
|-----------|-------|-------|--------|
| Before 2:00 PM | Intel Gathering | GEMINI | Build slate file |
| 2:00-4:00 PM | Anchor Design | APEX-MATRIX | Identify 4-5 anchors |
| 4:00-5:30 PM | Matrix Construction | APEX-MATRIX | Build single/cross-game matrices |
| 5:30-5:45 PM | Risk Review | LEDGER-KNIGHT | Set exposure caps |
| 5:45-6:00 PM | Final Verification | VIPER-ZERO | Go/No-Go decision |
| 6:00-6:45 PM | Execution Window 1 | ALL | Place priority bets |
| 9:30-10:00 PM | Execution Window 2 | ALL | Place remaining bets |
| Post-Game | Tracking | LEDGER-KNIGHT | Update results/ROI |

---

## EMERGENCY PROTOCOLS

### Anchor Scratch (After Bets Placed)
- [ ] Document affected tickets
- [ ] Calculate remaining exposure
- [ ] Consider live hedging if significant exposure

### Major Line Movement (>15%)
- [ ] Re-evaluate affected targets
- [ ] Document reason for movement
- [ ] Decide: proceed, reduce stake, or skip

### System Failure (File Issues)
- [ ] STOP all betting
- [ ] Restore from backup or recreate
- [ ] Resume only when system integrity verified

---

**Version:** 1.0  
**Created:** December 2, 2025  
**Owner:** Project Lead (Bam082608)  
*APEXVIPER System - No bet without the checklist* ✅
