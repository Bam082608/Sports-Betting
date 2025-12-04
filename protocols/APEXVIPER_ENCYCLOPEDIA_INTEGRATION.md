# 📚 APEXVIPER ENCYCLOPEDIA INTEGRATION PROTOCOL v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Protocol for updating team/player encyclopedia files based on performance data.

---

## OVERVIEW

This protocol defines:
1. Update frequency for all encyclopedia files
2. Data flow from game results to profiles
3. Player tier system and reclassification triggers
4. Team DNA refresh cadence
5. Sunday night routine checklist

---

## 1. UPDATE FREQUENCY SCHEDULE

### File Update Cadence

| File Type | Update Frequency | Trigger |
|-----------|------------------|---------|
| **Team DNA Files** | Weekly (Sunday) | After weekly roundup complete |
| **Player Tier Lists** | Weekly (Sunday) | Performance data review |
| **Game Intel Files** | Archive after 7 days | Maintain rolling window |
| **Daily Research** | Delete after 14 days | Prevent clutter |

### Update Schedule

| Day | Task | Files Affected |
|-----|------|----------------|
| **Sunday** | Major refresh | Team DNA, Player Tiers |
| **Wednesday** | Mid-week check | Hot/Cold streak flags only |
| **Daily** | Minor updates | Research files only |

---

## 2. DATA FLOW PROCESS

### How Game Results Feed Into Team Profiles

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA FLOW DIAGRAM                        │
└─────────────────────────────────────────────────────────────┘

DAILY INPUT
│
├── Game Results → tracking/bet-log.md
│
├── Player Performance → tracking/lessons-learned.md
│
└── Team Observations → research/[date]-notes.md

                    ↓ (Accumulates over week)

WEEKLY AGGREGATION (Sunday)
│
├── tracking/weekly-roundup-template.md
│   ├── Hot Streak Alerts
│   ├── Cold Streak Alerts
│   ├── System Performance Metrics
│   └── Protocol Adjustments
│
                    ↓ (Informs updates)

ENCYCLOPEDIA UPDATES
│
├── nhl/team-dna/[team].md
│   ├── Recent Form (L5 update)
│   ├── Betting DNA adjustments
│   └── Key player status changes
│
├── nhl/tier1-stars.md
│   └── Star reclassification if needed
│
└── nhl/tier2-players.md
    └── Role player tier changes
```

### Integration Rules

1. **Research → Tracking:** Daily game results go into bet-log.md
2. **Tracking → Weekly:** Weekly roundup aggregates tracking data
3. **Weekly → Encyclopedia:** Weekly roundup informs profile updates
4. **Encyclopedia → Protocols:** Profile changes may trigger protocol updates

---

## 3. PLAYER TIER SYSTEM

### Tier Definitions

| Tier | Name | Criteria | Betting Approach |
|------|------|----------|------------------|
| **Tier 1** | Foundation Anchors | ≥3.5 SOG/GP, >75% hit rate (2+) | Solo legs, anchor in parlays. **⚠️ CAVEAT: Vulnerable to Team Floor Events (e.g., 0-goal shutouts). Diversify across teams.** |
| **Tier 2** | Correlation Zone | 2.5-3.5 SOG/GP, 60-75% hit rate | Pair with anchors, layer bets |
| **Tier 3** | Value Plays | 2.0-2.5 SOG/GP, good odds | Selective targets, lottery legs |
| **Tier 4** | Lottery Tickets | <2.0 SOG/GP, +EV odds | Small stakes, high upside only |

### Graduation Criteria (Moving UP)

**Lottery Ticket → Value Play:**
- [ ] 3 consecutive weeks with ≥2.0 SOG/GP average
- [ ] Hit rate (2+ SOG) improved to >50%
- [ ] Consistent line placement (no yo-yo'ing)

**Value Play → Correlation Zone:**
- [ ] 3 consecutive weeks with ≥2.5 SOG/GP average
- [ ] Hit rate (2+ SOG) ≥60%
- [ ] PP time stable at >1:30/game
- [ ] No major line demotions

**Correlation Zone → Foundation Anchor:**
- [ ] 4 consecutive weeks with ≥3.5 SOG/GP average
- [ ] Hit rate (2+ SOG) ≥75%
- [ ] PP1 confirmed placement
- [ ] Top-6 forward or PP1 D-man
- [ ] Verified via weekly roundup data

### Downgrade Criteria (Moving DOWN)

**Foundation Anchor → Correlation Zone:**
- [ ] 2 consecutive weeks with <3.0 SOG/GP average
- [ ] Hit rate (2+ SOG) drops below 65%
- [ ] Lost PP1 placement
- [ ] Or: Injury affecting production

**Correlation Zone → Value Play:**
- [ ] 2 consecutive weeks with <2.5 SOG/GP average
- [ ] Hit rate (2+ SOG) drops below 50%
- [ ] Line demotion (out of top-6)

**Value Play → Lottery Ticket:**
- [ ] 2 consecutive weeks with <2.0 SOG/GP average
- [ ] Hit rate (2+ SOG) drops below 40%
- [ ] Healthy scratch risk

### Tier Transition Log Template
```
DATE: ____________
PLAYER: ____________
PREVIOUS TIER: ____________
NEW TIER: ____________
REASON: ____________________________________________
DATA SUPPORTING CHANGE:
- L5 SOG/GP: ____________
- L10 SOG/GP: ____________
- Hit Rate (2+): ____________%
- Line Placement: ____________
- PP Time: ____________
```

---

## 4. TEAM DNA REFRESH PROTOCOL

### Weekly Update Components

#### Recent Form Updates (Every Sunday)

Update the "Recent Form (L5)" section for each team:

```markdown
## Recent Form (L5)
| Date | Opponent | Result | GF | GA | SOG | Notes |
|------|----------|--------|----|----|-----|-------|
|      |          |        |    |    |     |       |
|      |          |        |    |    |     |       |
|      |          |        |    |    |     |       |
|      |          |        |    |    |     |       |
|      |          |        |    |    |     |       |

L5 Record: ___ - ___ - ___
L5 GF/GP: ___
L5 GA/GP: ___
L5 SOG/GP: ___
```

#### Betting DNA Adjustments

Update betting patterns based on weekly performance:

| Signal | Trigger | Action |
|--------|---------|--------|
| **Hot Streak Flag** | Won 4+ of L5 | Add to "Target" list |
| **Cold Streak Flag** | Lost 4+ of L5 | Add to "Fade" list |
| **High Scoring Flag** | Avg >3.5 GF in L5 | Target overs |
| **Low Scoring Flag** | Avg <2.0 GF in L5 | Fade player props |
| **B2B Performance** | Track 2nd game results | Update B2B note |

#### Protocol Trigger Flags

| Flag | Definition | Action Required |
|------|------------|-----------------|
| 🔥 **HOT** | Won 4+ of L5, scoring well | Increase exposure |
| ❄️ **COLD** | Lost 4+ of L5, struggling | Decrease exposure |
| ⚠️ **B2B ALERT** | Poor 2nd game performance | Apply fatigue matrix |
| 🏠 **HOME STRONG** | >70% home win rate | Target home games |
| ✈️ **ROAD STRONG** | >50% road win rate | Don't fade on road |
| 🥅 **BACKUP RISK** | Starter injured/load managing | Monitor goalie news |

### Team DNA Update Checklist (Sunday)

For EACH team you bet on this week:

- [ ] Update L5 record and stats
- [ ] Check for hot/cold streak flags
- [ ] Review goalie situation
- [ ] Note any lineup changes
- [ ] Update betting DNA section
- [ ] Add protocol trigger flags if applicable

---

## 5. ARCHIVE MANAGEMENT

### When to Archive Files

| File Type | Archive After | Archive Location |
|-----------|---------------|------------------|
| Research daily files | 7 days | archive/research/ |
| Analysis files | 14 days | archive/analysis/ |
| Outdated team intel | Monthly | archive/team-intel/ |

### Archive Naming Convention
```
archive/[type]/[YYYY-MM]/[original-filename]

Examples:
archive/research/2024-12/2024-12-01-slate-data.md
archive/analysis/2024-12/2024-12-05-DAL-vs-CHI-analysis.md
```

### What NOT to Archive (Keep Permanently)
- `protocols/*.md` - Core system files
- `nhl/team-dna/*.md` - Team profiles (update, don't archive)
- `nhl/tier1-stars.md` - Player tier lists
- `nhl/tier2-players.md` - Player tier lists
- `tracking/bankroll.md` - Running bankroll
- `tracking/bet-log.md` - Full bet history

---

## 6. SUNDAY NIGHT ROUTINE CHECKLIST

### Complete Every Sunday (Estimated Time: 45-60 min)

```
═══════════════════════════════════════════════════════════
SUNDAY NIGHT ENCYCLOPEDIA UPDATE ROUTINE
Date: ____________
═══════════════════════════════════════════════════════════

PHASE 1: WEEKLY ROUNDUP COMPLETION (15-20 min)
- [ ] Complete tracking/weekly-roundup-template.md
- [ ] Calculate all performance metrics
- [ ] Identify hot/cold streaks
- [ ] Document lessons learned

PHASE 2: PLAYER TIER REVIEW (10-15 min)
- [ ] Review Foundation Anchors (Tier 1) - any downgrades?
- [ ] Review Correlation Zone (Tier 2) - any movement?
- [ ] Review Value Plays (Tier 3) - any promotions?
- [ ] Review Lottery Tickets (Tier 4) - any promotions?
- [ ] Update nhl/tier1-stars.md if needed
- [ ] Update nhl/tier2-players.md if needed
- [ ] Log any tier transitions

PHASE 3: TEAM DNA REFRESH (15-20 min)
- [ ] Update L5 stats for teams bet on this week
- [ ] Add hot/cold streak flags where applicable
- [ ] Update goalie notes if changes
- [ ] Add any new targeting profile insights
- [ ] Update protocol trigger flags

PHASE 4: ARCHIVE CLEANUP (5 min)
- [ ] Move research files >7 days to archive
- [ ] Move analysis files >14 days to archive
- [ ] Delete any temporary/scratch files

PHASE 5: WEEK AHEAD PREP (5-10 min)
- [ ] Review upcoming schedule for target teams
- [ ] Note any B2B situations for the week
- [ ] Identify key matchups to prioritize
- [ ] Set any new monitoring alerts

═══════════════════════════════════════════════════════════
COMPLETION TIME: ____________
NEXT UPDATE: Sunday, ____________
═══════════════════════════════════════════════════════════
```

---

## 7. FILE LOCATION REFERENCE

### Where Files Live

```
Sports-Betting/
├── protocols/
│   ├── APEXVIPER_*.md          # Core protocols (never archive)
│   └── daily-workflow.md       # Daily ops (never archive)
│
├── nhl/
│   ├── team-dna/
│   │   └── [team-name].md      # Update weekly, never archive
│   ├── tier1-stars.md          # Update weekly, never archive
│   └── tier2-players.md        # Update weekly, never archive
│
├── tracking/
│   ├── bankroll.md             # Daily updates, never archive
│   ├── bet-log.md              # Continuous, never archive
│   ├── lessons-learned.md      # Continuous, never archive
│   └── weekly-roundup-template.md  # Weekly, save copies
│
├── research/
│   └── [date]-*.md             # Archive after 7-14 days
│
└── archive/
    ├── research/[YYYY-MM]/     # Archived research
    ├── analysis/[YYYY-MM]/     # Archived analysis
    └── team-intel/[YYYY-MM]/   # Archived team intel
```

### File Update Responsibilities

| File Type | Who Updates | When |
|-----------|-------------|------|
| Protocols | System review only | Rarely (after testing) |
| Team DNA | Weekly roundup process | Every Sunday |
| Player Tiers | Weekly roundup process | Every Sunday |
| Bet Log | After each betting session | Daily when betting |
| Bankroll | After bet settlement | Daily when betting |
| Research | During analysis | Daily when analyzing |

---

## 8. QUALITY CONTROL

### Before Committing Updates

- [ ] All changes reference source data (weekly roundup)
- [ ] No speculative claims without evidence
- [ ] Player tier changes have logged justification
- [ ] Team DNA updates include L5 stats
- [ ] Archive files moved to correct locations

### Update Log Template
```
UPDATE LOG - [DATE]
─────────────────────
Files Modified:
1. 
2. 
3. 

Changes Made:
- 
- 
- 

Source Data:
- Weekly Roundup: [date]
- Bet Log Entries: [date range]
- External Sources: [list]

Verified By: [name/agent]
```

---

## 🎯 CROSS-REFERENCE

This protocol integrates with:
- `tracking/weekly-roundup-template.md` - Primary data source
- `protocols/APEXVIPER_INTEL_UPDATE_PROTOCOL.md` - Detailed update workflow
- `nhl/team-dna/*.md` - Files being updated
- `nhl/tier1-stars.md` and `nhl/tier2-players.md` - Player files

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Systematic process for keeping encyclopedia files current and accurate.
