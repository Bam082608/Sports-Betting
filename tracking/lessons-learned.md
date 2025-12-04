# Lessons Learned — Tracking Log

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
