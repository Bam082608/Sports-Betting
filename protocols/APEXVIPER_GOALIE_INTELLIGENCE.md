# 🥅 APEXVIPER GOALIE INTELLIGENCE v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Apply goalie-based analysis to every NHL betting decision.

---

## 1. THE BACKUP GOALIE LAW
**The Law:** Teams starting backup goalies in high-stress situations are vulnerable.

**Definition of Backup Situations:**
- Starter resting on back-to-back
- Starter injured/ill (day-to-day)
- Load management in condensed schedule
- Scheduled rest for veteran goalies

**Action Rule:** When team starts backup goalie:
- **EVALUATE:** Backup quality (Strong vs Weak tier)
- **TARGET:** Opponent team total overs
- **CONSIDER:** Full-game overs if both teams have backup

---

## 2. STRESS CONDITIONS (Auto-Fade Triggers)

### High-Stress Indicators
| Condition | Impact | Action |
|-----------|--------|--------|
| **Back-to-Back** | Fatigue + backup likely | Check starting goalie |
| **Recent Injury** | Rust + confidence issues | Fade team |
| **Poor GSAx (Goals Saved Above Expected)** | Technical decline | Target overs |
| **Heavy Workload (65+ games prior season)** | Cumulative fatigue | Monitor closely |

### Stress Calculation
```
Stress Score = B2B Factor + Injury Factor + GSAx Factor + Workload Factor

Where:
- B2B Factor: +2 if second game of B2B
- Injury Factor: +2 if returning from injury within 2 weeks
- GSAx Factor: +1 if negative GSAx last 10 games
- Workload Factor: +1 if 65+ starts prior season

Score ≥ 4: High stress - Fade heavily
Score 2-3: Moderate stress - Proceed with caution
Score < 2: Normal - Standard analysis
```

---

## 3. STRONG/WEAK BACKUP FRAMEWORK

### Strong Backups (Trust in Spot Starts)
| Team | Backup | Notes |
|------|--------|-------|
| **VGK** | Hill/Thompson | System team, backups succeed |
| **COL** | Various | Strong team in front reduces load |
| **FLA** | Knight | High-quality backup |
| **CAR** | Various | Elite defense supports any goalie |
| **NJ** | Various | Defensive structure compensates |

### Weak Backups (Target for Overs)
| Team | Backup | Notes |
|------|--------|-------|
| **WPG** | Comrie | Massive drop from Hellebuyck |
| **BOS** | Korpisalo | Significant drop from Swayman |
| **MIN** | Gustavsson issues | When Fleury not available |
| **TOR** | Various | High-event regardless of goalie |
| **EDM** | Various | Skinner dependency apparent |

---

## 4. THE VARIANCE VOID (System Goalie Rule)
**Cross-Reference:** `APEXVIPER_MACRO_INTELLIGENCE.md` Section 3: THE "VARIANCE VOID" (Goalie Injury Rule)

**The Concept:** Elite "System Goalies" define team identity.

**System Goalies (Identity-Defining):**
- Connor Hellebuyck (WPG)
- Jeremy Swayman (BOS)
- Igor Shesterkin (NYR)
- Ilya Sorokin (NYI)
- Stuart Skinner (EDM)
- Juuse Saros (NAS/TOR)

**When System Goalie OUT:**
- **DO NOT** just adjust line by pennies
- **FADE THE STRUCTURE** - Defense collapses without trust
- **TARGET:** Full-game overs, opponent team totals

---

## 5. GOALIE CONFIRMATION PROTOCOL

### Daily Verification (MANDATORY)
1. **Source:** DailyFaceoff.com (starting goalies page)
2. **Timing:** Confirm 2-3 hours before puck drop
3. **Backup:** Twitter beat reporters for late changes

### What to Verify
- [ ] Starting goalie confirmed
- [ ] Is it starter or backup?
- [ ] Any injury designations?
- [ ] Back-to-back situation?
- [ ] Recent performance (GSAx last 5)

---

## 6. INTEGRATION WITH BETTING DECISIONS

### Goalie Matrix Decision Tree
```
Is starter confirmed?
├── YES → Check stress factors
│   ├── Stress Score < 2 → Normal betting approach
│   ├── Stress Score 2-3 → Reduce exposure, consider hedges
│   └── Stress Score ≥ 4 → Fade team or target overs
└── NO (Backup starting)
    ├── Strong Backup → Proceed with caution
    └── Weak Backup → Target opponent/game overs
```

---

## 🎯 ACTION ITEMS

### Pre-Bet Checklist (Goalie)
- [ ] Verify starting goalie via DailyFaceoff
- [ ] Calculate stress score for starter
- [ ] Identify if backup situation
- [ ] Classify backup quality (Strong/Weak)
- [ ] Adjust betting approach accordingly

### Future Tracking Reference
- Document goalie performance in `research/goalie-tracking.md`
- Track backup performance against spread
- Monitor GSAx trends for system goalies

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Systematically incorporate goalie intelligence into every NHL bet.
