# Research Folder

*AI Contributions for APEXVIPER System*

---

## Purpose

This folder stores research and analysis from multiple AI systems that contribute to the APEXVIPER betting intelligence system. All research files are dated, labeled by AI source, and pending synthesis into the core system files.

---

## AI Roles

| AI | Role | Contributions |
|----|------|---------------|
| **Claude (VIPER-ZERO)** | System Architect & Synthesizer | Reviews research, updates core files, makes final decisions |
| **Gemini** | Statistical Analyst | Number crunching, pattern recognition, SOG analysis |
| **Grok** | Public Sentiment Scout | Social media scanning, line movement, contrarian indicators |

---

## Workflow

### 1. Research Phase
- **Gemini** performs statistical analysis → Saves to `research/YYYY-MM-DD-gemini-[TOPIC].md`
- **Grok** performs sentiment analysis → Saves to `research/YYYY-MM-DD-grok-[TOPIC].md`

### 2. Synthesis Phase
- **Claude** reviews all research files
- Cross-references with core protocols
- Updates `core/` files with vetted insights

### 3. Integration Phase
- Confirmed patterns added to `core/nhl/team-dna/` or `core/protocols/`
- Research file status updated to "Integrated"
- Original research preserved for historical reference

---

## File Naming Convention

```
research/YYYY-MM-DD-[AI]-[TOPIC].md

Examples:
- research/2025-12-02-gemini-slate-analysis.md
- research/2025-12-02-grok-sentiment.md
- research/2025-12-03-gemini-gauthier-tracking.md
- research/2025-12-04-claude-synthesis-notes.md
```

---

## File Template

```markdown
# [AI] [Topic] - [Date]

**AI:** [Gemini/Grok/Claude]
**Date:** [Full date]
**Topic:** [What this covers]
**Status:** [Raw/Reviewed/Integrated]

## Analysis

[Content here]

## Recommendations

[What action should be taken]

## Notes

[Any caveats or context]
```

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| **Raw** | Initial research, not yet reviewed |
| **Reviewed** | Claude has reviewed, decision pending |
| **Integrated** | Insights added to core files |
| **Rejected** | Not integrated (with explanation) |

---

## Retention Policy

- **Current month:** Keep in `research/`
- **Previous months:** Move to `archive/YYYY-MM/research/`
- **Keep accessible:** Last 3 months
- **Delete:** Older files unless significant

---

## Example Research File

```markdown
# Gemini Statistical Analysis - Dec 2, 2025

**AI:** Gemini
**Date:** December 2, 2025
**Topic:** Slate analysis for 5 NHL games
**Status:** Raw

## Analysis

### Jack Hughes (NJ vs CBJ)
- Last 10 SOG avg: 4.7
- Concentration: 23%
- Trend: Consistent but below Tier 1 threshold
- **Recommendation:** Tier 2, not Tier 1

### Sidney Crosby (PIT vs PHI)
- Last 10 SOG avg: 4.9
- Concentration: 26%
- Trend: Borderline Tier 1
- **Recommendation:** Needs verification

## Recommendations

1. Add Hughes to Tier 2 list
2. Monitor Crosby for one more game before Tier 1 confirmation

## Notes

Data pulled from NHL.com and Natural Stat Trick
```

---

*All AIs can read core files for single source of truth. Research files are raw analysis pending synthesis.*
