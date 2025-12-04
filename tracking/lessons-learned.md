# Lessons Learned — Tracking Log

## 2025-12-04 — ARSENAL v3.0 SYSTEM EVOLUTION

### THE BREAKTHROUGH: Never Combine Opposites

**DISCOVERY:**
Putting Over + Under on the same ticket creates a single point of failure. Even when players hit and spreads cover, one missed total kills the entire ticket.

**EVIDENCE - Dallas @ New Jersey (3-0 game):**

OLD STRUCTURE (v2.1):
- Ticket: Robertson 2+ SOG + Spread + Over 3.5 + Under 8.5
- Robertson: ✅ HIT
- Spread: ✅ HIT
- Over 3.5: ❌ MISSED (game was 3-0)
- Under 8.5: ✅ HIT
- Result: TOTAL LOSS (-$1.39) because Over killed it

NEW STRUCTURE (v3.0):
- Ticket A: Robertson 2+ SOG + Under 6.5
  - Robertson: ✅ HIT
  - Under 6.5: ✅ HIT
  - Result: WIN (+$1.25)
- Ticket B: Robertson 2+ SOG + Over 5.5
  - Robertson: ✅ HIT
  - Over 5.5: ❌ MISSED
  - Result: LOSS (-$1.00)
- NET: +$0.25 instead of -$1.39
- IMPROVEMENT: $1.64 swing

**LESSON:** Split conflicting props across separate tickets. Multiple win paths > single point of failure.

### ARSENAL v3.0 PRINCIPLES

**NEVER COMBINE ON SAME TICKET:**
- ❌ Over + Under
- ❌ Team A ML + Team B ML
- ❌ Player to score + team to lose
- ❌ Offensive props + defensive totals

**ALWAYS DO:**
- ✅ Split into separate tickets
- ✅ Over on Ticket A, Under on Ticket B
- ✅ Same player props as base, different totals
- ✅ Multiple win paths per game

### NEW DEPLOYMENT MODEL

**Per Game: 4-6 tickets, $5-6 total**

1. Single Best Prop ($1.50) - Foundation
2. 2-Leg Volume ($1.25) - Shooters only, no totals
3. 2-Leg Defensive ($1.00) - Shooter + Under
4. 2-Leg Offensive ($1.00) - Shooter + Over
5. 3-Leg Spread Safety ($1.00) - Spread + shooter + total (pick one)
6. God Mode ($0.25) - Lottery ticket, 1 per slate

**KEY CHANGE:** Reduced from 10-11 tickets to 4-6 tickets per game. More focused, less dilution.

### RUSH HOUR PROTOCOL

**NEW ADDITION:** Time-constrained betting safety protocol

**When to Use:**
- Driving (pulled over, at traffic light)
- Between meetings (<10 minutes)
- Mobile-only, no desktop
- Public/distracted environments
- Fatigued state

**Rules:**
- Max 2-3 tickets only
- Max $3.50-4.50 total (reduced from $6.00)
- Use Enhanced Fat Finger Protocol (Steps 1-9)
- Skip complex tickets (God Mode, 3+ legs, both Over/Under)
- If you don't have time to do it right, don't bet

---

## 2025-12-04 — APEXVIPER Intel Drop Summary
- Fat Finger Loss / Replacement accounting
  - Fat Finger Loss: -$17.00
  - Replacement Win: +$1.32
  - NET COST: -$15.68
- Action: Add a mandatory two-step confirmation for any stake > $5 or any manual re-bet following a corrective action.

## New Protocol Discovery — Anchor Variants (ADDED)
Anchor Variants define how totals and splits should be handled based on team intent profile.

- DEFENSIVE ANCHOR
  - Policy: Under ONLY (do not split).
  - Rationale: Teams with sustained defensive posture suppress scoring opportunities and skew conditional probabilities toward lower totals.

- OFFENSIVE ANCHOR
  - Policy: Over ONLY (do not split).
  - Rationale: High-volume offense and aggressive zone play increase variance on totals toward Over.

- MIDDLE ANCHOR
  - Policy: Split Over/Under (rare — only for true 50/50 matchups).
  - Rationale: Use only when model indicates ~50/50 probability and no clear trend in pregame metrics.

## Decision Tree Update — Totals
- IF clearly defensive → Bet Under only (standard stake: $1.50)
- IF clearly offensive → Bet Over only (standard stake: $1.50)
- IF truly balanced → Split (stake: $1.25 on each side)
- IF unsure → SKIP totals; focus on player props or SOG markets

## Operational Notes
- Apply Anchor Variant tag to team-dna files for automated decisioning.
- Add confirmation prompt to UI/workflow for any corrective re-bet to avoid fat-finger losses.
- Flag any pending settlements in bet-log until cleared; do not reconcile P/L until settlement final.

---

*Post-bet analysis and insights for continuous improvement*

---

## Purpose

After each betting session or significant bet, document:
1. What went right
2. What went wrong
3. What to do differently next time

---

## Lesson Template

### [Date] - [Event/Game]

**The Bet:**
- 

**Outcome:**
- 

**What I Learned:**
- 

**Action Item:**
- 

---

## Key Insights

### Patterns Identified
- 

### Mistakes to Avoid
- 

### Winning Tendencies
- 

---

## Rules Developed

*Based on lessons learned, add rules to your protocols*

1. 
2. 
3. 

---

## Review Schedule

- [ ] Weekly review of recent bets
- [ ] Monthly analysis of patterns
- [ ] Quarterly strategy assessment
