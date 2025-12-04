# 🎰 TICKET ARSENAL v2.1 (Playbook Update)

**Version:** v2.1  
**Date:** 2025-12-04  
**Status:** 🧪 ACTIVE TESTING (First deployment: 12/3/25 - 19 tickets)  
**Test Phase:** Types 1-7 production, Type 8 experimental  
**Next Review:** After 10 games OR December 13, 2025  
**Validation Required:** Type-by-type win rate data

---

## 📋 ANCHOR VARIANT RULES

This update formalizes the Anchor Variant rules and the updated decision tree for totals. Integrate these rules into ticket generation and late-window decision logic.

### Anchor Variant Rules
- **Defensive Anchor** → Under ONLY (no splits)
- **Offensive Anchor** → Over ONLY (no splits)
- **Middle Anchor** → Split Over/Under (very rare; only for true 50/50 games)

### Totals Decision Tree & Stake Sizing
- **Defensive** → Under only | Stake: $1.50
- **Offensive** → Over only | Stake: $1.50
- **Balanced** → Split | Stake: $1.25 each side
- **Unsure** → Skip totals; redirect allocation to player props (SOG, PIM, 1+ points, etc.)

### Late Window Protocol (10:00 PM ET onward)
- Verify goalie matchup and rest/back-to-back status (must annotate match metadata).
- Cross-check team-dna Anchor tag and live SOG/shot quality feeds.
- For Tier A players (e.g., Gauthier — TIER 1 STAR): consider plus-up allocation per Tier rules (Tier A default bet $2.50 unless constrained).
- Mandatory: For any manual corrective re-bet, follow the two-step confirmation protocol.

### Risk Controls
- Max exposure per game: configurable, default $10
- Fat-finger safeguard: confirmation for stakes > $5 or manual corrective re-bets
- Reconciliation: pending tickets must remain flagged until settled by exchange

### Protocol Compliance Notes
- Ensure Protocol Addendum 2.7.1 compliance: latency and memory targets (<50ms execution, <20MB RAM usage) for any automated decision path.

---

## 🎯 ARSENAL PHILOSOPHY

**Before Ticket Arsenal:**
- Guessing bet structures game-to-game
- Inconsistent sizing and construction
- No historical performance tracking
- "What should I bet?" every single time

**After Ticket Arsenal:**
- Named, repeatable betting structures
- Standard deployment models per situation
- Win rate tracking by ticket type
- "Which ticket type fits this game?"

**Core Principle:** Standardization enables iteration. Can't improve what you don't measure.

---

## 📚 THE 8 TICKET TYPES

### Quick Reference Table

| Type | Purpose | Size | Legs | Risk Level | When to Deploy |
|------|---------|------|------|------------|----------------|
| **1. ANCHOR** | Foundation/Insurance | $2-3 | 1-2 | Low | Every deployment |
| **2. VOLUME STACK** | Exploit edge | $0.50-1 ea | 1 | Low | 3+ value props |
| **3. MIRROR** | Hedge/Both-sides | $1-2 total | 2-4 | Medium | Unclear winner |
| **4. BLACK SWAN** | Catastrophe insurance | $0.50 | 4-6 | Medium | Heavy one-side |
| **5. GOD MODE** | Lottery ticket | $0.50-1 | 8-12 | High | Max 1 per slate |
| **6. SUPERSTAR LADDER** | Elite targeting | $1-2 total | 1-3 | Low | Tier 1 star |
| **7. SPECIALIST** | Depth scoring | $0.50-1 | 1-2 | Medium | Value on depth |
| **8. TIME-HEDGED** | 🧪 Experimental | $3-4 | 2-3 | Medium | Test phase |

---

## 📖 DETAILED TICKET SPECIFICATIONS

### **TYPE 1: THE ANCHOR**

**Purpose:** Foundation bet that should hit 60-70% of the time. Portfolio insurance.

**Structure:**
- **Legs:** 1-2 props maximum
- **Criteria:** Tier 1 star, >70% historical hit rate, favorable matchup
- **Size:** $2-3
- **Odds Target:** -150 to +120 (sweet spot: -120 to +100)

**Examples:**
```
ANCHOR A (Single Prop):
├─ MacKinnon 3+ SOG (-135)
└─ Risk: $2.50 | To Win: $1.85

ANCHOR B (2-Prop Combo):
├─ Pastrnak 2+ SOG (-200)
├─ Pastrnak 1+ Point (+120)
└─ Risk: $2.00 | To Win: $2.80 (combined ~+140)
```

**Deployment Model:**
- **Every game you bet:** Start with 1 anchor
- **High-conviction games:** 2 anchors (different players)
- **Never:** 0 anchors

**Success Criteria:**
- Win rate: >60%
- ROI: Slightly positive to neutral
- Purpose: Minimize total-loss nights

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 2: THE VOLUME STACK**

**Purpose:** When you identify 3+ props with edge, stack singles for diversification.

**Structure:**
- **Legs:** 1 prop per ticket
- **Quantity:** 3-10 tickets
- **Criteria:** Each prop has identified +EV vs historical/matchup
- **Size:** $0.50-1.00 per ticket
- **Odds Target:** -130 to +150

**Examples:**
```
VOLUME STACK (5 tickets on CAR @ OTT):
├─ Ticket 1: Aho 3+ SOG (-125) | $1.00
├─ Ticket 2: Svechnikov 2+ SOG (-110) | $0.75
├─ Ticket 3: Tkachuk 1+ Point (-105) | $1.00
├─ Ticket 4: Stutzle 3+ SOG (+105) | $0.50
└─ Ticket 5: CAR Team Total O2.5 (-115) | $0.75
Total Risk: $4.00 | Need 2/5 to profit
```

**Deployment Model:**
- **When:** 3+ props pass value test (Phase 4 of Decision Tree)
- **How many:** 1 ticket per qualified prop
- **Size each:** Proportional to conviction (0.5x-1x base unit)

**Success Criteria:**
- Win rate: >50% (at -110 odds, 52.4%+ is profitable)
- ROI: Positive (even if slightly)
- Purpose: Exploit edges systematically

**Advantage Over Parlay:**
- Diversification: 2/5 wins = profit vs parlay needs all 5
- Variance reduction: Smooth returns
- Learning: Track which prop types perform best

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 3: THE MIRROR**

**Purpose:** Hedge strategy when game outcome is unclear but props exist both sides.

**Structure:**
- **Legs:** 2-4 props, evenly split between both teams
- **Criteria:** Props that can hit regardless of winner
- **Size:** $1-2 per mirror ticket
- **Odds Target:** Combined +200 to +400

**Examples:**
```
MIRROR A (Defensive Grind):
├─ Team A Under 2.5 goals
├─ Team B Under 2.5 goals
├─ Both Goalies 25+ Saves
└─ Low-scoring narrative regardless of winner
Risk: $2.00 | To Win: $6.00 (+300)

MIRROR B (Both Offenses Pop):
├─ Team A Star 3+ SOG
├─ Team B Star 3+ SOG  
├─ Team A Star 1+ Point
└─ Team B Star 1+ Point
Risk: $1.50 | To Win: $4.50 (+300)
```

**Deployment Model:**
- **When:** Decision Tree Phase 7 conviction = 5-6/10
- **When:** DNA suggests "both teams do their thing"
- **When:** You can't pick a side clearly

**Success Criteria:**
- Win rate: >35% (at +300 odds)
- ROI: Neutral to slightly positive
- Purpose: Profit from uncertainty

**Key Insight:**
> Don't force a side when both sides have merit. Bet the props that don't care who wins.

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 4: THE BLACK SWAN**

**Purpose:** Insurance against catastrophic loss when heavily exposed to one side.

**Structure:**
- **Legs:** 4-6 props from the OPPOSITE side of your main exposure
- **Criteria:** Props that hit if your main narrative is completely wrong
- **Size:** $0.50
- **Odds Target:** +500 to +1500

**Examples:**
```
Main Portfolio: $10 on "CAR dominates OTT"
├─ CAR stars props
├─ CAR team total overs
└─ OTT unders

BLACK SWAN Insurance:
├─ OTT wins in regulation (+180)
├─ OTT Team Total O3.5 (+140)
├─ Stutzle 2+ Points (+350)
├─ Tkachuk 1 Goal (+220)
└─ CAR goalie 5+ goals against (+200)
Risk: $0.50 | To Win: ~$12 (if OTT crushes)

Result: If OTT wins big, Black Swan covers most losses
```

**Deployment Model:**
- **When:** >70% of portfolio exposed to one narrative
- **When:** Total exposure on game >$12
- **Size:** ~5-10% of your total game exposure

**Success Criteria:**
- Win rate: <20% (it's insurance, should rarely hit)
- ROI: Negative on its own (that's okay)
- Purpose: Bankroll protection, reduce max loss

**Psychological Benefit:**
- Removes "what if I'm completely wrong?" anxiety
- Allows aggressive main position
- Small cost for peace of mind

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 5: GOD MODE**

**Purpose:** Pure lottery ticket. Maximum entertainment, maximum payout, maximum loss expectation.

**Structure:**
- **Legs:** 8-12 props
- **Criteria:** Props you genuinely believe in (not random)
- **Size:** $0.50-1.00
- **Odds Target:** +1000 to +10000

**Examples:**
```
GOD MODE Ticket (12 legs):
├─ Game 1: Star A 3+ SOG
├─ Game 1: Star B 1+ Point
├─ Game 1: Team Total Over
├─ Game 2: Star C 4+ SOG
├─ Game 2: Star D 2+ Points
├─ Game 2: Goalie 30+ Saves
├─ Game 3: Star E 1 Goal
├─ Game 3: Star F 1+ Assist
├─ Game 3: Team ML
├─ Game 4: Star G 3+ SOG
├─ Game 4: Team Total Under
└─ Game 4: Both Teams Score
Risk: $0.50 | To Win: $500-5000 (depending on odds)
```

**Deployment Model:**
- **Frequency:** Maximum 1 per slate
- **When:** After anchors/volume stacks placed
- **Time limit:** Build in <2 minutes (don't overthink)

**Success Criteria:**
- Win rate: <5% (expected)
- ROI: Highly negative (expected)
- Purpose: Massive upside potential, entertainment value

**Critical Rules:**
1. NEVER chase God Mode losses
2. NEVER increase size beyond $1
3. NEVER skip anchors to afford God Mode
4. Accept it will lose 95%+ of the time

**Why Include This?**
- Satisfies "lottery ticket" urge in controlled way
- Better than uncontrolled parlay chasing
- Occasionally hits huge (bankroll reset potential)
- Fun factor (don't discount this)

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 6: THE SUPERSTAR LADDER**

**Purpose:** Tiered approach to elite players, scaling bet size with difficulty.

**Structure:**
- **Legs:** 1-3 props on same elite player
- **Criteria:** Tier 1 superstar with multiple prop options
- **Tiers:**
  - Tier A (Easy): 2+ SOG ($2)
  - Tier B (Medium): 3+ SOG ($1)
  - Tier C (Hard): 1+ Point ($0.50)
- **Total Size:** $3.50

**Examples:**
```
SUPERSTAR LADDER: Nathan MacKinnon
├─ Ticket 1: MacKinnon 2+ SOG (-250) | $2.00 → Win $0.80
├─ Ticket 2: MacKinnon 3+ SOG (-140) | $1.00 → Win $0.71
└─ Ticket 3: MacKinnon 1+ Point (+110) | $0.50 → Win $0.55
Total Risk: $3.50

Outcomes:
- 0/3 hit: Lose $3.50 (rare, MacK is elite)
- 1/3 hit (Tier A): Lose $2.00 (partial loss)
- 2/3 hit (A+B): Profit $0.01 (break-even)
- 3/3 hit (A+B+C): Profit $2.06 (best case)
```

**Deployment Model:**
- **When:** Elite Tier 1 star in elite matchup
- **Who:** MacKinnon, Pastrnak, Matthews, McDavid tier only
- **Frequency:** 1-2 per slate maximum

**Success Criteria:**
- Win rate Tier A: >85%
- Win rate Tier B: >65%
- Win rate Tier C: >50%
- Overall ROI: Positive

**Advantage:**
- Even if hard prop misses, easier props cushion loss
- Scalable risk based on difficulty
- Consistent approach to stars

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 7: THE SPECIALIST**

**Purpose:** Target depth/specialist players with specific roles (PP QB, shot-blocker, etc.)

**Structure:**
- **Legs:** 1-2 props
- **Criteria:** Tier 2-3 player in specific role with value line
- **Size:** $0.50-1.00
- **Odds Target:** -110 to +200

**Examples:**
```
SPECIALIST A (Defenseman PP Quarterback):
├─ Cale Makar 1+ Point (-105)
└─ PP1 usage + elite matchup
Risk: $1.00 | To Win: $0.95

SPECIALIST B (Shot-Blocking Grinder):
├─ Depth D-man 3+ Blocks (+130)
└─ Defensive game script, heavy PK time
Risk: $0.50 | To Win: $0.65

SPECIALIST C (Hot Goalie):
├─ Goalie 30+ Saves (-115)
└─ Faces high-volume shooting team
Risk: $0.75 | To Win: $0.65
```

**Deployment Model:**
- **When:** Specific role player has clear path to production
- **When:** Line offers value vs player's role expectation
- **Avoid:** Generic "depth guy might do something"

**Roles to Target:**
- PP1 defensemen (points in high-scoring games)
- Shot-blocking specialists (defensive games)
- Hot backup goalies (save volume matchups)
- 3rd line grinders (on hot streak)

**Success Criteria:**
- Win rate: >55%
- ROI: Positive
- Purpose: Extract value from non-stars

**Key Insight:**
> Depth players are less efficient priced. Market focuses on stars. Opportunity exists in specialists.

**Historical Context:**
- First deployed: 12/3/25
- Sample size: TBD
- Current record: TBD

---

### **TYPE 8: THE TIME-HEDGED ANCHOR** 
**⚠️ EXPERIMENTAL STATUS ⚠️**

**Current Status:** 
- Test Phase: Active (1 game deployed 12/3/25)
- Sample Size: 1/5 required
- Win/Loss: [PENDING]
- Decision Date: After 5 games OR December 10, 2025

**Testing Protocol:**
- Deploy on next 4 games
- Track: Cost, Win scenarios hit, Net P/L
- **PASS threshold:** 3/5 games profitable
- **FAIL threshold:** 0-1/5 games profitable

**If PASS:** Promote to standard arsenal  
**If FAIL:** Archive as "interesting but unprofitable"  
**If INCONCLUSIVE (2/5):** Extend test to 10 games

---

**Purpose:** Hedge against timing uncertainty by betting same prop at different lines across periods.

**Structure:**
- **Legs:** 2-3 tickets on same prop, different time frames
- **Criteria:** High-usage player, prop available for full game + periods
- **Size:** $3-4 total (split across tickets)
- **Odds Target:** Combined break-even ~2/3 scenarios

**Example:**
```
TIME-HEDGED: Auston Matthews SOG
├─ Ticket 1: Matthews 1P Under 1.5 SOG (+110) | $1.00
├─ Ticket 2: Matthews 2P+3P Over 2.5 SOG (-105) | $1.50
└─ Ticket 3: Matthews Full Game 3+ SOG (-125) | $1.50
Total Risk: $4.00

Win Scenarios:
1. Matthews quiet 1P, hot later: Tickets 1+2+3 WIN → +$5.50
2. Matthews hot 1P, quiet later: Ticket 3 WIN → -$0.50
3. Matthews 1 SOG each period: Tickets 1+3 WIN → +$2.00
4. Matthews cold all game: Ticket 1 WIN → -$1.65
```

**Hypothesis:**
- Can profit from period-to-period variance
- Reduces "right read, wrong timing" losses
- More expensive but smoother variance

**Why Experimental?**
1. Complex to construct (time cost)
2. Higher total risk than single anchor
3. Unproven ROI vs simple anchor
4. May be overthinking

**Test Plan:**
- Deploy on next 4 games (5 total)
- Track construction time (should be <3 min)
- Calculate per-game P/L
- Compare ROI vs Type 1 Anchor on same games

**Success Criteria (Promotion to Production):**
- 3/5 games: Net profit
- Average ROI: Better than Type 1 Anchor
- Construction time: <3 minutes
- Mental clarity: No analysis paralysis

**Failure Criteria (Archive):**
- 0-1/5 games: Net profit
- Worse ROI than simple anchor
- Construction time: >5 minutes
- Creates confusion/overthinking

**Historical Context:**
- Conceived: 12/3/25
- First deployed: 12/3/25 (DAL @ NJD)
- Current record: 0-0-1 (pending)
- Status: Under evaluation

---

## 🎮 DEPLOYMENT STRATEGY

### Game-by-Game Approach

**For Each Game:**

```
STEP 1: Identify game conviction (Decision Tree Phase 7)
├─ 8-10/10: Full deployment (5-7 tickets)
├─ 6-7/10: Standard deployment (3-5 tickets)
├─ 5/10: Minimal deployment (1-2 tickets)
└─ <5/10: Skip game

STEP 2: Select ticket types based on situation

High Conviction (8-10/10):
├─ 1-2x Anchor (Type 1)
├─ 1x Volume Stack (Type 2) - 3-5 singles
├─ 1x Superstar Ladder (Type 6) if elite star
├─ 1x Black Swan (Type 4) if heavy one side
└─ Optional: 1x God Mode (Type 5) across slate

Medium Conviction (6-7/10):
├─ 1x Anchor (Type 1)
├─ 1x Volume Stack (Type 2) - 2-3 singles
├─ 1x Mirror (Type 3) if both-sides narrative
└─ Optional: 1x Specialist (Type 7) if value

Low Conviction (5/10):
├─ 1x Anchor (Type 1) OR
└─ 1x Specialist (Type 7)

STEP 3: Size appropriately
- High conviction: Max risk ($12-15 total)
- Medium conviction: Standard risk ($8-10 total)
- Low conviction: Minimal risk ($2-3 total)
```

### Multi-Game Portfolio

**3-Game Slate Example:**

```
Total Bankroll: $569
Max Daily Risk: $19.50 (3% of bankroll)
Target Deployment: $15-18

GAME 1 (High Conviction - 8/10):
├─ Anchor x2: $5.00
├─ Volume Stack x3: $3.00
├─ Superstar Ladder: $3.50
└─ Black Swan: $0.50
Total: $12.00

GAME 2 (Medium Conviction - 6/10):
├─ Anchor x1: $2.50
├─ Volume Stack x2: $2.00
└─ Mirror: $1.50
Total: $6.00

GAME 3 (Low Conviction - 5/10):
├─ Specialist x1: $0.75
Total: $0.75

SLATE-WIDE:
└─ God Mode x1 (across all 3 games): $0.50

GRAND TOTAL: $19.25 (within $19.50 max)
```

---

## 📊 PERFORMANCE TRACKING

### Per-Ticket-Type Metrics

**Track After Each Game:**

```markdown
## [DATE] Performance

### Type 1 - Anchor
- Deployed: [X] tickets
- Won: [X] | Lost: [X]
- Total Risk: $[X] | Total Return: $[X]
- ROI: [X]%
- Notes: [What worked/didn't]

### Type 2 - Volume Stack
[Same structure]

[Repeat for all types]
```

**Update Running Totals in README:**

Update the status table after every 5 games to track trends.

---

## 🔄 ITERATION PROTOCOL

### After 10 Games (First Review)

**For Each Ticket Type:**

1. **Calculate Win Rate**
   - If <40%: Flag for review
   - If <30%: Consider modification or removal

2. **Calculate ROI**
   - Negative ROI: Why? Fix or drop?
   - Positive ROI: What's working? Do more?

3. **Assess Deployment Frequency**
   - Deployed too often (>60% of games): Diluting edge?
   - Deployed too rarely (<20% of games): Not enough data?

4. **Subjective Evaluation**
   - Is this ticket type fun/useful?
   - Does it cause analysis paralysis?
   - Does it fit within 10-min execution window?

### After 25 Games (Comprehensive Audit)

1. **Arsenal-Wide Review**
   - Which ticket types are core (always use)?
   - Which are situational (specific conditions)?
   - Which should be dropped?

2. **Sizing Adjustments**
   - Increase sizing on high-ROI types
   - Decrease sizing on negative-ROI types

3. **New Ticket Type Development**
   - Based on 25 games, any patterns emerged?
   - New structure worth testing?
   - Add as Type 9 (experimental)

---

## ✅ QUICK REFERENCE

```
╔═══════════════════════════════════════════════════════════════╗
║ TICKET ARSENAL v2.0 - QUICK SELECT                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ START EVERY DEPLOYMENT:                                      ║
║ → Type 1 (Anchor) - Foundation                               ║
║                                                               ║
║ IF 3+ VALUE PROPS:                                           ║
║ → Type 2 (Volume Stack) - Singles                            ║
║                                                               ║
║ IF UNCLEAR WINNER:                                           ║
║ → Type 3 (Mirror) - Both sides                               ║
║                                                               ║
║ IF HEAVY ONE SIDE (>$10):                                    ║
║ → Type 4 (Black Swan) - Insurance                            ║
║                                                               ║
║ IF ELITE STAR:                                               ║
║ → Type 6 (Superstar Ladder) - Tiered                         ║
║                                                               ║
║ IF DEPTH VALUE:                                              ║
║ → Type 7 (Specialist) - Role player                          ║
║                                                               ║
║ ONCE PER SLATE:                                              ║
║ → Type 5 (God Mode) - Lottery                                ║
║                                                               ║
║ EXPERIMENTAL (5-game test):                                  ║
║ → Type 8 (Time-Hedged) - Period splits                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

**Last Updated:** December 4, 2025  
**Owner:** Billy (ApexViper)  
**Version:** 2.1  
**Status:** Active testing phase  
**Next Review:** After 10 games

**Standardized structures. Measurable results. Continuous iteration.** 🐍⚡🎯
