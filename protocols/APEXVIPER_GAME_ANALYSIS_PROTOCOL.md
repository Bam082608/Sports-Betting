# 🐍 APEXVIPER GAME ANALYSIS PROTOCOL v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Standardize the workflow for analyzing NHL games and generating GitHub-ready intelligence files.

---

## Mission

This protocol defines how data agents (Gemini/Grok) and analysis agents (Claude/VIPER-ZERO) must cooperate, and how outputs are stored for long-term use.

**Applies to:**
- All NHL game analyses.
- All APEXVIPER agents participating in data ingestion, analysis, or recommendation generation.

---

## 1. PRE-ANALYSIS CHECKLIST (MANDATORY)

Before any analysis, the agent must complete this checklist.

### Step 1: Temporal Lock
Confirm and state explicitly:
- ✅ Current Date: [INSERT DATE]
- ✅ Training Data Cutoff: January 2025
- ✅ Status: All 2025–26 data requires live verification

### Step 2: Game Identification
Define the game context:
- Away Team: [ABBREVIATION]
- Home Team: [ABBREVIATION]
- Game Time: [TIME] ET
- Venue: [ARENA, CITY]

### Step 3: Data Sources Confirmed
Check and list all data sources used:
- Goalie confirmations (DailyFaceoff or user-provided)
- Injury report (updated within last 24h)
- Line combinations (if available)
- Odds from at least 2 sportsbooks

> **No betting recommendation should be made until Steps 1–3 are completed and documented.**

---

## 2. PHASE 1 — DATA INGESTION (TASK AGENT: GEMINI / GROK)

### Role
Data agents (e.g., Gemini, Grok, Copilot with browsing) are responsible for **structuring data only**, not making betting decisions.

### Input
- Screenshots, URLs, or raw notes from Billy.

### Output
A markdown block containing the following tables, ready to be dropped into `research/YYYY-MM-DD_[AWAY]_at_[HOME]-analysis.md`.

### Table 1: Team Stats Comparison

| Stat Category        | Away Team         | Home Team         | Edge |
|----------------------|-------------------|-------------------|------|
| Record               | [W-L-OTL]         | [W-L-OTL]         | [🏆 TEAM] |
| Goals For            | [#] ([Rank])      | [#] ([Rank])      | [🏆 TEAM] |
| Goals Against        | [#] ([Rank])      | [#] ([Rank])      | [🏆 TEAM] |
| Power Play %         | [%] ([Rank])      | [%] ([Rank])      | [🏆 TEAM] |
| Penalty Kill %       | [%] ([Rank])      | [%] ([Rank])      | [🏆 TEAM] |
| Shooting %           | [%] ([Rank])      | [%] ([Rank])      | [🏆 TEAM] |
| Recent Form (L5)     | [Record]          | [Record]          | [🏆 TEAM] |

### Table 2: Line Shopping Matrix

| Sportsbook | Away ML | Home ML | Spread        | Total       |
|-----------|---------|---------|--------------|-------------|
| FanDuel   | [odds]  | [odds]  | [line/odds]  | O/U [#]     |
| BetMGM    | [odds]  | [odds]  | [line/odds]  | O/U [#]     |
| [Other]   | [odds]  | [odds]  | [line/odds]  | O/U [#]     |

**ARBITRAGE ALERT:** [If 30+ cent difference exists, flag here]

### Table 3: Confirmed Goalies

| Team | Starter | GP | W-L-OTL | GAA | SV%  | Recent Form        |
|------|---------|----|---------|-----|------|--------------------|
| [AWAY] | [Name] | [#] | [Record] | [#] | [%] | [Last 3 games]    |
| [HOME] | [Name] | [#] | [Record] | [#] | [%] | [Last 3 games]    |

**Injury/Fatigue Flags:** [B2B? Long road trip? Coming off injury?]

### Table 4: Star Concentration (Shot Volume Leaders)

**Away Team Top 3:**
| Player | Position | SOG/GP | Team Share % | 2+ SOG Odds |
|--------|----------|--------|--------------|-------------|
| [Name] | [POS]    | [#]    | [%]          | [odds]      |
| [Name] | [POS]    | [#]    | [%]          | [odds]      |
| [Name] | [POS]    | [#]    | [%]          | [odds]      |

**Home Team Top 3:**
| Player | Position | SOG/GP | Team Share % | 2+ SOG Odds |
|--------|----------|--------|--------------|-------------|
| [Name] | [POS]    | [#]    | [%]          | [odds]      |
| [Name] | [POS]    | [#]    | [%]          | [odds]      |
| [Name] | [POS]    | [#]    | [%]          | [odds]      |

### Table 5: Key Injuries & Line Changes

**Away Team:**
- [Player] ([Position]): [Status] — [Impact: High/Medium/Low]
- [Player] ([Position]): [Status] — [Impact: High/Medium/Low]

**Home Team:**
- [Player] ([Position]): [Status] — [Impact: High/Medium/Low]
- [Player] ([Position]): [Status] — [Impact: High/Medium/Low]

### Table 6: Recent Head-to-Head (If Available)

| Date   | Matchup        | Score | Key Takeaway                |
|--------|----------------|-------|-----------------------------|
| [Date] | [Away] @ [Home]| [X-Y] | [1-sentence game insight]   |

### Constraint
- Data agents **must not** make recommendations in Phase 1.
- Output is purely structured data.

---

## 3. PHASE 2 — VIPER ANALYSIS (TASK AGENT: CLAUDE / VIPER-ZERO)

### Role
Analysis agents (Claude/VIPER‑ZERO class) take Phase 1 tables and apply all APEXVIPER protocols: Macro Intelligence, Team DNA, Goalie Intelligence, Fatigue Matrix, Altitude Edge, Public Money, Portfolio Construction, and Master Query Protocol.

### Input
- Phase 1 tables.
- Existing protocol files in `protocols/`.
- Relevant `nhl/team-dna/*.md` and `research/*-slate-data.md`.

### Output
Narrative and structured analysis blocks, ready to embed under `## VIPER Analysis` and `## Betting Recommendation`.

### Analysis Block 1: Universal Law Application

Agent must check each relevant macro/protocol:

- Weather / environment (if applicable).
- Public Tax (APEXVIPER_PUBLIC_MONEY).
- B2B and fatigue (APEXVIPER_FATIGUE_MATRIX).
- Backup goalie / starter status (APEXVIPER_GOALIE_INTELLIGENCE).
- Altitude edge (APEXVIPER_ALTITUDE_EDGE) for COL/UTA.
- Home underdog law (APEXVIPER_HOME_UNDERDOG).
- Portfolio construction constraints (APEXVIPER_PORTFOLIO_CONSTRUCTION).
- Team DNA for both teams (nhl/team-dna/*.md).

Summarize as:

```markdown
**Universal Law Check:**
- Weather / Environment: [Notes or N/A]
- Public Money / Brand Tax: [Notes]
- B2B / Fatigue: [Notes]
- Goalie Situation: [Starter/Backup, risk assessment]
- Altitude / Home Edge: [Notes]
- Home Underdog Signal: [Yes/No, why]
- Team DNA Conflicts: [e.g., "Fade Centers vs PHI"]
```

### Analysis Block 2: Pattern Recognition ("Free Will Theory")

```markdown
**[AWAY TEAM] Pattern:**
- Structural Identity: [Offensive / Defensive / Balanced]
- Shot Volume Tendency: [High / Average / Low] — [Rank]
- Current Streak: [W/L streak] — Cause: [Injury / Variance / Schedule]
- Road Performance: [Record] — [Key trend]

**[HOME TEAM] Pattern:**
- Structural Identity: [Offensive / Defensive / Balanced]
- Shot Volume Tendency: [High / Average / Low] — [Rank]
- Current Streak: [W/L streak] — Cause: [Injury / Variance / Schedule]
- Home Performance: [Record] — [Key trend]

**Collision Point:**
[2–3 sentences on likely game script when these patterns collide]
```

### Analysis Block 3: Star Concentration Theory

```markdown
**Foundation Anchors (≈3.5+ SOG/GP):**
- [Player] ([Team]): [SOG/GP], [Team Share %]
  └ Bet Structure: [Solo leg vs anchor leg in parlays]

**Correlation Zone (2.5–3.5 SOG/GP):**
- [Player] ([Team]): [SOG/GP], [Team Share %]
  └ Bet Structure: [Best paired with which angles]

**Lottery Candidates (<2.5 SOG/GP but +EV odds):**
- [Player] ([Team]): [SOG/GP] with [favorable odds]
  └ Bet Structure: [Small stake, high-upside ticket]
```

### Analysis Block 4: Line Value & Market Inefficiency

```markdown
**Best Available Prices:**
- Away ML: [Book] @ [odds] (worst: [odds])
- Home ML: [Book] @ [odds] (worst: [odds])
- Spread: [Best book, line/odds]
- Total: [Best book, O/U + odds]

**Market Signals:**
- Reverse Line Movement: [Yes/No + explanation]
- Sharp/Steam Indicators: [Any notable moves or freezes]
```

---

## 4. PHASE 3 — BETTING RECOMMENDATION (VIPER OUTPUT)

The analysis agent must produce:

### Primary Bet

```markdown
**PRIMARY BET:** [Team/Prop] at [Odds] on [Book]  
**STAKE:** [e.g., 1.5–2.0% bankroll]  
**REASONING:** [2–3 sentences tying Universal Laws + Team DNA + Price]
```

### Correlation Parlay (Foundation Ticket)

```markdown
**CORRELATION PARLAY (Core Ticket):**
- Leg 1: [Bet] — [Odds]
- Leg 2: [Bet] — [Odds]
- Leg 3: [Bet] — [Odds]
**Combined Odds:** [Value]

**Logic:** [Short description of correlation between legs]  
**Floor Security:** [Which leg is the "anchor" with the safest floor]
```

### Hedge Strategy

```markdown
**HEDGE PLAN:**
If we take [Primary Bet], offset risk with:
- [Hedge Bet] — [Odds]

**Rationale:** [1–2 sentences explaining how hedge protects downside]
```

### Lottery Ticket (Optional)

```markdown
**LOTTERY TICKET (Small Stake):**
- Structure: [3–4 leg longshot parlay]
- Rationale: [Why outcome is unlikely but plausible]
- Stake: [Tiny fraction of bankroll, e.g., 0.25–0.5%]
```

### Titanic Rule Compliance Check

```markdown
**TITANIC RULE CHECK:**
- ✅ No single team is the linchpin of multiple parlays.
- ✅ No player appears in more than 2 tickets.
- ✅ Exposure diversified across teams/games.
```

If the Titanic Rule is violated, the agent must **flag and adjust** the recommended tickets.

---

## 5. PHASE 4 — GITHUB OUTPUT FORMAT

### Target File Location (Example)
- `research/2025-12-01_CBJ_at_NJD-analysis.md`

### Filename Convention
- `YYYY-MM-DD_[AWAY]_at_[HOME]-analysis.md`  
  Example: `2025-12-01_CBJ_at_NJD-analysis.md`

### File Structure

```markdown
# [AWAY TEAM] @ [HOME TEAM] — [DATE]

## Pre-Analysis Context
[Temporal Lock + Game Identification + Source Check]

## Phase 1 — Data Tables
[Insert Tables 1–6 from Data Ingestion]

## VIPER Analysis
[Insert Universal Law Check, Patterns, Star Concentration, Market Notes]

## Betting Recommendation
[Primary Bet, Correlation Parlay, Hedge, Lottery Ticket if any, Titanic Rule Check]

## Post-Game Update (Fill After Game)
**Final Score:** [Score]  
**Primary Bet Result:** [W/L, +/- units]  
**Correlation Parlay Result:** [W/L, +/- units]  
**Lottery Ticket Result:** [W/L, +/- units]

**Lessons Learned:**
- [What worked]  
- [What didn't]  
- [Any protocol adjustments suggested]
```

---

## 6. ROLE ASSIGNMENTS (AGENT EXPECTATIONS)

### GEMINI / GROK / DATA AGENT
- Execute **Phase 1** only.
- No betting opinions.
- Output clean markdown for tables and context.

### VIPER (CLAUDE / HIGH-LEVEL ANALYST)
- Execute **Phase 2 & Phase 3**.
- Must honor:
  - APEXVIPER_MACRO_INTELLIGENCE
  - APEXVIPER_QUERY_PROTOCOL
  - APEXVIPER_GOALIE_INTELLIGENCE
  - APEXVIPER_FATIGUE_MATRIX
  - APEXVIPER_ALTITUDE_EDGE
  - APEXVIPER_PUBLIC_MONEY
  - APEXVIPER_PORTFOLIO_CONSTRUCTION
  - Relevant Team DNA & Slate Data

### BILLY (PROJECT LEAD)
- Runs **execution and feedback**:
  - Chooses which ideas to actually bet.
  - Ensures GitHub files are created/updated.
  - Adds post-game results and "Lessons Learned."

---

## 7. PER-GAME CHECKLIST (SHOULD BE TICKED OFF)

- [ ] Temporal lock confirmed (date + cutoff + live data note)  
- [ ] Goalies verified (live/within 24h)  
- [ ] Injuries checked (within 24h)  
- [ ] Line shopping across at least 2 books  
- [ ] Star concentration documented  
- [ ] Universal Laws applied (macro + fatigue + altitude + home dog + public tax)  
- [ ] Team DNA consulted for both sides (if available)  
- [ ] Correlation and hedge structure built  
- [ ] Titanic Rule compliance verified  
- [ ] GitHub analysis file created or updated  
- [ ] Post-game results added after completion

---

## 🎯 CROSS-REFERENCE

This protocol integrates with:
- `protocols/APEXVIPER_MACRO_INTELLIGENCE.md`
- `protocols/APEXVIPER_QUERY_PROTOCOL.md`
- `protocols/APEXVIPER_GOALIE_INTELLIGENCE.md`
- `protocols/APEXVIPER_FATIGUE_MATRIX.md`
- `protocols/APEXVIPER_ALTITUDE_EDGE.md`
- `protocols/APEXVIPER_PUBLIC_MONEY.md`
- `protocols/APEXVIPER_PORTFOLIO_CONSTRUCTION.md`
- `nhl/team-dna/*.md`
- `research/*-slate-data.md`

---

**Status:** READY FOR TESTING. Apply it to tonight's games to validate the workflow end-to-end.

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Standardize the workflow for analyzing NHL games and generating GitHub-ready intelligence files.
