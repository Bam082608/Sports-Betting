# 🗄️ APEXVIPER DATABASE STRUCTURE v1.0
**Directive:** Standardize storage for betting intelligence.
**Goal:** Create a scalable "External Brain" that agents must query before recommending bets.

## 1. DIRECTORY MAP
- `nhl/team-dna/` → Stores Team Defense/Goalie DNA. (**The Shield**)
- `nhl/players/` → Stores Shooter/Scorer Profiles. (**The Sword**)
- `research/` → Daily logs and one-time analysis. (**The Trash Can**)

### 1.1 TEAM DNA FILES (The Shield)
**Path Pattern:** `nhl/team-dna/[team-name].md`
**Required Keys in Evidence:** `Analysis File:`, `Sources:`, `Retrieved_At:`, `Author:`, `Verifier:`

### 1.2 PLAYER PROFILE FILES (The Sword)
**Path Pattern:** `nhl/players/[player-name].md`
**Trigger:** Tier 1 Stars or verified "Hidden Volume" targets.

### 1.3 RESEARCH FILES (The Trash Can)
**Path Pattern:** `research/YYYY-MM-DD-*-analysis.md`
**Purpose:** Contains the VERIFIED Data Integrity Checklist.

---

## 2. AGENT BEHAVIOR RULES
1. **First Read:** Before any SOG analysis, check `nhl/team-dna/` for the opponent.
2. **Blocker Alert:** If DNA flags `[BLOCKER]`, acknowledge the risk immediately.
3. **Update Protocol:** New structural truths must be committed to Team DNA via PR.
