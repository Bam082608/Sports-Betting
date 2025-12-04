# 🐍 APEXVIPER - GAME ANALYSIS PROTOCOL v2.0 (TEST VERSION)

**Version:** 2.0-TEST  
**Status:** TESTING  
**Classification:** CORE ANALYSIS PROTOCOL  
**Effective Date:** 2025-12-03  
**Author:** Project Lead Bam082608  
**Note:** This is a TEST version. v1.0 remains as reference. Will be upgraded to v2.0 FINAL after validation.

**Dependencies:**  
- [APEXVIPER_NARRATIVE_BETTING_SYSTEM_v3.1.0.md](./APEXVIPER_NARRATIVE_BETTING_SYSTEM_v3.1.0.md)  
- [APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md](./APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md)

---

## PURPOSE

This protocol ensures **every game is analyzed the same way, every time**.

**Core Principle:**
> If data is missing, state "NOT PROVIDED."  
> If a field is required, it MUST be filled.  
> All numbers have defined meanings.

---

## CRITICAL RULES

1. **USE ONLY PROVIDED DATA** - No web search, no training data assumptions
2. **FOLLOW THE SEQUENCE** - Complete each phase in order
3. **NO EMPTY FIELDS** - If data missing, write "NOT PROVIDED"
4. **QUANTIFY EVERYTHING** - Use the defined rating scales
5. **FORCE NARRATIVE SELECTION** - Must classify before betting

---

## QUICK START TEMPLATE

**Copy this header for every game analysis:**

```markdown
# GAME ANALYSIS: [AWAY] @ [HOME]
**Date:** [YYYY-MM-DD]  
**Analyst:** [YOUR NAME / AI NAME]  
**Protocol Version:** 2.0-TEST  
**Analysis Start Time:** [HH:MM]  
**Data Sources:** [List all sources used]
```

---

## PHASE 1: DATA COLLECTION (5 minutes max)

### 1.1 MANDATORY DATA CHECKLIST

**Before proceeding, confirm you have:**

| Data Type | Source | Status | Timestamp |
|-----------|--------|--------|-----------|
| Home Team Season Stats | Yahoo/NHL.com | ☐ Have / ☐ Missing | |
| Away Team Season Stats | Yahoo/NHL.com | ☐ Have / ☐ Missing | |
| Home Team Last 5 Games | Yahoo/NHL.com | ☐ Have / ☐ Missing | |
| Away Team Last 5 Games | Yahoo/NHL.com | ☐ Have / ☐ Missing | |
| Home Goalie Confirmed | DailyFaceoff | ☐ Have / ☐ Missing | |
| Away Goalie Confirmed | DailyFaceoff | ☐ Have / ☐ Missing | |
| Current Betting Lines | FanDuel/DK | ☐ Have / ☐ Missing | |
| Injury Reports | Rotoworld/Team | ☐ Have / ☐ Missing | |

**STOP RULE:** If goalies are not confirmed, do NOT proceed to betting. Flag game as "MONITOR ONLY."

---

### 1.2 TEAM STATS TABLE (Season-to-Date)

**Fill in ALL fields. No blanks.**

| Stat | Home Team | Away Team | Edge (H/A/N) | Edge Rating (1-5) |
|------|-----------|-----------|--------------|-------------------|
| Record (W-L-OTL) | | | | |
| Goals Per Game | | | | |
| Goals Against Per Game | | | | |
| Power Play % | | | | |
| Penalty Kill % | | | | |
| Shots Per Game | | | | |
| Shots Against Per Game | | | | |
| Save % (Team) | | | | |
| Home/Road Record | | | | |
| Last 10 Games | | | | |

**Edge Rating Scale:**
- **5** = Dominant advantage (>15% better)
- **4** = Clear advantage (10-15% better)
- **3** = Slight advantage (5-10% better)
- **2** = Marginal advantage (2-5% better)
- **1** = Neutral (<2% difference)

**Total Edge Points:** [Sum all Edge Ratings]  
**Edge Leader:** [HOME / AWAY] by [X] points

---

### 1.3 RECENT FORM TABLE (Last 5 Games)

**HOME TEAM - Last 5 Games:**

| Date | Opponent | Result | GF | GA | SOG For | SOG Against | Notes |
|------|----------|--------|----|----|---------|-------------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

**HOME TEAM RECENT FORM SUMMARY:**
- Record Last 5: [W-L-OTL]
- GPG Last 5: [X.X]
- GAPG Last 5: [X.X]
- Goal Differential Last 5: [+/- X]
- Form Trend: ☐ HOT (3+ wins) / ☐ COLD (3+ losses) / ☐ MIXED

---

**AWAY TEAM - Last 5 Games:**

| Date | Opponent | Result | GF | GA | SOG For | SOG Against | Notes |
|------|----------|--------|----|----|---------|-------------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

**AWAY TEAM RECENT FORM SUMMARY:**
- Record Last 5: [W-L-OTL]
- GPG Last 5: [X.X]
- GAPG Last 5: [X.X]
- Goal Differential Last 5: [+/- X]
- Form Trend: ☐ HOT (3+ wins) / ☐ COLD (3+ losses) / ☐ MIXED

---

### 1.4 GOALIE COMPARISON

| Stat | Home Goalie | Away Goalie | Edge (H/A/N) |
|------|-------------|-------------|--------------|
| Name | | | |
| Season SV% | | | |
| Season GAA | | | |
| Last 3 Starts Record | | | |
| Last 3 Starts SV% | | | |
| Home/Road Split | | | |
| vs. This Opponent (if data) | | | |

**Goalie Situation Flags:**
- ☐ Home backup starting (FADE opportunity)
- ☐ Away backup starting (FADE opportunity)
- ☐ B2B situation for either goalie
- ☐ Coming off injury
- ☐ Hot streak (3+ good starts)
- ☐ Cold streak (3+ bad starts)

**GOALIE EDGE:** [HOME / AWAY / NEUTRAL]  
**GOALIE EDGE RATING:** [1-5]

---

### 1.5 SITUATIONAL FACTORS

| Factor | Home Team | Away Team | Impact |
|--------|-----------|-----------|--------|
| Days of Rest | | | |
| Back-to-Back? | ☐ Yes / ☐ No | ☐ Yes / ☐ No | |
| 3-in-4 nights? | ☐ Yes / ☐ No | ☐ Yes / ☐ No | |
| Travel Miles | N/A | | |
| Time Zone Change | N/A | | |
| Key Injuries | | | |

**FATIGUE EDGE:** [HOME / AWAY / NEUTRAL]  
**FATIGUE EDGE RATING:** [1-5]

---

### 1.6 BETTING LINES

| Market | Line | Home Odds | Away Odds | Notes |
|--------|------|-----------|-----------|-------|
| Moneyline | N/A | | | |
| Puck Line | ±1.5 | | | |
| Total | O/U | | | |
| Alt Total 1 | O/U | | | |
| Alt Total 2 | O/U | | | |

**Line Movement (if available):**
- Opened: [HOME odds] / [AWAY odds] / [TOTAL]
- Current: [HOME odds] / [AWAY odds] / [TOTAL]
- Movement: [HOME moved from X to Y] / [TOTAL moved from X to Y]

---

## PHASE 2: EDGE SYNTHESIS (3 minutes max)

### 2.1 EDGE SUMMARY TABLE

**Compile all edges into one view:**

| Edge Category | Winner | Rating (1-5) | Confidence |
|---------------|--------|--------------|------------|
| Season Stats Edge | | | ☐ High / ☐ Med / ☐ Low |
| Recent Form Edge | | | ☐ High / ☐ Med / ☐ Low |
| Goalie Edge | | | ☐ High / ☐ Med / ☐ Low |
| Fatigue Edge | | | ☐ High / ☐ Med / ☐ Low |
| Home Ice Edge | HOME | 2 | ☐ High / ☐ Med / ☐ Low |

**TOTAL EDGE SCORE:**  
- Home Team: [X] points  
- Away Team: [X] points  
- **Leader:** [HOME / AWAY] by [X] points

---

### 2.2 NARRATIVE CLASSIFICATION (MANDATORY)

**Based on ALL data above, this game is classified as:**

☐ **DEFENSIVE GRIND 🔒**  
*Indicators checked:*  
- ☐ Both teams averaging <2.5 GPG last 5  
- ☐ Strong goalies confirmed  
- ☐ Recent games trending under  
- ☐ Total posted ≤5.5

☐ **SKILL SHOW 🔥**  
*Indicators checked:*  
- ☐ Both teams averaging 3+ GPG last 5  
- ☐ Star players in form  
- ☐ Recent games trending over  
- ☐ Total posted ≥6.5

☐ **BLOWOUT CONTROL 💪**  
*Indicators checked:*  
- ☐ One team favored -200 or stronger  
- ☐ Major form disparity (hot vs cold)  
- ☐ Backup goalie for underdog  
- ☐ Clear talent gap

☐ **COMPETITIVE GRIND ⚔️**  
*Indicators checked:*  
- ☐ Favorite between -130 and -180  
- ☐ Similar recent form  
- ☐ Total between 5.5 and 6.5  
- ☐ Game likely decided by 1-2 goals

**SELECTED NARRATIVE:** [Write the name]  
**NARRATIVE CONFIDENCE:** [HIGH / MEDIUM / LOW]  
**NARRATIVE JUSTIFICATION:** [2-3 sentences explaining why]

---

## PHASE 3: BETTING THESIS (2 minutes max)

### 3.1 GAME PREDICTION

**Expected Outcome:**  
- Winner: [HOME / AWAY]  
- Margin: [1 goal / 2 goals / 3+ goals]  
- Total: [OVER / UNDER] [X.5]  
- Game Script: [1-2 sentences describing how the game plays out]

---

### 3.2 PRIMARY EDGE STATEMENT

**In one sentence, what is our edge?**  

> "[Write the single strongest reason to bet this game]"

**Edge Strength:** [1-10 scale]  
- **9-10:** Slam dunk, maximum confidence  
- **7-8:** Strong edge, confident bet  
- **5-6:** Moderate edge, standard bet  
- **3-4:** Weak edge, small bet or skip  
- **1-2:** No real edge, SKIP

---

### 3.3 RISK FACTORS

**What could make this analysis wrong?**

1. [Risk factor 1]  
2. [Risk factor 2]  
3. [Risk factor 3]

**Overall Risk Level:** ☐ LOW / ☐ MEDIUM / ☐ HIGH

---

## PHASE 4: BET CONSTRUCTION (Based on Narrative)

### 4.1 TIER STRUCTURE (From Protocol 3.1.0)

**For narrative: [SELECTED NARRATIVE]**

**TIER 1 - CORE (4-5 legs):**

| Leg # | Bet | Line | Odds | Rationale |
|-------|-----|------|------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 (opt) | | | | |

**Combined Parlay Odds:** [+XXX]  
**Stake:** $[X.XX]  
**Potential Win:** $[X.XX]

---

**TIER 2 - EXTENDED (5-6 legs):**

| Leg # | Bet | Line | Odds | Rationale |
|-------|-----|------|------|-----------|
| 1-4 | [Inherit Tier 1] | | | |
| 5 | | | | |
| 6 | | | | |

**Combined Parlay Odds:** [+XXX]  
**Stake:** $[X.XX]  
**Potential Win:** $[X.XX]

---

**TIER 3 - GOD TICKET (8-10 legs):**

| Leg # | Bet | Line | Odds | Rationale |
|-------|-----|------|------|-----------|
| 1-6 | [Inherit Tier 2] | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

**Combined Parlay Odds:** [+XXXX]  
**Stake:** $[X.XX]  
**Potential Win:** $[X.XX]

---

**TIER 4 - HEDGES (Standalone):**

| Bet | Odds | Stake | Purpose |
|-----|------|-------|---------|
| | | | Floor protection |
| | | | Variance reduction |

---

### 4.2 TOTAL PORTFOLIO

| Tier | Risk | Potential Win | Notes |
|------|------|---------------|-------|
| Tier 1 Core | $[X.XX] | $[X.XX] | |
| Tier 2 Extended | $[X.XX] | $[X.XX] | |
| Tier 3 God Ticket | $[X.XX] | $[X.XX] | |
| Tier 4 Hedges | $[X.XX] | $[X.XX] | |
| **TOTAL** | **$[X.XX]** | **$[X.XX]** | |

---

## PHASE 5: CONFIDENCE CALIBRATION

### 5.1 FINAL RATINGS

| Category | Rating (1-10) | Notes |
|----------|---------------|-------|
| Data Quality | | [Was all data available and current?] |
| Narrative Clarity | | [How clear was the game story?] |
| Edge Strength | | [How strong is our advantage?] |
| Bet Structure Confidence | | [Do the legs make sense together?] |

**OVERALL ANALYSIS SCORE:** [X/10] (average of above)

---

### 5.2 FINAL RECOMMENDATION

**Based on overall score:**

| Score Range | Recommendation | Action |
|-------------|----------------|--------|
| 8-10 | **STRONG BET** | Execute full Tier 1-3 structure |
| 6-7 | **STANDARD BET** | Execute Tier 1 + hedges |
| 4-5 | **SMALL BET** | Execute hedges only |
| 1-3 | **SKIP** | Do not bet this game |

**MY RECOMMENDATION:** [STRONG BET / STANDARD BET / SMALL BET / SKIP]

---

## PHASE 6: POST-GAME TRACKING (Complete After Game)

### 6.1 RESULTS

**Final Score:** [HOME X] - [AWAY X] ([REG / OT / SO])

**Narrative Accuracy:**
- Predicted Narrative: [NARRATIVE]
- Actual Game Type: [NARRATIVE]
- **Narrative Grade:** ☐ A (Perfect) / ☐ B (Close) / ☐ C (Off) / ☐ D (Wrong) / ☐ F (Opposite)

---

### 6.2 BET RESULTS

| Tier | Result | P/L | Notes |
|------|--------|-----|-------|
| Tier 1 Core | ☐ W / ☐ L | $[±X.XX] | |
| Tier 2 Extended | ☐ W / ☐ L | $[±X.XX] | |
| Tier 3 God Ticket | ☐ W / ☐ L | $[±X.XX] | |
| Tier 4 Hedges | ☐ W / ☐ L | $[±X.XX] | |
| **TOTAL** | | **$[±X.XX]** | |

---

### 6.3 LEG-BY-LEG ANALYSIS

| Leg | Bet | Result | Actual | Notes |
|-----|-----|--------|--------|-------|
| 1 | | ☐ HIT / ☐ MISS | | |
| 2 | | ☐ HIT / ☐ MISS | | |
| 3 | | ☐ HIT / ☐ MISS | | |
| 4 | | ☐ HIT / ☐ MISS | | |
| 5 | | ☐ HIT / ☐ MISS | | |

**Hit Rate:** [X/Y] = [XX%]

---

### 6.4 LESSONS LEARNED

**What Worked:**
-

**What Didn't Work:**
-

**Analysis Errors:**
-

**Protocol Adjustments Needed:**
-

---

## DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0-TEST | 2025-12-03 | Project Lead Bam082608 | Complete rewrite with quantified edges, forced narrative classification, confidence calibration. TEST VERSION for validation. |
| 1.0 | 2025-12-02 | Project Lead Bam082608 | Initial protocol (retained as reference) |

---

## CROSS-REFERENCE

This protocol integrates with:
- `protocols/APEXVIPER_NARRATIVE_BETTING_SYSTEM_v3.1.0.md` - Narrative framework
- `protocols/APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md` - Execution workflow
- `protocols/APEXVIPER_GAME_ANALYSIS_PROTOCOL.md` - Original v1.0 (reference)
- `nhl/team-dna/*.md` - Team profiles

---

## USAGE INSTRUCTIONS

### For Any AI (Gemini, Claude, Grok):

1. Receive this protocol + game data
2. Fill in ALL fields (no blanks allowed)
3. Force a narrative classification
4. Output the complete analysis
5. Hand to Project Lead for execution decision

### For Project Lead:

1. Review the completed analysis
2. Check the Overall Analysis Score
3. Follow the recommendation matrix
4. Execute using Protocol 3.2.0 if betting
5. Complete Phase 6 after game ends

---

## TEST VERSION NOTES

**This is v2.0-TEST. After validation:**
- If it works well → Upgrade to v2.0 FINAL
- If adjustments needed → Create v3.0 with improvements
- v1.0 remains as reference regardless

**Feedback to capture during testing:**
- Were any fields redundant?
- Were any fields missing?
- Did the flow make sense?
- Did it improve confidence in betting decisions?

---

*🐍 APEXVIPER - GAME ANALYSIS PROTOCOL v2.0-TEST*  
*"Same process. Every game. Every time."*