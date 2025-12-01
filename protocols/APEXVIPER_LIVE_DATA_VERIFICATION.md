# 📋 APEXVIPER LIVE DATA VERIFICATION CHECKLIST v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Comprehensive pre-game verification for NHL betting executed 2-3 hours before puck drop.

---

## 1. VERIFICATION TIMING SCHEDULE

| Time Before Puck Drop | Action | Priority |
|-----------------------|--------|----------|
| **3 hours** | Initial goalie check | 🟡 Medium |
| **2-2.5 hours** | Morning skate confirmation | 🔴 High |
| **1.5-2 hours** | Final line combinations | 🔴 High |
| **1 hour** | Injury report refresh | 🔴 High |
| **30 minutes** | Final confirmation sweep | 🔴 Critical |

**Data Cutoff Rule:** Information retrieved more than 3 hours before puck drop is considered STALE and must be re-verified.

---

## 2. GOALIE CONFIRMATION SOURCES

### Primary Source: DailyFaceoff
**URL:** `https://www.dailyfaceoff.com/starting-goalies/`

- [ ] Goalie listed as "Confirmed" (not "Expected" or "Unconfirmed")
- [ ] Timestamp on confirmation is from today
- [ ] Note backup goalie name for reference

### Secondary Source: NHL.com
**URL:** `https://www.nhl.com/news`

- [ ] Check team-specific news sections
- [ ] Look for "projected lineup" articles

### Tertiary Source: Twitter Beat Writers
**Search Queries:**
```
[TEAM NAME] morning skate
[TEAM NAME] projected lineup
[TEAM NAME] starting goalie
[GOALIE NAME] starting
```

**Example Searches:**
- `"Panthers morning skate"` OR `"Florida Panthers goalie"`
- `"Oilers morning skate"` OR `"Stuart Skinner starting"`
- `"Jets morning skate"` OR `"Hellebuyck starting"`

---

## 3. INJURY REPORT VERIFICATION

### Primary Source: NHL.com Injury Report
**URL:** `https://www.nhl.com/news/injuries`

### Secondary Source: Team Beat Writers (Twitter)
**Search Queries:**
```
[TEAM NAME] injury update
[TEAM NAME] out tonight
[TEAM NAME] game time decision
[PLAYER NAME] status
```

### Injury Classification Quick Reference

| Status | Betting Impact | Action |
|--------|----------------|--------|
| **OUT** | High | Adjust all bets involving team |
| **GTD (Game Time Decision)** | Critical | Wait for confirmation before betting |
| **Day-to-Day** | Medium | Monitor closely pre-game |
| **IR** | Low | Already factored into lines |

---

## 4. LINE COMBINATION VERIFICATION

### Primary Source: DailyFaceoff Line Combos
**URL:** `https://www.dailyfaceoff.com/teams/[team-name]/line-combinations/`

**Replace [team-name] with:**
- `anaheim-ducks`, `boston-bruins`, `buffalo-sabres`, etc.

### Verification Checklist
- [ ] Top line (1st line) unchanged from expected
- [ ] Power Play Unit 1 unchanged
- [ ] Target player on expected line
- [ ] Target player on expected PP unit

---

## 5. TWITTER BEAT WRITER SEARCH STRINGS

### Team-Specific Search Templates

| Team | Search String |
|------|---------------|
| **ANA** | `Ducks morning skate` OR `Anaheim lineup` |
| **ARI/UTA** | `Utah Hockey morning skate` OR `Utah lineup` |
| **BOS** | `Bruins morning skate` OR `Boston lineup` |
| **BUF** | `Sabres morning skate` OR `Buffalo lineup` |
| **CGY** | `Flames morning skate` OR `Calgary lineup` |
| **CAR** | `Hurricanes morning skate` OR `Carolina lineup` |
| **CHI** | `Blackhawks morning skate` OR `Chicago lineup` |
| **COL** | `Avalanche morning skate` OR `Colorado lineup` |
| **CBJ** | `Blue Jackets morning skate` OR `Columbus lineup` |
| **DAL** | `Stars morning skate` OR `Dallas lineup` |
| **DET** | `Red Wings morning skate` OR `Detroit lineup` |
| **EDM** | `Oilers morning skate` OR `Edmonton lineup` |
| **FLA** | `Panthers morning skate` OR `Florida lineup` |
| **LAK** | `Kings morning skate` OR `LA Kings lineup` |
| **MIN** | `Wild morning skate` OR `Minnesota lineup` |
| **MTL** | `Canadiens morning skate` OR `Montreal lineup` |
| **NSH** | `Predators morning skate` OR `Nashville lineup` |
| **NJD** | `Devils morning skate` OR `New Jersey lineup` |
| **NYI** | `Islanders morning skate` OR `New York Islanders lineup` |
| **NYR** | `Rangers morning skate` OR `New York Rangers lineup` |
| **OTT** | `Senators morning skate` OR `Ottawa lineup` |
| **PHI** | `Flyers morning skate` OR `Philadelphia lineup` |
| **PIT** | `Penguins morning skate` OR `Pittsburgh lineup` |
| **SJS** | `Sharks morning skate` OR `San Jose lineup` |
| **SEA** | `Kraken morning skate` OR `Seattle lineup` |
| **STL** | `Blues morning skate` OR `St Louis lineup` |
| **TBL** | `Lightning morning skate` OR `Tampa Bay lineup` |
| **TOR** | `Maple Leafs morning skate` OR `Toronto lineup` |
| **VAN** | `Canucks morning skate` OR `Vancouver lineup` |
| **VGK** | `Golden Knights morning skate` OR `Vegas lineup` |
| **WSH** | `Capitals morning skate` OR `Washington lineup` |
| **WPG** | `Jets morning skate` OR `Winnipeg lineup` |

---

## 6. RED FLAG ABORT TRIGGERS

### 🚨 IMMEDIATE BET ABORTION (No Questions Asked)

| Red Flag | Action |
|----------|--------|
| **Last-minute goalie change** (within 1 hour of puck drop) | ABORT all team props |
| **Star player scratch** (top-6 forward, top-4 D) | ABORT all player props for that team |
| **Multiple injuries** (2+ not reflected in lines) | ABORT entire game exposure |
| **Line combinations drastically changed** | ABORT player props, reassess |
| **Goalie still "Unconfirmed"** (within 1 hour) | ABORT goalie-dependent bets |

### 🟡 CAUTION FLAGS (Proceed With Reduced Exposure)

| Caution Flag | Action |
|--------------|--------|
| GTD player not yet confirmed | Reduce stake by 50% |
| Backup goalie for favored team | Reassess team totals |
| Morning skate info conflicting | Wait for clarification |
| Line shuffling (not drastic) | Verify target player position |

---

## 7. PRE-GAME VERIFICATION MASTER CHECKLIST

Execute this checklist 2-3 hours before puck drop for EACH game you're betting:

### Game: _____________ vs _____________ | Time: _______

**GOALIE VERIFICATION**
- [ ] Away goalie confirmed on DailyFaceoff
- [ ] Home goalie confirmed on DailyFaceoff
- [ ] Backup situation identified (if any)
- [ ] Goalie confirmation timestamp noted

**INJURY VERIFICATION**
- [ ] NHL.com injury report checked
- [ ] No new GTD designations
- [ ] No surprise scratches on Twitter
- [ ] All target players confirmed active

**LINE COMBINATION VERIFICATION**
- [ ] Away team lines unchanged
- [ ] Home team lines unchanged
- [ ] Target players on expected lines
- [ ] PP units unchanged

**FINAL SWEEP (30 min pre-game)**
- [ ] Re-check Twitter for late scratches
- [ ] Confirm no line movement red flags
- [ ] All systems GO for bet placement

---

## 8. DATA SOURCE RELIABILITY TIERS

| Tier | Source | Reliability | Use Case |
|------|--------|-------------|----------|
| **Tier 1** | DailyFaceoff Confirmed | 95%+ | Primary goalie/lineup source |
| **Tier 1** | NHL.com Official | 95%+ | Injury reports, official news |
| **Tier 2** | Beat Writer Twitter | 85-90% | Real-time updates, morning skate |
| **Tier 2** | Team Official Twitter | 85-90% | Lineup confirmations |
| **Tier 3** | Reddit/Forums | 60-70% | Early rumors only, must verify |
| **Tier 3** | Betting Twitter | 60-70% | Line movement intel only |

**Rule:** Never bet based on Tier 3 sources alone. Always verify with Tier 1 or Tier 2.

---

## 9. QUICK VERIFICATION WORKFLOW

```
┌─────────────────────────────────────────────┐
│ STEP 1: Open DailyFaceoff Starting Goalies  │
│         Note: Confirmed vs Expected         │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│ STEP 2: Search Twitter for Morning Skate    │
│         "[TEAM] morning skate"              │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│ STEP 3: Check NHL.com Injury Report         │
│         Note any GTD or new OUT             │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│ STEP 4: Verify Line Combinations            │
│         DailyFaceoff team page              │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│ STEP 5: Red Flag Check                      │
│         Any abort triggers present?         │
└────────────────────┬────────────────────────┘
                     │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
    ┌───────────┐       ┌───────────┐
    │  YES      │       │   NO      │
    │  ABORT    │       │ PROCEED   │
    │  BET      │       │ TO BET    │
    └───────────┘       └───────────┘
```

---

## 🎯 CROSS-REFERENCE

This protocol integrates with:
- `protocols/APEXVIPER_GOALIE_INTELLIGENCE.md`
- `protocols/APEXVIPER_GAME_ANALYSIS_PROTOCOL.md`
- `protocols/daily-workflow.md`

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Ensure all NHL bets are placed with verified, current information.
