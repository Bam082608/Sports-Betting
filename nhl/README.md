# 🏒 NHL Betting Intelligence System

**APEXVIPER Primary Operational Theater**

The NHL subsystem is the flagship betting intelligence platform of APEXVIPER Genesis, featuring comprehensive team analysis, live surveillance tools, tier-based player tracking, and multi-layered intelligence gathering.

**Last Updated:** December 3, 2025  
**Status:** Active Production System  
**Coverage:** 32 NHL teams • 8+ surveillance dashboards • 34 team profiles

---

## 📑 Table of Contents

- [System Overview](#system-overview)
- [Directory Structure](#directory-structure)
- [HTML Surveillance Tools](#html-surveillance-tools)
- [Team DNA System](#team-dna-system)
- [Player Tier System](#player-tier-system)
- [Daily Intelligence](#daily-intelligence)
- [Data Infrastructure](#data-infrastructure)
- [Quick Start Guide](#quick-start-guide)

---

## 🎯 System Overview

### Primary Focus Areas
1. **Player Props** - SOG (Shots on Goal) totals with tier-based tracking
2. **Game Totals** - Over/under with goalie and offensive matchup analysis
3. **Team Situational Spots** - B2B, home/away, fatigue factors

### Key Differentiators
- **Live Surveillance:** Custom HTML dashboards for real-time odds monitoring
- **Team DNA Profiles:** 34 comprehensive team analysis files
- **Tier-Based Player System:** Elite (Tier 1) vs. selective (Tier 2) player tracking
- **Multi-Source Intel:** Encyclopedia integration, daily research, statistical databases

---

## 📁 Directory Structure

```
nhl/
├── README.md                           # This file
│
├── *.html (8 files)                    # Live surveillance dashboards
│   ├── index.html                      # Main surveillance hub
│   ├── odds-surveillance-v2.html       # Enhanced odds tracker
│   ├── bos-det-surveillance.html       # Game-specific trackers (6 files)
│   ├── cgy-nsh-surveillance.html
│   ├── min-edm-surveillance.html
│   ├── tor-fla-surveillance.html
│   ├── van-col-surveillance.html
│   └── wsh-la-surveillance.html
│
├── surveillance/                       # Additional surveillance tools
│   ├── README.md                       # Surveillance system docs
│   ├── chi-vgk-surveillance.html
│   ├── dal-nyr-surveillance.html
│   ├── ott-mtl-surveillance.html
│   ├── tb-nyi-surveillance.html
│   └── wsh-la-surveillance.html
│
├── team-dna/                           # Team profile system
│   ├── README.md                       # Team DNA documentation
│   ├── [team-name].md (32 teams)       # Individual team profiles
│   ├── shot-blocking-database.json     # Defensive metrics database
│   └── SHIN_PAD_EQUITY_REPORT_v3.3.md  # Shot-blocking analysis
│
├── daily-intel/                        # Game-day research
│   ├── README.md                       # Currently exists
│   └── YYYY-MM-DD-*.md                 # Dated intelligence files
│
├── data/                               # Statistical databases
│   └── [Data files]
│
├── encyclopedia/                       # NHL reference materials
│   └── [Reference content]
│
├── tier1-stars.md                      # Elite player tracking list
└── tier2-players.md                    # High-volume selective players
```

---

## 🖥️ HTML Surveillance Tools

### Primary Surveillance Hub

**index.html** - Main entry point for surveillance system
- Purpose: Central dashboard for accessing all surveillance tools
- Location: `/nhl/index.html`
- Features: Quick links to all game-specific trackers

### Enhanced Odds Tracker

**odds-surveillance-v2.html** - Advanced odds monitoring (v2)
- Purpose: Real-time odds tracking across multiple sportsbooks
- Location: `/nhl/odds-surveillance-v2.html`
- Features:
  - Multi-book comparison
  - Line movement alerts
  - Historical odds tracking
  - Value identification
- **Use:** Primary odds monitoring tool for all game days

### Game-Specific Surveillance Dashboards

Located in `/nhl/` root directory (6 dashboards):

| Dashboard | Matchup | Size | Purpose |
|-----------|---------|------|---------|
| **bos-det-surveillance.html** | Boston @ Detroit | 21,275 bytes | BOS/DET game tracking |
| **cgy-nsh-surveillance.html** | Calgary @ Nashville | 12,990 bytes | CGY/NSH game tracking |
| **min-edm-surveillance.html** | Minnesota @ Edmonton | 15,315 bytes | MIN/EDM game tracking |
| **tor-fla-surveillance.html** | Toronto @ Florida | 15,491 bytes | TOR/FLA game tracking |
| **van-col-surveillance.html** | Vancouver @ Colorado | 14,471 bytes | VAN/COL game tracking |
| **wsh-la-surveillance.html** | Washington @ LA | 25,227 bytes | WSH/LA game tracking |

**Features (Each Dashboard):**
- Pre-game team stats
- Player prop markets
- Live odds updates
- Goalie confirmations
- Injury updates
- Key matchup metrics

### Additional Surveillance Tools

Located in `/nhl/surveillance/` (5 additional dashboards):

| Dashboard | Matchup | Features |
|-----------|---------|----------|
| **chi-vgk-surveillance.html** | Chicago @ Vegas | 8,949 bytes |
| **dal-nyr-surveillance.html** | Dallas @ NY Rangers | 9,545 bytes |
| **ott-mtl-surveillance.html** | Ottawa @ Montreal | 657 bytes |
| **tb-nyi-surveillance.html** | Tampa Bay @ NY Islanders | 662 bytes |
| **wsh-la-surveillance.html** | Washington @ LA | 8,587 bytes (duplicate) |

**See:** [surveillance/README.md](/nhl/surveillance/README.md) for complete surveillance system documentation

---

## 🧬 Team DNA System

### Overview

The Team DNA system provides comprehensive team profiles for all 32 NHL teams, documenting:
- Offensive systems and tendencies
- Defensive structures
- Special teams effectiveness
- Coaching strategies
- Key players and depth charts
- Situational performance (home/away, B2B, etc.)

### Team Coverage

**Total Profiles:** 34 files (32 teams + 2 special files)

**All 32 NHL Teams:**
- Anaheim Ducks
- Boston Bruins
- Buffalo Sabres
- Calgary Flames
- Carolina Hurricanes
- Chicago Blackhawks
- Colorado Avalanche
- Columbus Blue Jackets
- Dallas Stars
- Detroit Red Wings
- Edmonton Oilers
- Florida Panthers
- Los Angeles Kings
- Minnesota Wild
- Montreal Canadiens
- Nashville Predators
- New Jersey Devils
- New York Islanders
- New York Rangers
- Ottawa Senators
- Philadelphia Flyers
- Pittsburgh Penguins
- San Jose Sharks
- Seattle Kraken
- St. Louis Blues
- Tampa Bay Lightning
- Toronto Maple Leafs
- Utah Hockey Club
- Vancouver Canucks
- Vegas Golden Knights
- Washington Capitals
- Winnipeg Jets

**Special Files:**
- `shot-blocking-database.json` - JSON database of defensive metrics
- `SHIN_PAD_EQUITY_REPORT_v3.3.md` - Shot-blocking analysis report (v3.3)

### Team DNA Template Structure

Each team profile follows a consistent structure:

```markdown
# [Team Name]

## Team Overview
*Last Updated: [Date]*

## APEXVIPER Betting Intelligence

### ⭐ Tier 1 Stars
[Elite players with detailed SOG metrics]

### Tier 2 Players
[High-volume selective players]

## Betting Strategy
[Team-specific betting approaches]

## Team Systems
[Offensive/defensive systems analysis]

## Key Situational Factors
[Home/away, B2B, travel considerations]

## Goalie Situation
[Starting goalie analysis and backup assessment]

## Notes
[Additional intelligence and patterns]
```

**See:** [team-dna/README.md](/nhl/team-dna/README.md) for complete team index and DNA template documentation

---

## ⭐ Player Tier System

APEXVIPER uses a two-tier system for player prop tracking based on SOG volume and consistency.

### Tier 1 Stars (Elite)

**Criteria:**
- Average 5+ SOG per game
- 25%+ shot concentration (% of team shots)
- Consistent performance across game states
- **Bet Every Game** with 2P+3P splits

**Stake Level:** Tier A ($2.50 per bet)

**Location:** `/nhl/tier1-stars.md`

**Current Tier 1 Players:** See [tier1-stars.md](/nhl/tier1-stars.md) for full list

**Example Tier 1 Profile:**
```
Cutter Gauthier (ANA)
- Average SOG: 8.0
- Concentration: 31%
- Hit Rate: ~85%
- Strategy: Bet every game, 2P+3P splits
```

### Tier 2 Players (High-Volume Selective)

**Criteria:**
- Average 3.5-4.9 SOG per game
- 18-24% shot concentration
- Good volume but situation-dependent
- **Selective Betting** - favorable matchups only

**Stake Level:** Tier B ($2.00 per bet) or lower depending on confidence

**Location:** `/nhl/tier2-players.md`

**Tier 2 Strategy:**
- Analyze matchup quality
- Check defensive opponent
- Verify line combinations
- Confirm power play time

**See:** [tier2-players.md](/nhl/tier2-players.md) for full list and betting guidelines

---

## 📰 Daily Intelligence

### Purpose

Game-day research files containing:
- Slate analysis and game prioritization
- Injury reports and lineup changes
- Goalie confirmations
- Situational factors (B2B, travel, etc.)
- Betting recommendations

### File Naming Convention

```
daily-intel/YYYY-MM-DD-[description].md

Examples:
- 2025-12-03-DAL-at-NJD.md (single game deep-dive)
- 2025-12-02-slate.md (full slate analysis)
- 2025-12-02_tuesday_7pm_slate.md (specific time slot)
```

### Current Intel Files

| File | Date | Coverage |
|------|------|----------|
| 2025-12-03-DAL-at-NJD.md | Dec 3 | Dallas @ New Jersey deep-dive |
| 2025-12-02-slate.md | Dec 2 | Full slate analysis |
| 2025-12-02_tuesday_7pm_slate.md | Dec 2 | Tuesday 7pm games |
| 2025-12-01_monday_slate.md | Dec 1 | Monday slate |
| 2025-12-01_WPG_at_BUF.md | Dec 1 | Winnipeg @ Buffalo |

**See:** [daily-intel/README.md](/nhl/daily-intel/README.md) for intel workflow and templates

---

## 💾 Data Infrastructure

### Shot-Blocking Database

**File:** `team-dna/shot-blocking-database.json`

**Purpose:** JSON database tracking defensive shot-blocking metrics by team

**Data Structure:**
```json
{
  "team": "Team Name",
  "blockers": [
    {
      "player": "Player Name",
      "blocks_per_game": X.X,
      "block_percentage": XX%
    }
  ]
}
```

**Use Cases:**
- Identifying defensive-minded teams that suppress SOG
- Player prop adjustments for shot-blocking heavy opponents
- Team total analysis

### SHIN PAD EQUITY Report

**File:** `team-dna/SHIN_PAD_EQUITY_REPORT_v3.3.md`  
**Version:** 3.3  
**Size:** 2,265 bytes

**Purpose:** Analysis of shot-blocking impact on betting markets

**Key Insights:**
- Shot-blocking leaders by team
- Impact on game totals
- Player prop adjustments for blocked shots
- High-blocking defensive pairings

---

## 🚀 Quick Start Guide

### For Game Day Analysis

**Step 1: Check Daily Intel**
```
1. Navigate to nhl/daily-intel/
2. Open today's slate file (YYYY-MM-DD-slate.md)
3. Review prioritized games and key factors
```

**Step 2: Open Surveillance**
```
1. Open nhl/odds-surveillance-v2.html in browser
2. Monitor line movements and odds
3. Open game-specific dashboards for priority games
```

**Step 3: Review Team DNA**
```
1. Navigate to nhl/team-dna/
2. Open profiles for both teams in target game
3. Check Tier 1/2 players and team systems
```

**Step 4: Check Player Tiers**
```
1. Review nhl/tier1-stars.md for "bet every game" players
2. Review nhl/tier2-players.md for selective opportunities
3. Cross-reference with daily intel matchup analysis
```

**Step 5: Apply Protocols**
```
1. Use protocols/APEXVIPER_GAME_ANALYSIS_PROTOCOL.md
2. Verify goalies via APEXVIPER_GOALIE_CONFIRMATION.md
3. Build portfolio via APEXVIPER_PORTFOLIO_CONSTRUCTION.md
```

### For Player Prop Research

**Finding Tier 1 Bets:**
```
1. Open nhl/tier1-stars.md
2. Check which Tier 1 players are playing tonight
3. Bet 2P+3P splits for all Tier 1 players (Tier A stakes)
4. Verify lines in odds-surveillance-v2.html
```

**Evaluating Tier 2 Opportunities:**
```
1. Open nhl/tier2-players.md
2. Check tonight's Tier 2 players
3. Navigate to team-dna for opponent defensive profile
4. Only bet if matchup is favorable
5. Use Tier B stakes or lower
```

### For Team Total Analysis

**Offensive Analysis:**
```
1. Check team-dna/[team].md for offensive system
2. Review tier lists for shot volume players
3. Check goalie matchup quality
4. Review daily-intel for situational factors
```

**Defensive Analysis:**
```
1. Check shot-blocking-database.json for defensive metrics
2. Review SHIN_PAD_EQUITY_REPORT_v3.3.md
3. Check opposing team's tier players
4. Factor in goalie quality
```

---

## 🔗 Related Documentation

| Topic | Location |
|-------|----------|
| **Protocol Suite** | [/protocols/README.md](/protocols/README.md) |
| **Team DNA System** | [/nhl/team-dna/README.md](/nhl/team-dna/README.md) |
| **Surveillance Tools** | [/nhl/surveillance/README.md](/nhl/surveillance/README.md) |
| **Daily Intel** | [/nhl/daily-intel/README.md](/nhl/daily-intel/README.md) |
| **Tracking System** | [/tracking/README.md](/tracking/README.md) |
| **Root Documentation** | [/README.md](/README.md) |

---

## 📊 NHL System Statistics

**Current Coverage:**
- ✅ 32/32 team profiles (100% coverage)
- ✅ 8 root-level surveillance dashboards
- ✅ 5 surveillance/ subdirectory dashboards
- ✅ 13 total HTML surveillance tools
- ✅ Tier 1 player list maintained
- ✅ Tier 2 player list maintained
- ✅ JSON shot-blocking database
- ✅ Active daily intel production

**System Health:** Fully Operational

---

*Last Updated: December 3, 2025*  
*NHL System Version: 1.0*  
*Primary APEXVIPER operational theater*