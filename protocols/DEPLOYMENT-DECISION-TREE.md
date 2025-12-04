# 🌳 DEPLOYMENT DECISION TREE

**Status:** ✅ PRODUCTION-READY  
**First Use:** December 3, 2025  
**Next Review:** After 10 games

---

## 🎯 PURPOSE

A systematic 7-phase pre-game workflow that eliminates analysis paralysis and ensures consistent deployment decisions. Transforms "Should I bet this game?" into a structured yes/no decision tree.

**Core Principle:** If a game fails ANY phase, skip it. No regrets, no second-guessing.

---

## 🌲 THE 7-PHASE DECISION TREE

```
                        START: New Game on Slate
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 1: GOALIE CONFIRMATION                                   │
│ ├─ Are starting goalies confirmed?                             │
│ ├─ YES → Proceed to Phase 2                                    │
│ └─ NO → ❌ SKIP GAME (check back in 2 hours)                   │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 2: TEAM DNA ALIGNMENT                                    │
│ ├─ Does matchup align with at least one team's DNA?            │
│ ├─ YES → Proceed to Phase 3                                    │
│ └─ NO → ❌ SKIP GAME (narrative unclear)                       │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 3: TIER 1 STAR AVAILABILITY                              │
│ ├─ Are there 2+ Tier 1 stars available to target?              │
│ ├─ YES → Proceed to Phase 4                                    │
│ └─ NO → ❌ SKIP GAME (insufficient quality targets)            │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 4: LINE VALUE ASSESSMENT                                 │
│ ├─ Are there 3+ props with +EV vs historical averages?         │
│ ├─ YES → Proceed to Phase 5                                    │
│ └─ NO → ❌ SKIP GAME (no betting edge identified)              │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 5: PORTFOLIO FIT                                         │
│ ├─ Does this game complement existing slate exposure?          │
│ ├─ Avoid correlation bombs (4+ games same narrative)           │
│ ├─ YES → Proceed to Phase 6                                    │
│ └─ NO → ❌ SKIP GAME (overexposure risk)                       │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 6: EXECUTION READINESS                                   │
│ ├─ Can you deploy RIGHT NOW within 10 minutes?                 │
│ ├─ Sportsbook open, bankroll ready?                            │
│ ├─ YES → Proceed to Phase 7                                    │
│ └─ NO → ❌ SKIP GAME (timing not aligned)                      │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────┐
│ PHASE 7: GUT CHECK                                             │
│ ├─ On a scale of 1-10, conviction level?                       │
│ ├─ 7+ → ✅ DEPLOY GAME                                         │
│ ├─ 5-6 → ⚠️ MINIMAL EXPOSURE ($5-10 max)                       │
│ └─ <5 → ❌ SKIP GAME                                           │
└────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                          ✅ GAME APPROVED FOR DEPLOYMENT
                    Proceed to Ticket Arsenal Selection
```

---

## 📋 PHASE-BY-PHASE BREAKDOWN

### PHASE 1: GOALIE CONFIRMATION

**Why It Matters:**
- Goalies drive 70%+ of game dynamics
- Unconfirmed goalies = unpredictable variance
- Not worth analyzing if starter unknown

**Decision Criteria:**
```
✅ PASS: Both starting goalies confirmed via:
   - Team official announcement
   - Reliable beat reporter
   - Lineup confirmation site (Daily Faceoff)

❌ FAIL: Either starter unconfirmed
   - Backup possibility
   - "Game-time decision" status
   - Conflicting reports

⚠️ CONDITIONAL: One starter confirmed, one likely
   - Reduce position size by 50%
   - Focus props on confirmed side only
```

**Tools:**
- [APEXVIPER_GOALIE_CONFIRMATION.md](./APEXVIPER_GOALIE_CONFIRMATION.md)
- [APEXVIPER_GOALIE_INTELLIGENCE.md](./APEXVIPER_GOALIE_INTELLIGENCE.md)

---

### PHASE 2: TEAM DNA ALIGNMENT

**Why It Matters:**
- DNA provides narrative foundation
- Misaligned games = random noise
- Need story to build coherent portfolio

**Decision Criteria:**
```
✅ PASS: Game aligns with clear DNA pattern:
   - Offensive explosion matchup (both teams high-event)
   - Defensive grind (both teams structured)
   - Mismatch (elite offense vs weak defense)
   - Home/Road split (home team DNA advantage)

❌ FAIL: DNA signals conflict or unclear:
   - Both teams "middling" in all categories
   - DNA suggests defensive game but totals are high
   - No clear narrative emerges from matchup

⚠️ CONDITIONAL: One team DNA strong, other neutral
   - Focus portfolio on strong-DNA team
   - Avoid cross-team parlays
```

**Key Questions:**
1. What does Team A's DNA say about this matchup?
2. What does Team B's DNA say about this matchup?
3. Do these narratives complement or conflict?
4. Can I articulate a 1-sentence game story?

**Tools:**
- `/nhl/team-dna/` profiles
- [APEXVIPER_GAME_ANALYSIS_PROTOCOL.md](./APEXVIPER_GAME_ANALYSIS_PROTOCOL.md)

---

### PHASE 3: TIER 1 STAR AVAILABILITY

**Why It Matters:**
- Tier 1 stars = foundation of portfolio
- Need 2+ quality anchors per game
- Volume without quality = losing strategy

**Decision Criteria:**
```
✅ PASS: 2+ Tier 1 players active and targeted:
   - MacKinnon, Pastrnak, Matthews level
   - High consistency (70%+ hit rate)
   - Props available at reasonable lines

❌ FAIL: <2 Tier 1 stars available:
   - Key injuries to top players
   - Stars' props not offered
   - Lines too juiced (>-150)

⚠️ CONDITIONAL: Exactly 2 Tier 1 stars
   - Build smaller portfolio (1-2 tickets max)
   - Supplement with high-confidence Tier 2
```

**Tier 1 Identification:**
- Check `/nhl/tier1-stars.md`
- Verify no late scratches (injury reports)
- Confirm props available on sportsbook

**Tools:**
- [tier1-stars.md](/nhl/tier1-stars.md)
- [APEXVIPER_NARRATIVE_BETTING_SYSTEM_v3.1.0.md](./APEXVIPER_NARRATIVE_BETTING_SYSTEM_v3.1.0.md)

---

### PHASE 4: LINE VALUE ASSESSMENT

**Why It Matters:**
- Edge = value vs market
- No value = no bet (fundamental rule)
- Need multiple +EV props to build portfolio

**Decision Criteria:**
```
✅ PASS: 3+ props with identified value:
   - Player avg 3.2 SOG, line at 2.5 (-120) ✅
   - Defenseman avg 0.6 PPG, line at 0.5 (+100) ✅
   - Team total avg 3.4, line at 2.5 (-110) ✅

❌ FAIL: Lines are efficient or against us:
   - Player avg 2.8 SOG, line at 3.5 (+100) ❌
   - All props require -150+ to get value ❌
   - Historical data suggests no edge ❌

⚠️ CONDITIONAL: 2 props with value
   - Build 1-2 ticket structure (limited)
   - No large parlays (insufficient options)
```

**Value Indicators:**
- Historical avg > line by 15%+
- Favorable matchup context (DNA support)
- Recent form trending toward over
- Reasonable juice (<-130)

**Tools:**
- Team DNA databases (usage rates, matchup history)
- Player averages from tracking files
- [APEXVIPER_LIVE_DATA_VERIFICATION.md](./APEXVIPER_LIVE_DATA_VERIFICATION.md)

---

### PHASE 5: PORTFOLIO FIT

**Why It Matters:**
- Diversification protects bankroll
- Correlation bombs = catastrophic risk
- Portfolio balance > individual game quality

**Decision Criteria:**
```
✅ PASS: Game adds diversity to slate exposure:
   - Different narrative than existing games
   - Different players (no overlap)
   - Geographic/time diversity
   - Balances existing risk

❌ FAIL: Game creates dangerous correlation:
   - 4th game with "home favorite" narrative
   - 5+ total games deployed (overextension)
   - Same players across multiple games
   - Doubles down on existing narrative

⚠️ CONDITIONAL: Some correlation but manageable
   - Reduce position size by 30-50%
   - Avoid cross-game parlays with correlated games
```

**Portfolio Questions:**
1. How many games am I already on tonight?
2. What narratives am I already exposed to?
3. Does this game balance or amplify existing risk?
4. What's my total $ exposure if this game added?

**Tools:**
- [APEXVIPER_PORTFOLIO_CONSTRUCTION.md](./APEXVIPER_PORTFOLIO_CONSTRUCTION.md)
- [APEXVIPER_PORTFOLIO_RULES.md](./APEXVIPER_PORTFOLIO_RULES.md)

---

### PHASE 6: EXECUTION READINESS

**Why It Matters:**
- Analysis without execution = wasted time
- ADHD execution gap is real
- Bet-as-you-analyze or don't analyze

**Decision Criteria:**
```
✅ PASS: Ready to deploy immediately:
   - Sportsbook app/site open
   - Bankroll confirmed and available
   - Next 10 minutes free to execute
   - Mental state: focused, not tilted

❌ FAIL: Cannot execute right now:
   - Sportsbook closed/maintenance
   - Out of funds until deposit clears
   - About to drive/eat/meeting
   - Emotional state: tilted, rushed, distracted

⚠️ CONDITIONAL: Can execute in 30-60 min
   - Save analysis notes
   - Set phone reminder
   - Risk: conviction may fade (protocol warning)
```

**Critical Rule from ADHD Protocol:**
> If you are not prepared to place bets RIGHT NOW, do not begin analysis.

**Tools:**
- [APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md](./APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md)

---

### PHASE 7: GUT CHECK

**Why It Matters:**
- Final psychological safeguard
- Conviction = kelly criterion signal
- Low conviction bets lose even when they win

**Decision Criteria:**
```
✅ PASS (Conviction 7-10):
   - Would defend this bet to a friend
   - Excited to deploy
   - Clear narrative in mind
   - No nagging doubts
   → FULL DEPLOYMENT

⚠️ CONDITIONAL (Conviction 5-6):
   - Feels "pretty good" but not great
   - Some uncertainty remains
   - Analysis checks out but gut hesitates
   → MINIMAL EXPOSURE ($5-10 total)
   → Use as "tracking bet" for learning

❌ FAIL (Conviction <5):
   - Forcing it because "slate is here"
   - Second-guessing the analysis
   - Would be embarrassed if it loses
   → SKIP GAME (no regrets)
```

**Gut Check Questions:**
1. On a scale of 1-10, how confident am I?
2. Am I betting this because I want to, or because I feel like I should?
3. If this loses, will I think "bad luck" or "what was I thinking?"

**Remember:** It's okay to skip games. Preservation > participation.

---

## 🎯 DECISION TREE EXAMPLES

### Example 1: CAR @ OTT (December 3, 2025)

```
PHASE 1: Goalie Confirmation
├─ CAR: Kochetkov confirmed ✅
├─ OTT: Forsberg confirmed ✅
└─ PASS → Proceed to Phase 2

PHASE 2: Team DNA Alignment
├─ CAR DNA: High-event offense, pushes tempo
├─ OTT DNA: Defense-first, low-event
├─ Narrative: CAR offense vs OTT defense clash
└─ PASS → Proceed to Phase 3

PHASE 3: Tier 1 Star Availability
├─ CAR: Aho, Svechnikov (both Tier 1)
├─ OTT: Tkachuk, Stutzle (both Tier 1+)
└─ PASS → Proceed to Phase 4

PHASE 4: Line Value Assessment
├─ Aho 3+ SOG (-125) → Avg 3.8 ✅
├─ Stutzle 1+ Point (-110) → Avg 0.75 PPG ✅
├─ CAR Team Total O2.5 (-115) → Avg 3.1 ✅
└─ PASS → Proceed to Phase 5

PHASE 5: Portfolio Fit
├─ Already deployed: BOS-DET (home fav)
├─ This game: Road favorite (CAR)
├─ Different narrative, different players
└─ PASS → Proceed to Phase 6

PHASE 6: Execution Readiness
├─ Time: 4:45 PM (game at 7 PM)
├─ Sportsbook: Open and ready
├─ Mental state: Focused
└─ PASS → Proceed to Phase 7

PHASE 7: Gut Check
├─ Conviction: 8/10
├─ Clear narrative: CAR powers through OTT structure
├─ Excited to deploy
└─ PASS → ✅ GAME APPROVED

RESULT: Deploy via Ticket Arsenal (Types 1-4)
```

---

### Example 2: NYI @ MTL (Hypothetical Skip)

```
PHASE 1: Goalie Confirmation
├─ NYI: Sorokin confirmed ✅
├─ MTL: Montembeault confirmed ✅
└─ PASS → Proceed to Phase 2

PHASE 2: Team DNA Alignment
├─ NYI DNA: Defensive, low-event, grind
├─ MTL DNA: Inconsistent, rebuilding, high-variance
├─ Narrative: Unclear - could be 5-4 or 2-1
└─ FAIL → ❌ SKIP GAME

RESULT: Game skipped at Phase 2
No need to proceed further
No regrets, saved time
```

---

### Example 3: COL @ NJD (Conditional Deploy)

```
PHASE 1-4: All PASS ✅
PHASE 5: Portfolio Fit
├─ Already deployed: 3 games
├─ All 3 games are "home favorite" narrative
├─ COL @ NJD is another "home favorite" (NJD)
└─ ⚠️ CONDITIONAL → Correlation warning

PHASE 6-7: PASS but adjusted

RESULT: Deploy with 50% reduced position size
Instead of $15 total → $7.50 total
Avoid cross-game parlays with other home favs
```

---

## 🔄 ITERATION & LEARNING

### After Each Game
Document the decision tree path in `/tracking/post-game/`:
- Which phases passed/failed?
- Was the decision correct in hindsight?
- Should any criteria be adjusted?

### After 10 Games
Review deployment decisions:
- How many games deployed vs skipped?
- Win rate: Deployed games vs skipped games
- Which phases most often caused skips?
- Any phases that should be added/removed?

### Metrics to Track
```
| Metric | Target | Current |
|--------|--------|---------|
| Games analyzed | 100% of slate | TBD |
| Games deployed | 30-50% of slate | TBD |
| Phase 1 failures | <10% | TBD |
| Phase 2 failures | 20-30% | TBD |
| Phase 3 failures | <15% | TBD |
| Phase 4 failures | 20-30% | TBD |
| Phase 5 failures | <10% | TBD |
| Phase 6 failures | <5% | TBD |
| Phase 7 failures | 10-20% | TBD |
```

**Good Sign:** Most skips happen at Phases 2 or 4 (narrative/value)  
**Bad Sign:** Most skips happen at Phase 6 or 7 (execution issues)

---

## 🎓 PHILOSOPHY

### Why This Works

1. **Eliminates Analysis Paralysis**
   - Clear yes/no at each phase
   - No "maybe" allowed
   - Skip = freedom, not failure

2. **Prevents Forcing Bets**
   - Multiple quality filters
   - Conviction requirement
   - Portfolio fit consideration

3. **Protects Against FOMO**
   - If game fails phase, it's a bad bet
   - Skipping is correct decision
   - No second-guessing allowed

4. **Systematic Learning**
   - Document each decision
   - Review outcomes
   - Iterate criteria

### Key Mindset Shift

**Before Decision Tree:**
> "Should I bet this game? Maybe... let me think about it more... I don't know... might as well try..."

**After Decision Tree:**
> "Phase 2 fails. Skip. Next game."

**Clarity > Perfection**

---

## 📊 QUICK REFERENCE

```
╔═══════════════════════════════════════════════════════════════╗
║ DEPLOYMENT DECISION TREE - QUICK CHECKLIST                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ □ Phase 1: Goalies confirmed?                                ║
║ □ Phase 2: DNA alignment clear?                              ║
║ □ Phase 3: 2+ Tier 1 stars available?                        ║
║ □ Phase 4: 3+ props with value?                              ║
║ □ Phase 5: Portfolio fit (no correlation bomb)?              ║
║ □ Phase 6: Can execute RIGHT NOW?                            ║
║ □ Phase 7: Conviction ≥7/10?                                 ║
║                                                               ║
║ ALL 7 PASS → ✅ DEPLOY                                       ║
║ ANY FAIL → ❌ SKIP (no regrets)                              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

**Last Updated:** December 3, 2025  
**Owner:** Billy (ApexViper)  
**Status:** Production-ready  
**Next Review:** After 10 games OR when skip rate <20% OR >60%

**The best bet is often the one you don't make.** 🐍⚡
