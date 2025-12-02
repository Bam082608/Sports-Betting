# 🐍 APEXVIPER AGENT ROLES v1.0
**Operation Protocol:** MATRIX-FORGE  
**Purpose:** Define clear responsibilities for system execution  
**Owner:** Project Lead (Bam082608)

---

## 1. OVERVIEW

The APEXVIPER system operates through four conceptual agents, each with distinct responsibilities. These roles ensure systematic execution of the betting pipeline:

```
Research → Daily Intel → Executions → Tracking
```

**Golden Rule:** No bet is placed unless it exists in `DAILY INTEL` with proper Tier, Market, Price, and Logic tags.

---

## 2. AGENT DEFINITIONS

### 2.1. VIPER-ZERO (Central Command)

**Role:** Protocol Enforcement & System Integrity

**Responsibilities:**
- Ensures no PDF/screenshot graveyard: all final decisions transcribed into Markdown SITREP format
- Guards the pipeline integrity:
  1. Research (PDF/Spreadsheets/Books)
  2. `nhl/daily-intel/YYYY-MM-DD-slate.md`
  3. `executions/` (actual tickets)
  4. `tracking/` (results/ROI)
- Enforces that every wager has:
  - A `DAILY INTEL` record
  - A DNA link
  - A Tier tag
  - A Result field to be updated

**Primary Command:**
> No bet is placed unless the game and target exist in `DAILY INTEL` and are tagged with Tier, Market, Price, and Logic.

**Verification Checklist:**
- [ ] All targets have unique IDs (e.g., DAL-1, OTT-2)
- [ ] All targets have Result field `[PENDING]`
- [ ] DNA links connect to `nhl/team-dna/` files
- [ ] Tier tags match `tier1-stars.md` or `tier2-players.md`

---

### 2.2. GEMINI "THE EYE" (Data Extraction Analyst)

**Role:** Data Ingestion & Slate Construction

**Responsibilities:**
- Reads external intel sources (books, PDFs, tools, line screens)
- Extracts:
  - Lines and prices
  - Implied probabilities
  - Key averages/projections (SOG averages, PPG)
  - Context (injuries, B2B, matchup edges)
  - "Fast Money" props (Goal in First 10, period props)

**Daily Duties:**
1. For every NHL game being considered:
   - Create `## GAME: AWAY @ HOME (TIME)` block in daily slate
   - Add:
     - `**Status:** ACTIVE`
     - `**DNA Link:** [[away-dna]] | [[home-dna]]`
2. For each game, list all candidate targets in `### TARGETS`:
   - Player / Market / Line / Price / Avg / Logic / Result `[PENDING]`
3. Flag all anchors clearly:
   - e.g., `Tag: [ANCHOR]` or `Price: -750 (ANCHOR)`

**Output Template:**
```markdown
## GAME: AWAY @ HOME (TIME ET)

**Status:** ACTIVE  
**DNA Link:** [[away-team]] | [[home-team]]  
**Edge:** [Brief description of situational edge]

### TARGETS

| ID | Player | Market | Line | Price | Avg | Logic | Tier | Tag | Result |
|----|--------|--------|------|-------|-----|-------|------|-----|--------|
| XXX-1 | Name | SOG | 2+ | -200 | 2.5 | Logic here | Tier 1 | [ANCHOR] | [PENDING] |
```

---

### 2.3. APEX-MATRIX (Portfolio Architect)

**Role:** Matrix & Parlay Design

**Responsibilities:**
Takes structured targets from `DAILY INTEL` and designs bet grids:

**Single-Game Matrices:**
- Build multiple low-stake combos around each game's anchor(s)
- Example structure:
  - Anchor: Robertson 2+ SOG
  - Satellites: Hintz 2+ SOG, Johnston 1+ Point, Goal in First 10

**Cross-Game Matrices:**
- Combine anchors from different games into low-stake parlays
- Spread exposure across the slate

**Design Principles:**

1. **Multiple Anchors (4-5):**
   - Select 4-5 Tier 1, high-confidence, high-consistency legs
   - Must have strong DNA/tier support
   - Price in line with expectation (or underpriced)
   - Label clearly in `DAILY INTEL` file

2. **Low-Stake, High-Count Tickets:**
   - Many tickets at small stakes ($1-3 per parlay)
   - Single plays / same-game parlays / small ladders
   - Nightly P&L driven by breadth of edges, not oversized bets

3. **Double-Edged Parlays per Game:**
   - One combination "Team A performance heavy"
   - Another combination "Team B performance heavy"
   - Optional hybrid "both sides go off" for high-scoring games

**Matrix Template:**
```markdown
### SINGLE-GAME MATRIX: AWAY @ HOME

**Matrix A (Team A Heavy):**
- Star A 2+ SOG [ANCHOR]
- Star A 1+ Point
- Goal in First 10: YES

**Matrix B (Team B Heavy):**
- Star B 2+ SOG
- Star B 1+ Point
- Goal in First 10: YES

**Matrix C (Both Stars - Middle):**
- Star A 2+ SOG [ANCHOR]
- Star B 2+ SOG
```

---

### 2.4. LEDGER-KNIGHT (Risk & Tracking Officer)

**Role:** Exposure Control & Result Logging

**Pre-Bet Responsibilities:**
- Approve per-game exposure caps (max units tied to one game)
- Approve per-anchor exposure caps (max units on single anchor)
- Verify total daily risk within limits

**Post-Bet Responsibilities:**
- Log every fired bet in `executions/YYYY-MM-DD-nhl-executions.md`:
  - Book, Market, Line, Price, Stake, Parlay composition
  - Reference back to `DAILY INTEL` entries
- Update Result fields post-game
- Feed nightly data to `tracking/`:
  - By team, player, Tier, market, and anchor

**Exposure Cap Template:**
```markdown
### Per-Game Exposure Caps
| Game | Max Exposure | Current | Status |
|------|--------------|---------|--------|
| AWAY @ HOME | $10 | $X | ✅/⚠️ |

### Per-Anchor Exposure Caps
| Anchor | Max Exposure | Current | Status |
|--------|--------------|---------|--------|
| Player Line | $8 | $X | ✅/⚠️ |
```

---

## 3. EXECUTION FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│                        DAILY WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. GEMINI extracts slate intel → daily-intel/YYYY-MM-DD.md     │
│                          ↓                                       │
│  2. VIPER-ZERO verifies format → Tags, Tiers, DNA Links         │
│                          ↓                                       │
│  3. APEX-MATRIX designs matrices → Single-game + Cross-game     │
│                          ↓                                       │
│  4. LEDGER-KNIGHT approves exposure → Caps verified             │
│                          ↓                                       │
│  5. EXECUTE → Bets placed during windows                        │
│                          ↓                                       │
│  6. LEDGER-KNIGHT logs → executions/YYYY-MM-DD-executions.md    │
│                          ↓                                       │
│  7. POST-GAME → Results updated, ROI calculated                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. INTER-AGENT COMMUNICATION

### Handoff Protocol

| From | To | Trigger | Deliverable |
|------|-----|---------|-------------|
| GEMINI | VIPER-ZERO | Slate complete | `daily-intel/` file with all TARGETS |
| VIPER-ZERO | APEX-MATRIX | Format verified | Approved targets list |
| APEX-MATRIX | LEDGER-KNIGHT | Matrices designed | Parlay compositions with stakes |
| LEDGER-KNIGHT | EXECUTE | Exposure approved | Final ticket list |
| POST-GAME | LEDGER-KNIGHT | Games complete | Result data for logging |

### Escalation Protocol

- **Invalid Format:** VIPER-ZERO rejects → GEMINI corrects
- **Exposure Exceeded:** LEDGER-KNIGHT blocks → APEX-MATRIX revises
- **Late Scratch:** ALL STOP → Re-evaluate affected matrices

---

## 5. AGENT ACTIVATION CHECKLIST

Before any slate execution:

- [ ] GEMINI: Slate file created with all games and targets
- [ ] VIPER-ZERO: Format verified, all tags present
- [ ] APEX-MATRIX: Matrices designed, anchors distributed
- [ ] LEDGER-KNIGHT: Exposure caps approved, logging template ready

---

## 6. APPENDIX: QUICK REFERENCE

### Tier Stakes
| Tier | Stake | Description |
|------|-------|-------------|
| Tier 1 / A | $2.50 | Elite stars, bet every game |
| Tier 2 / B | $1.25 | Good volume, selective |
| Tier 3 / C | $0.75 | Situational, low confidence |

### Anchor Criteria
- Tier 1 classification
- High-consistency (8/10 games hit)
- High-usage (top line + PP)
- Price ≤ -300 (implied >75% probability)

### Matrix Types
| Type | Description | Stake Range |
|------|-------------|-------------|
| Single-Game | Props within one game | $1-3 |
| Cross-Game | Anchors across games | $1-1.50 |
| Apex | 5+ leg parlays | $0.50-1 |

---

**Version:** 1.0  
**Created:** December 2, 2025  
**Owner:** Project Lead (Bam082608)  
*APEXVIPER System - All systems operational* 🐍
