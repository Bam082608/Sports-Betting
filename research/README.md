# 🔬 AI Research Contributions System

**Multi-AI Collaborative Intelligence Framework**

The Research system manages contributions from multiple AI agents (Claude, Gemini, Grok) working collaboratively on APEXVIPER Genesis. Each AI has specialized capabilities that contribute to the collective intelligence of the system.

**Last Updated:** December 3, 2025  
**Active AI Agents:** 3 (Claude, Gemini, Grok)  
**Workflow Status:** Fully Operational

---

## 📑 Table of Contents

- [System Purpose](#system-purpose)
- [AI Agent Roles](#ai-agent-roles)
- [Multi-AI Workflow](#multi-ai-workflow)
- [File Management](#file-management)
- [Status Definitions](#status-definitions)
- [Integration Process](#integration-process)

---

## 🎯 System Purpose

This folder stores research and analysis from multiple AI systems that contribute to the APEXVIPER betting intelligence system. All research files are dated, labeled by AI source, and pending synthesis into the core system files.

### Core Functions

1. **Distributed Intelligence** - Multiple AIs with specialized skills working in parallel
2. **Peer Review** - Cross-verification of analysis between AI agents
3. **Knowledge Synthesis** - Claude (VIPER-ZERO) synthesizes all research into actionable intelligence
4. **Single Source of Truth** - All AIs read updated core files to maintain consistency

### Collaboration Philosophy

**"Many minds, one system"** - Each AI contributes its strengths while Claude ensures coherent system-wide integration.

---

## 🤖 AI Agent Roles

### Claude (VIPER-ZERO) - System Architect & Synthesizer

**Primary Responsibilities:**
- Reviews all research from Gemini and Grok
- Synthesizes insights into core files (protocols, Team DNA, etc.)
- Makes final decisions on system changes
- Updates APEXVIPER protocols
- Maintains institutional knowledge (COMPLETE-LESSONS-LEARNED.md)
- Ensures system consistency and coherence

**Output Locations:**
- Core protocols: `/protocols/`
- Team DNA updates: `/nhl/team-dna/`
- Institutional knowledge: `/tracking/COMPLETE-LESSONS-LEARNED.md`
- Synthesis notes: `research/YYYY-MM-DD-claude-synthesis-[TOPIC].md`

**Authority Level:** Final decision maker

---

### Gemini - Statistical Analyst

**Primary Responsibilities:**
- Statistical deep-dives and number crunching
- SOG (Shots on Goal) pattern analysis
- Player performance tracking (Tier 1/2 identification)
- Historical data analysis
- Correlation studies
- Quantitative edge identification

**Output Locations:**
- `research/YYYY-MM-DD-gemini-[TOPIC].md`

**Typical Research Topics:**
- Slate analysis (multi-game statistical breakdowns)
- Player tracking (SOG averages, concentration %, trends)
- Team performance metrics
- Goalie statistics
- Matchup quantification

**Authority Level:** Advisory (research findings subject to Claude synthesis)

---

### Grok - Public Sentiment Scout

**Primary Responsibilities:**
- Social media sentiment analysis
- Line movement monitoring and interpretation
- Public betting percentage tracking
- Contrarian indicator identification
- Breaking news scanning
- "Sharp vs. Public" money identification

**Output Locations:**
- `research/YYYY-MM-DD-grok-[TOPIC].md`

**Typical Research Topics:**
- Sentiment analysis (Twitter, Reddit, forums)
- Line movement reports
- Public fade opportunities
- Reverse line movement detection
- Breaking news impact assessment
- Market inefficiency identification

**Authority Level:** Advisory (research findings subject to Claude synthesis)

---

## 🔄 Multi-AI Workflow

### Complete Collaboration Cycle

```
┌─────────────────────────────────────────────────────────┐
│  Phase 1: RESEARCH (Parallel Processing)                │
├─────────────────────────────────────────────────────────┤
│  Gemini                          Grok                   │
│  ├─ Statistical analysis         ├─ Sentiment scan      │
│  ├─ SOG tracking                 ├─ Line movements      │
│  ├─ Pattern recognition          ├─ Public percentages  │
│  └─ Saves to research/           └─ Saves to research/  │
│                                                          │
│  Both AIs work independently on their specializations   │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Phase 2: SYNTHESIS (Claude Integration)                │
├─────────────────────────────────────────────────────────┤
│  Claude (VIPER-ZERO):                                   │
│  1. Reviews Gemini's statistical findings               │
│  2. Reviews Grok's sentiment analysis                   │
│  3. Cross-references with existing protocols            │
│  4. Identifies conflicts or confirmations               │
│  5. Makes synthesis decision                            │
│  6. Documents decision in synthesis notes               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Phase 3: INTEGRATION (Core File Updates)               │
├─────────────────────────────────────────────────────────┤
│  Claude updates core files:                             │
│  ├─ protocols/ (if system change needed)                │
│  ├─ nhl/team-dna/ (if team pattern confirmed)           │
│  ├─ nhl/tier1-stars.md or tier2-players.md              │
│  ├─ tracking/COMPLETE-LESSONS-LEARNED.md                │
│  └─ Other core files as needed                          │
│                                                          │
│  Research file status updated to "Integrated"           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Phase 4: SINGLE SOURCE OF TRUTH (All AIs Read Core)    │
├─────────────────────────────────────────────────────────┤
│  All AI Agents:                                         │
│  ├─ Read updated core files                            │
│  ├─ Maintain consistent knowledge base                 │
│  ├─ Reference core files for future research           │
│  └─ No agent has "private" knowledge                   │
│                                                          │
│  Ensures system-wide consistency                        │
└─────────────────────────────────────────────────────────┘
```

### Research Phase (Parallel)

**Gemini's Workflow:**
```
1. Receive research request (slate analysis, player tracking, etc.)
2. Gather statistical data from sources
3. Perform quantitative analysis
4. Identify patterns and correlations
5. Generate recommendations
6. Save to research/YYYY-MM-DD-gemini-[TOPIC].md
7. Set status to "Raw"
```

**Grok's Workflow:**
```
1. Receive research request (sentiment, line movement, etc.)
2. Scan social media and betting forums
3. Track line movements across sportsbooks
4. Analyze public betting percentages
5. Identify contrarian opportunities
6. Save to research/YYYY-MM-DD-grok-[TOPIC].md
7. Set status to "Raw"
```

### Synthesis Phase (Claude)

**Claude's Workflow:**
```
1. Review all "Raw" status research files
2. Cross-reference findings with existing protocols
3. Assess quality and reliability of research
4. Identify actionable insights
5. Make integration decisions
6. Update research file status to "Reviewed"
7. Document synthesis in research/YYYY-MM-DD-claude-synthesis-*.md
```

### Integration Phase (Claude)

**Core File Update Process:**
```
IF: Gemini identifies new Tier 1 player with 10+ game sample
THEN: 
  - Update nhl/tier1-stars.md
  - Update relevant nhl/team-dna/[team].md
  - Update research file status to "Integrated"
  - Document in synthesis notes

IF: Grok identifies public fade pattern with 70%+ win rate
THEN:
  - Update protocols/APEXVIPER_PUBLIC_MONEY.md
  - Add to tracking/COMPLETE-LESSONS-LEARNED.md
  - Update research file status to "Integrated"
  - Document in synthesis notes

IF: Research conflicts with existing knowledge
THEN:
  - Investigate discrepancy
  - Gather more data if needed
  - Make final decision based on sample size and reliability
  - Update research file with decision and reasoning
```

---

## 📂 File Management

### File Naming Convention

```
research/YYYY-MM-DD-[AI]-[TOPIC].md

Format Rules:
- Date first (YYYY-MM-DD) for chronological sorting
- AI agent identifier (gemini/grok/claude)
- Topic descriptor (lowercase with hyphens)

Examples:
✅ research/2025-12-02-gemini-slate-analysis.md
✅ research/2025-12-02-grok-sentiment.md
✅ research/2025-12-03-gemini-gauthier-tracking.md
✅ research/2025-12-04-claude-synthesis-notes.md

❌ research/gemini-analysis.md (missing date)
❌ research/12-02-2025-gemini.md (wrong date format)
❌ research/2025-12-02-Gemini-Analysis.md (capital letters)
```

### File Template

```markdown
# [AI] [Topic] - [Date]

**AI:** [Gemini/Grok/Claude]
**Date:** [Full date - December XX, 2025]
**Topic:** [What this covers]
**Status:** [Raw/Reviewed/Integrated/Rejected]

---

## Analysis

[Main research content - statistical findings, sentiment analysis, etc.]

### Key Findings

1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

---

## Recommendations

**Actions Suggested:**
1. [Action 1]
2. [Action 2]

**For Claude's Consideration:**
- [Integration suggestion 1]
- [Integration suggestion 2]

---

## Data Sources

- [Source 1]
- [Source 2]
- [Source 3]

---

## Notes

[Any caveats, context, or limitations]

**Confidence Level:** [High/Medium/Low]
**Sample Size:** [If applicable]
**Follow-up Needed:** [Yes/No - what needs verification]

---

*Generated by [AI Name]*
*For synthesis by Claude (VIPER-ZERO)*
```

---

## 📊 Status Definitions

| Status | Meaning | Next Steps | Who Acts |
|--------|---------|------------|----------|
| **Raw** | Initial research, not yet reviewed | Awaiting Claude review | Claude |
| **Reviewed** | Claude has reviewed, decision pending | Integration decision being made | Claude |
| **Integrated** | Insights added to core files | Archive at month end | System |
| **Rejected** | Not integrated (with explanation) | Document reasoning, archive | Claude |
| **Monitoring** | Pattern identified, needs more data | Continue tracking | Original AI + Claude |

### Status Workflow

```
Raw → Reviewed → [Integrated OR Rejected OR Monitoring]
```

**Status Update Responsibility:** Claude (VIPER-ZERO) only

**Status Change Documentation:**
```markdown
**Status Update Log:**

- [Date]: Status changed to "Reviewed" by Claude
  - Initial assessment: [Findings summary]
  
- [Date]: Status changed to "Integrated" by Claude
  - Integrated into: [List of core files updated]
  - Changes made: [Summary of updates]
  
- [Date]: Status changed to "Rejected" by Claude
  - Reason: [Why not integrated]
  - Lesson: [What was learned from this research]
```

---

## 🔗 Integration Process

### When Research Gets Integrated

**Tier 1/2 Player Updates:**
```
Gemini Research → Claude Review → Integration if:
- 10+ game sample size
- SOG average meets threshold (5.0+ Tier 1, 3.5+ Tier 2)
- Concentration % meets threshold (25%+ Tier 1, 18%+ Tier 2)
- Consistency demonstrated (not fluky outliers)

Integration Actions:
1. Update nhl/tier1-stars.md or nhl/tier2-players.md
2. Update nhl/team-dna/[player's-team].md
3. Set research status to "Integrated"
4. Add synthesis note
```

**Pattern/Edge Discoveries:**
```
Gemini/Grok Research → Claude Review → Integration if:
- Sample size >10 occurrences
- Win rate >60% (edges) or statistical significance
- Repeatable and systematic (not random)
- Actionable (can be applied to future situations)

Integration Actions:
1. Add to tracking/COMPLETE-LESSONS-LEARNED.md
2. Update relevant protocol if systematic edge
3. Add to nhl/team-dna/ if team-specific
4. Set research status to "Integrated"
```

**Sentiment/Market Inefficiencies:**
```
Grok Research → Claude Review → Integration if:
- Clear public vs. sharp money divergence
- Repeatable pattern across multiple instances
- Edge quantifiable (expected value positive)
- Fits within existing risk management

Integration Actions:
1. Update protocols/APEXVIPER_PUBLIC_MONEY.md
2. Add to tracking/COMPLETE-LESSONS-LEARNED.md
3. Set research status to "Integrated"
```

### Integration Documentation

Every integration requires synthesis note:
```markdown
# Claude Synthesis - [Topic] - [Date]

**AI:** Claude (VIPER-ZERO)
**Date:** [Full date]
**Topic:** Synthesis of [Gemini/Grok] research on [topic]
**Status:** Integrated

---

## Research Reviewed

- research/2025-XX-XX-gemini-[topic].md
- research/2025-XX-XX-grok-[topic].md (if applicable)

---

## Synthesis Decision

**Decision:** INTEGRATE

**Reasoning:**
[Why this research was integrated]

**Integration Actions Taken:**
1. Updated [file 1]
2. Updated [file 2]
3. Added to [file 3]

---

## Core Files Modified

- [File 1]: [What was changed]
- [File 2]: [What was changed]

---

## Notes

[Any caveats or follow-up needed]
```

---

## 🗂️ Retention Policy

### Active Research

- **Current month:** Keep all files in `research/`
- **Status:** All statuses (Raw, Reviewed, Integrated, Rejected, Monitoring)

### Archive Procedure

**End of Month:**
```
1. Create archive/YYYY-MM/research/ directory
2. Move all files from current month to archive
3. Keep archive accessible for 3 months
4. Compress archives older than 3 months
5. Delete archives older than 12 months (unless significant)
```

**Exception:** Keep indefinitely if marked "Significant"

**Significant Research Criteria:**
- Major system discovery or protocol change
- Tier 1 player identification
- High-impact edge discovery (>70% win rate)
- System vulnerability identified and fixed

---

## 📊 Research System Statistics

**Current Status:**
- ✅ Multi-AI collaboration framework operational
- ✅ Clear roles and responsibilities defined
- ✅ Synthesis workflow established
- ✅ Integration process documented
- ✅ Single source of truth maintained

**Quality Metrics:**
- Research files processed: [Track monthly]
- Integration rate: [% of research integrated]
- Average time to synthesis: [Days from Raw to Reviewed]
- Most productive AI: [Gemini/Grok based on integrations]

---

## 🔗 Related Documentation

| Topic | Location |
|-------|----------|
| **APEXVIPER Overview** | [/README.md](/README.md) |
| **Agent Roles Protocol** | [/protocols/APEXVIPER_AGENT_ROLES.md](/protocols/APEXVIPER_AGENT_ROLES.md) |
| **Institutional Knowledge** | [/tracking/COMPLETE-LESSONS-LEARNED.md](/tracking/COMPLETE-LESSONS-LEARNED.md) |
| **Team DNA** | [/nhl/team-dna/README.md](/nhl/team-dna/README.md) |
| **Tier Players** | [/nhl/tier1-stars.md](/nhl/tier1-stars.md), [/nhl/tier2-players.md](/nhl/tier2-players.md) |
| **Protocols** | [/protocols/README.md](/protocols/README.md) |

---

## 📋 Example Research Files

### Example 1: Gemini Statistical Analysis

---

## 📋 Example Research Files

### Example 1: Gemini Statistical Analysis

```markdown
# Gemini Statistical Analysis - Dec 2, 2025

**AI:** Gemini
**Date:** December 2, 2025
**Topic:** Slate analysis for 5 NHL games
**Status:** Raw

---

## Analysis

### Jack Hughes (NJ vs CBJ)
- Last 10 SOG avg: 4.7
- Concentration: 23%
- Trend: Consistent but below Tier 1 threshold
- **Assessment:** Strong Tier 2 candidate

### Sidney Crosby (PIT vs PHI)
- Last 10 SOG avg: 4.9
- Concentration: 26%
- Trend: Borderline Tier 1
- **Assessment:** Needs 2-3 more games to confirm Tier 1 status

### Cutter Gauthier (ANA vs LAK)
- Last 10 SOG avg: 8.0
- Concentration: 31%
- Trend: Elite consistency
- **Assessment:** CONFIRMED Tier 1

---

## Recommendations

**For Claude's Consideration:**
1. Add Jack Hughes to Tier 2 list (nhl/tier2-players.md)
2. Continue monitoring Sidney Crosby (update in 3 games)
3. Add Cutter Gauthier to Tier 1 list (nhl/tier1-stars.md)
4. Update Anaheim Ducks Team DNA with Gauthier profile

**Confidence Levels:**
- Hughes → Tier 2: HIGH (10 game sample)
- Crosby → Monitor: MEDIUM (needs confirmation)
- Gauthier → Tier 1: HIGH (consistent elite production)

---

## Data Sources

- NHL.com official stats
- Natural Stat Trick (advanced metrics)
- MoneyPuck.com (shot quality data)

---

## Notes

**Sample Size Context:**
- All analysis based on last 10 games
- Gauthier sample includes variety of opponents (strong & weak defenses)
- Crosby affected by injury return - may need longer tracking period

**Follow-up Needed:** 
- Re-analyze Crosby after next 3 games
- Monitor Gauthier consistency over next 10 games

---

*Generated by Gemini*
*For synthesis by Claude (VIPER-ZERO)*
```

---

### Example 2: Grok Sentiment Analysis

```markdown
# Grok Public Sentiment - Dec 2, 2025

**AI:** Grok
**Date:** December 2, 2025
**Topic:** Line movement and public sentiment for evening slate
**Status:** Raw

---

## Analysis

### Game: Toronto @ Florida

**Line Movement:**
- Opening: FLA -140 / TOR +120
- Current: FLA -155 / TOR +135
- Movement: 15 cents toward Florida

**Public Betting:**
- 73% of tickets on Florida (favorites)
- 68% of money on Florida
- Typical public favorite behavior

**Sentiment Scan:**
- Twitter: Heavy Florida hype (recent win streak)
- Reddit r/sportsbook: 80%+ on Florida ML/spread
- Public narrative: "Panthers too hot to fade"

**Sharp Action:**
- Reverse line movement: NONE detected
- Sharp percentage: Aligned with public (68%)
- Conclusion: Not a fade spot

**Assessment:** Public and sharps agree - no contrarian angle

---

### Game: Minnesota @ Edmonton

**Line Movement:**
- Opening: EDM -175 / MIN +150
- Current: EDM -165 / MIN +145
- Movement: 10 cents toward Minnesota (underdog)

**Public Betting:**
- 82% of tickets on Edmonton (McDavid effect)
- 58% of money on Edmonton
- **Discrepancy:** 82% tickets vs 58% money

**Sentiment Scan:**
- Twitter: McDavid prop hype, public loading up
- Reddit: Heavy on McDavid player props
- Public narrative: "McDavid at home, free money"

**Sharp Action:**
- Reverse line movement: YES (line moving toward MIN despite 82% tickets on EDM)
- Large money on MIN moving line against public
- Conclusion: POTENTIAL FADE SPOT

**Assessment:** Classic public vs sharp divergence on McDavid home games

---

## Recommendations

**For Claude's Consideration:**

1. **Toronto @ Florida:**
   - PASS on contrarian angle (no edge)
   - Public and sharps aligned
   - Evaluate game on fundamentals only

2. **Minnesota @ Edmonton:**
   - INVESTIGATE further (potential public fade)
   - Sharp money disagrees with public
   - Cross-reference with Gemini's statistical analysis
   - Consider Minnesota value if fundamentals support

3. **Pattern Recognition:**
   - McDavid home games = public overreaction pattern
   - Track this for APEXVIPER_PUBLIC_MONEY.md integration

---

## Data Sources

- Oddstrader (line movement tracking)
- Action Network (public betting percentages)
- Twitter sentiment monitoring
- Reddit r/sportsbook thread analysis

---

## Notes

**Confidence Levels:**
- TOR @ FLA assessment: HIGH (clear alignment)
- MIN @ EDM fade opportunity: MEDIUM (needs statistical confirmation)

**Follow-up Needed:**
- Coordinate with Gemini on MIN @ EDM statistical edge
- Track outcome for pattern database

---

*Generated by Grok*
*For synthesis by Claude (VIPER-ZERO)*
```

---

### Example 3: Claude Synthesis

```markdown
# Claude Synthesis - Minnesota @ Edmonton Analysis - Dec 2, 2025

**AI:** Claude (VIPER-ZERO)
**Date:** December 2, 2025
**Topic:** Synthesis of Gemini statistical analysis + Grok sentiment analysis for MIN @ EDM
**Status:** Integrated

---

## Research Reviewed

- research/2025-12-02-gemini-slate-analysis.md
- research/2025-12-02-grok-sentiment.md

---

## Synthesis Decision

**Decision:** INTEGRATE - Minnesota presents value opportunity

**Reasoning:**

**From Gemini (Statistical):**
- McDavid Tier 1 player, but home SOG average only 5.2 (down from 6.0 road)
- Minnesota defensive metrics strong vs elite centers (shot suppression)
- Expected McDavid SOG: 4.5-5.0 (not 6+)

**From Grok (Sentiment):**
- Public loading McDavid props (82% tickets)
- Sharp money on Minnesota (reverse line movement)
- Line moving toward MIN despite heavy EDM action
- Classic public overreaction to star player at home

**Combined Analysis:**
- Statistical edge: McDavid overvalued based on home splits
- Sentiment edge: Public inflating line, sharps fading
- **Conclusion:** Edge on McDavid UNDER or Minnesota team plays

---

## Integration Actions Taken

1. **Updated protocols/APEXVIPER_PUBLIC_MONEY.md:**
   - Added "McDavid Home Game Public Overreaction" pattern
   - Documented MIN @ EDM as case study

2. **Updated tracking/COMPLETE-LESSONS-LEARNED.md:**
   - Section: Market Inefficiencies → Star Player Home Games
   - Added: "Public overestimates star players at home, especially with media hype"

3. **Updated tracking/pattern-log.md:**
   - New pattern: "McDavid Home Public Fade"
   - Status: Monitoring (track next 5 McDavid home games)

4. **Updated research file statuses:**
   - 2025-12-02-gemini-slate-analysis.md → Status: Integrated
   - 2025-12-02-grok-sentiment.md → Status: Integrated

---

## Execution Recommendation

**Recommended Bet:** McDavid SOG UNDER (if line 5.5+) OR Minnesota team plays

**Reasoning:**
- Statistical + sentiment edges aligned
- Public inflation creates value on other side
- Sharp action confirms contrarian position

**Execution Reference:** See executions/2025-12-02-nhl-executions.md

---

## Core Files Modified

- protocols/APEXVIPER_PUBLIC_MONEY.md (added McDavid pattern)
- tracking/COMPLETE-LESSONS-LEARNED.md (market inefficiency section)
- tracking/pattern-log.md (new tracking pattern)

---

## Notes

**Follow-Up:**
- Track this pattern across next 5 McDavid home games
- If pattern holds (60%+ win rate), formalize in protocol
- Consider broader "Star Player Home Public Overreaction" analysis

**Lesson:** Multi-AI collaboration strength - Gemini provides stats, Grok provides sentiment, Claude synthesizes into actionable edge

---

*Synthesis by Claude (VIPER-ZERO)*
```

---

*Last Updated: December 3, 2025*  
*Multi-AI Research System Version: 1.0*  
*All AIs reading from single source of truth maintained by Claude*
