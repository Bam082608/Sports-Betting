# 😴 APEXVIPER FATIGUE MATRIX v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Identify and exploit fatigue-based edges in NHL scheduling.

---

## 1. THE BACK-TO-BACK (B2B) LAW
**The Law:** Teams playing second game of back-to-back are physically compromised.

**Why It Works:**
- 82-game season = compressed recovery windows
- Travel between games compounds fatigue
- Backup goalie situations more common
- Reduced special teams effectiveness

**B2B Verification:**
- Check yesterday's schedule
- Identify teams that played last night
- Note travel distance (same city vs cross-country)

---

## 2. AUTO-FADE TEAMS (B2B Specialists)
**The Law:** These teams perform significantly worse on B2B rest.

| Team | Why They Struggle | B2B Action |
|------|-------------------|------------|
| **CAR** | High-event system requires energy | FADE |
| **BOS** | Older roster, slower recovery | FADE |
| **TOR** | High-pressure market compounds fatigue | FADE |
| **PIT** | Aging core (Crosby, Malkin, Letang) | FADE |
| **WPG** | Hellebuyck dependency + fatigue = issues | FADE |

**Auto-Fade Protocol:**
When these teams are on B2B second game:
- ✅ **TARGET:** Opponent spread/ML
- ✅ **CONSIDER:** Unders (tired = low event)
- ❌ **AVOID:** Backing these teams as favorites

---

## 3. EXCEPTION TEAMS (B2B Resilient)
**The Law:** These teams maintain performance despite B2B scheduling.

| Team | Why They Handle B2B | B2B Action |
|------|---------------------|------------|
| **VGK** | Deep roster, system-dependent | TRUST |
| **COL** | Elite conditioning, altitude advantage | TRUST |
| **FLA** | Younger legs, warm weather recovery | TRUST |

**Exception Protocol:**
When these teams are on B2B second game:
- **NEUTRAL:** Don't auto-fade based on B2B alone
- **PROCEED:** Apply standard analysis
- **NOTE:** Still verify goalie situation

---

## 4. TRAVEL FATIGUE FACTORS

### Distance Multipliers
| Travel Type | Fatigue Impact | Adjustment |
|-------------|----------------|------------|
| **Same city B2B** | Minimal | Standard B2B analysis |
| **Same timezone** | Moderate | Add +1 to fatigue score |
| **Cross-timezone** | Significant | Add +2 to fatigue score |
| **Coast-to-coast** | Severe | Add +3 to fatigue score |

### Time Zone Challenges
- Eastern → Pacific: Jet lag, late games
- Pacific → Eastern: Early body clock
- International games: Maximum disruption

---

## 5. REST ADVANTAGE CALCULATION

### Rest Days Matrix
| Your Team Rest | Opponent Rest | Edge |
|----------------|---------------|------|
| 2+ days | B2B | STRONG advantage |
| 2+ days | 1 day | Moderate advantage |
| 1 day | B2B | Slight advantage |
| B2B | B2B | Neutral |
| B2B | 2+ days | STRONG disadvantage |

### Fatigue Score Formula
```
Fatigue Score = Days Since Last Game + Travel Factor + B2B Factor

Where:
- Days Since Last Game: 0 (B2B), 1 (1 day), 2+ (well rested)
- Travel Factor: 0 (home), 1 (short travel), 2-3 (long travel)
- B2B Factor: -2 if Auto-Fade team on B2B

Score Interpretation:
≤ 0: Heavy fatigue - FADE
1-2: Moderate fatigue - Cautious
3+: Well rested - SUPPORT
```

---

## 6. SCHEDULE SPOT ANALYSIS

### Favorable Spots (BET INTO)
- Team off 2+ days rest at home
- Team after loss with revenge narrative + rest
- Team's only game this week (extra prep)

### Unfavorable Spots (FADE)
- 3rd game in 4 nights
- 4th game in 6 nights
- B2B with cross-country travel
- Back-to-back-to-back (rare but deadly)

---

## 7. INTEGRATION WITH MACRO INTELLIGENCE
**Cross-Reference:** `APEXVIPER_MACRO_INTELLIGENCE.md` Section 2: THE "OLYMPIC SQUEEZE" (Fatigue Protocol)

### The Olympic Squeeze Connection
- 2024-25 schedule compressed for 2026 Olympics
- More B2B situations than normal
- "Schedule losses" more pronounced this season

### Combined Application
```
IF: Auto-Fade Team + B2B + Travel
THEN: Strong FADE signal

IF: Exception Team + B2B + Home
THEN: Neutral / Proceed with standard analysis

IF: Any Team + 3-in-4 nights
THEN: FADE regardless of team quality
```

---

## 🎯 ACTION ITEMS

### Pre-Bet Checklist (Fatigue)
- [ ] Check both teams' schedules (last game date)
- [ ] Identify any B2B situations
- [ ] Calculate travel distance if applicable
- [ ] Cross-reference against Auto-Fade/Exception lists
- [ ] Calculate Fatigue Score differential

### Future Tracking Reference
- Document B2B results in `research/b2b-results.md`
- Track Auto-Fade team performance
- Monitor Exception team B2B resilience

---

## 8. QUICK REFERENCE

### B2B Quick Decision Matrix
```
Auto-Fade Team on B2B → FADE (high confidence)
Exception Team on B2B → NEUTRAL (standard analysis)
Any Team on 3-in-4 → FADE (automatic)
Team off 3+ days rest → SUPPORT (fresh legs)
```

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Systematically identify and exploit schedule-based fatigue edges.
