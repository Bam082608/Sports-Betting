# 🖥️ NHL Surveillance System

**Real-Time Odds Monitoring & Game Intelligence Dashboards**

The NHL Surveillance System provides comprehensive HTML-based dashboards for live odds monitoring, line movement tracking, and game-specific intelligence gathering across multiple sportsbooks.

**Last Updated:** December 3, 2025  
**Total Dashboards:** 13 HTML files (8 root + 5 surveillance/)  
**Technology:** HTML5 + JavaScript (vanilla)

---

## 📑 Table of Contents

- [System Overview](#system-overview)
- [Surveillance Hub](#surveillance-hub)
- [Dashboard Inventory](#dashboard-inventory)
- [Dashboard Features](#dashboard-features)
- [Usage Guide](#usage-guide)
- [Integration with Betting Workflow](#integration-with-betting-workflow)

---

## 🎯 System Overview

### Purpose

The Surveillance System enables:
1. **Real-time odds monitoring** across multiple sportsbooks
2. **Line movement detection** and value identification
3. **Game-specific intelligence** tracking for individual matchups
4. **Multi-book comparison** for line shopping
5. **Historical odds reference** and pattern recognition

### Technology Stack

- **Frontend:** HTML5 + Vanilla JavaScript
- **Data Sources:** Manual entry / API integration (where available)
- **Refresh:** Real-time or manual refresh depending on implementation
- **Compatibility:** Any modern web browser

### Surveillance Locations

**Primary Surveillance (Root /nhl/):**
- 8 dashboard files including main hub and odds tracker
- Accessible directly from `/nhl/` directory
- Includes primary odds surveillance tool (v2)

**Additional Surveillance (/nhl/surveillance/):**
- 5 game-specific dashboard files
- Organized in dedicated surveillance subdirectory
- Complements root-level dashboards

---

## 🏠 Surveillance Hub

### index.html

**Location:** `/nhl/index.html`  
**Size:** 3,258 bytes  
**Purpose:** Main entry point and navigation hub for surveillance system

**Features:**
- Quick links to all surveillance dashboards
- Game schedule overview
- Surveillance tool selector
- Direct access to odds-surveillance-v2.html

**Use When:**
- Starting game day surveillance
- Need to quickly access specific game dashboard
- Want overview of available surveillance tools

**Typical Workflow:**
```
1. Open /nhl/index.html in browser
2. Review today's game schedule
3. Click link to specific game dashboard or odds tracker
4. Keep index.html open in separate tab for quick navigation
```

---

## 📊 Dashboard Inventory

### Primary Odds Tracker

#### odds-surveillance-v2.html (Enhanced Version)

**Location:** `/nhl/odds-surveillance-v2.html`  
**Size:** 16,532 bytes  
**Version:** 2.0 (Enhanced)  
**Status:** Primary odds monitoring tool

**Features:**
- Multi-sportsbook odds comparison
- Line movement alerts and highlighting
- Value bet identification
- Historical line tracking
- Opening vs. current line comparison
- Public betting percentage integration (if available)

**Supported Markets:**
- Moneyline
- Puck Line / Spread
- Game Totals (Over/Under)
- Player Props (SOG, Points, etc.)

**Recommended Usage:**
- Keep open throughout entire game day
- Refresh at regular intervals (15-30 minutes)
- Monitor before bet placement for line shopping
- Check after bet placement to verify you got best available line

**Sportsbooks Tracked:**
- DraftKings
- FanDuel
- BetMGM
- Caesars
- Other major books (varies by implementation)

---

### Game-Specific Dashboards (Root /nhl/)

Located in `/nhl/` directory - 6 matchup-specific surveillance tools:

#### bos-det-surveillance.html
**Matchup:** Boston Bruins @ Detroit Red Wings  
**Size:** 21,275 bytes (Largest dashboard)  
**Features:**
- Detailed BOS/DET team stats
- Player prop markets for both teams
- Goalie matchup analysis
- Historical head-to-head data
- Key injury updates
- Line combination tracking

**Use When:** Analyzing or betting on Bruins vs. Red Wings matchups

---

#### cgy-nsh-surveillance.html
**Matchup:** Calgary Flames @ Nashville Predators  
**Size:** 12,990 bytes  
**Features:**
- CGY/NSH team statistics
- Western Conference matchup analysis
- Special teams comparison
- Travel/rest factors

**Use When:** Analyzing or betting on Flames vs. Predators matchups

---

#### min-edm-surveillance.html
**Matchup:** Minnesota Wild @ Edmonton Oilers  
**Size:** 15,315 bytes  
**Features:**
- MIN/EDM team analytics
- Connor McDavid prop tracking (if EDM)
- Goalie situation for both teams
- Recent performance trends

**Use When:** Analyzing or betting on Wild vs. Oilers matchups

---

#### tor-fla-surveillance.html
**Matchup:** Toronto Maple Leafs @ Florida Panthers  
**Size:** 15,491 bytes  
**Features:**
- TOR/FLA matchup intelligence
- High-profile player prop markets
- Playoff implications (if applicable)
- Atlantic Division context

**Use When:** Analyzing or betting on Maple Leafs vs. Panthers matchups

---

#### van-col-surveillance.html
**Matchup:** Vancouver Canucks @ Colorado Avalanche  
**Size:** 14,471 bytes  
**Features:**
- VAN/COL team analysis
- **Altitude Edge factors** (Ball Arena - 5,280 ft)
- Avalanche home performance metrics
- Visiting team fatigue assessment

**Use When:** 
- Analyzing or betting on Canucks vs. Avalanche matchups
- **CRITICAL:** Reference when using APEXVIPER_ALTITUDE_EDGE.md protocol

---

#### wsh-la-surveillance.html
**Matchup:** Washington Capitals @ Los Angeles Kings  
**Size:** 25,227 bytes (Second largest dashboard)  
**Features:**
- WSH/LA comprehensive analysis
- Cross-conference matchup intelligence
- West coast travel factor (if WSH traveling)
- Time zone impact assessment

**Use When:** Analyzing or betting on Capitals vs. Kings matchups

---

### Additional Surveillance Tools (/nhl/surveillance/)

Located in `/nhl/surveillance/` subdirectory - 5 additional dashboards:

#### chi-vgk-surveillance.html
**Matchup:** Chicago Blackhawks @ Vegas Golden Knights  
**Size:** 8,949 bytes  
**Features:** CHI/VGK matchup tracking

---

#### dal-nyr-surveillance.html
**Matchup:** Dallas Stars @ New York Rangers  
**Size:** 9,545 bytes  
**Features:** DAL/NYR matchup tracking

---

#### ott-mtl-surveillance.html
**Matchup:** Ottawa Senators @ Montreal Canadiens  
**Size:** 657 bytes (Minimal)  
**Status:** Basic template - needs expansion

---

#### tb-nyi-surveillance.html
**Matchup:** Tampa Bay Lightning @ New York Islanders  
**Size:** 662 bytes (Minimal)  
**Status:** Basic template - needs expansion

---

#### wsh-la-surveillance.html
**Matchup:** Washington Capitals @ Los Angeles Kings  
**Size:** 8,587 bytes  
**Note:** Duplicate of root-level wsh-la dashboard (different version/size)

---

## 🔧 Dashboard Features

### Common Features (All Dashboards)

**Pre-Game Intelligence:**
- Team statistics comparison
- Recent form (last 5-10 games)
- Head-to-head history
- Injury reports
- Starting goalie confirmation
- Line combinations

**Live Odds Tracking:**
- Current odds from multiple books
- Opening line reference
- Line movement indicators
- Best available odds highlighting
- Arbitrage opportunity detection

**Player Props:**
- Key player prop markets (SOG, Points, etc.)
- Tier 1/2 player identification
- Historical prop performance
- Prop line comparison across books

**Situational Factors:**
- Home/away performance
- Rest days / back-to-backs
- Travel distance
- Time zone changes
- Special circumstances

### Enhanced Features (Select Dashboards)

**odds-surveillance-v2.html Exclusive:**
- Multi-game slate view
- Sortable odds tables
- Custom alert configuration
- Historical line charts
- Value bet calculator

**Larger Dashboards (15KB+):**
- Extended statistical analysis
- Advanced metrics integration
- Multiple market types
- Detailed goalie statistics
- Special teams breakdown

---

## 📖 Usage Guide

### Game Day Setup

**Step 1: Open Primary Surveillance**
```
1. Open browser
2. Navigate to /nhl/index.html
3. Open /nhl/odds-surveillance-v2.html in new tab
```

**Step 2: Identify Priority Games**
```
1. Use protocols/APEXVIPER_MULTI_GAME_TRIAGE.md
2. Note 2-3 priority games for the slate
```

**Step 3: Open Game-Specific Dashboards**
```
For each priority game:
1. Open corresponding surveillance dashboard
2. Example: For TOR @ FLA, open tor-fla-surveillance.html
3. Arrange browser tabs for easy switching
```

**Step 4: Monitor Throughout Day**
```
1. Refresh odds-surveillance-v2.html every 15-30 minutes
2. Check game-specific dashboards before deep analysis
3. Update as late-breaking news emerges (injuries, goalies)
```

### Pre-Bet Verification Workflow

**Using Surveillance for Final Checks:**
```
1. Identify target bet from analysis
2. Open odds-surveillance-v2.html
3. Verify current odds across all books
4. Select best available line
5. Open game-specific dashboard
6. Double-check goalie confirmation
7. Verify no late scratches/injuries
8. Execute bet at best odds
```

### Line Shopping Process

**Finding Best Value:**
```
1. Note your target bet (e.g., Player X Over 3.5 SOG)
2. Check odds-surveillance-v2.html for line across books:
   - DraftKings: -115
   - FanDuel: -110
   - BetMGM: -120
3. Identify FanDuel as best value (-110)
4. Place bet at FanDuel
5. Document in tracking/bet-log.md
```

### Monitoring Line Movement

**Detecting Market Shifts:**
```
1. Note opening line in surveillance dashboard
2. Monitor for significant movement (10+ cents or line change)
3. Investigate cause:
   - Injury news?
   - Sharp money?
   - Public heavy on one side?
4. Apply APEXVIPER_PUBLIC_MONEY.md protocol if applicable
5. Adjust betting strategy accordingly
```

---

## 🔄 Integration with Betting Workflow

### Protocol Integration Points

**With APEXVIPER_GAME_ANALYSIS_PROTOCOL.md:**
```
1. Use surveillance dashboard to gather current team stats
2. Reference goalie confirmations
3. Check injury updates in real-time
4. Verify line combinations match expected
```

**With APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md:**
```
1. Open surveillance tools as part of execution setup
2. Use for final odds verification before bet placement
3. Line shop across books shown in odds tracker
4. Document actual odds obtained
```

**With APEXVIPER_ALTITUDE_EDGE.md:**
```
1. Open van-col-surveillance.html for Colorado games
2. Reference altitude-specific metrics
3. Check visiting team travel and rest factors
4. Apply altitude adjustments to totals/props
```

**With APEXVIPER_GOALIE_CONFIRMATION.md:**
```
1. Check game-specific dashboard for goalie updates
2. Cross-reference with official team sources
3. Update confidence level in protocol
4. Adjust bets if goalie change detected
```

### Daily Workflow Integration

**Morning (10:00 AM - 12:00 PM):**
```
1. Open index.html to see today's games
2. Open odds-surveillance-v2.html
3. Check opening lines for all games
4. Note any unusual line movements overnight
```

**Afternoon (2:00 PM - 4:00 PM):**
```
1. Refresh odds-surveillance-v2.html
2. Monitor for line movement
3. Open game-specific dashboards for priority games
4. Begin detailed analysis with fresh data
```

**Pre-Game (1-2 hours before first puck drop):**
```
1. Final refresh of all surveillance tools
2. Confirm starting goalies in dashboards
3. Check for last-minute scratches
4. Verify odds one final time before execution
5. Execute bets with best available lines
```

**Live/In-Game (Optional):**
```
1. Monitor odds for live betting opportunities
2. Track game flow vs. pre-game expectations
3. Document observations for post-game analysis
```

---

## 📊 Surveillance System Statistics

**Current Coverage:**
- ✅ 1 primary surveillance hub (index.html)
- ✅ 1 enhanced odds tracker (odds-surveillance-v2.html)
- ✅ 6 detailed game-specific dashboards (root)
- ✅ 5 additional game dashboards (surveillance/)
- ✅ 13 total HTML surveillance tools

**Dashboard Status:**
- 11 fully functional (84.6%)
- 2 minimal templates (15.4%)

**Planned Enhancements:**
- Expand ott-mtl-surveillance.html
- Expand tb-nyi-surveillance.html
- Resolve wsh-la duplicate dashboard
- Add automated data refresh (API integration)

---

## 🔗 Related Documentation

| Topic | Location |
|-------|----------|
| **NHL System Overview** | [/nhl/README.md](/nhl/README.md) |
| **Odds Analysis Protocol** | [/protocols/APEXVIPER_PUBLIC_MONEY.md](/protocols/APEXVIPER_PUBLIC_MONEY.md) |
| **Goalie Confirmation** | [/protocols/APEXVIPER_GOALIE_CONFIRMATION.md](/protocols/APEXVIPER_GOALIE_CONFIRMATION.md) |
| **Live Data Verification** | [/protocols/APEXVIPER_LIVE_DATA_VERIFICATION.md](/protocols/APEXVIPER_LIVE_DATA_VERIFICATION.md) |
| **Execution Protocol** | [/protocols/APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md](/protocols/APEXVIPER_ADHD_EXECUTION_PROTOCOL_v3.2.0.md) |
| **Root Documentation** | [/README.md](/README.md) |

---

## 🛠️ Technical Notes

### Browser Compatibility
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Internet Explorer (Not supported)

### Performance Recommendations
- Use modern browser with JavaScript enabled
- Keep no more than 5-6 surveillance tabs open simultaneously
- Refresh manually rather than auto-refresh to control bandwidth
- Close unused dashboards to maintain browser performance

### Local Usage
All dashboards can be opened directly from local file system:
```
file:///[path-to-repo]/nhl/index.html
file:///[path-to-repo]/nhl/odds-surveillance-v2.html
```

---

*Last Updated: December 3, 2025*  
*Surveillance System Version: 2.0*  
*13 active dashboards • Real-time odds monitoring enabled*