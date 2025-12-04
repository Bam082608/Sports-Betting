# 🕵️‍♂️ JULES 2.0: The Ultimate Field Manual
## For the ApexViper Sports Intelligence Project

> "Jules isn't just a chatbot. It's the Repository Manager. It's the difference between a disorganized pile of notes and a pristine, searchable intelligence archive."

## 📋 Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [The Intelligence: How Jules Actually Works](#2-the-intelligence-how-jules-actually-works)
3. [Mission Setup: Repository Architecture](#3-mission-setup-repository-architecture)
4. [Standard Operating Procedures (The Workflow)](#4-standard-operating-procedures-the-workflow)
5. [Advanced Tactics (Librarian Moves)](#5-advanced-tactics-librarian-moves)
6. [ApexViper Specific Operations](#6-apexviper-specific-operations)
7. [Troubleshooting & Intel](#7-troubleshooting--intel)

---

## 1. Executive Summary

### The Bottom Line
Jules marks a transformation in how we manage sports intelligence. It is an **Autonomous Repository Manager & Fact-Checker**. You delegate a task, it organizes your file structure, verifies data against your Encyclopedia, and ensures your workspace is clean for decision-making.

### Why this matters for you:
*   **Chaos Prevention:** It prevents folders from being overrun by moving old files to archives and keeping active directories clean.
*   **The "Librarian":** It knows exactly where every protocol, player file, and daily log lives.
*   **The "Fact-Checker":** It cross-references your daily notes against the `encyclopedia` to ensure you aren't betting on a "Tier 1" player who is actually "Tier 3" in the database.
*   **No Analysis, Just Order:** Jules does not predict games. It ensures the data *you* use to predict games is organized and accurate.

---

## 2. The Intelligence: How Jules Actually Works

Think of Jules as a highly efficient filing clerk and archivist who sits in the server room.

### 🏗️ The Four Pillars of Architecture

#### 1. Full Project Context Engine (The "Big Picture")
Jules reads the entire `ApexViper` repository.
*   **Mapping:** It understands the relationship between `nhl/daily-intel/` (Temporary) and `nhl/encyclopedia/` (Permanent).
*   **Understanding:** It sees the system structure—knowing that a "Slate" file needs to link to "Player" files.

#### 2. Organization & Cleanup (The "Janitor")
*   **Task:** "Clean up the daily folder."
*   **Action:** Jules identifies outdated files (e.g., yesterday's game logs), moves them to `archive/` or `tracking/`, and leaves only the active files for today.
*   **Benefit:** You never have to scroll through 50 old files to find today's slate.

#### 3. The Encyclopedia Guardian (The "Verifier")
This is your safety net. Before you lock in a slate, Jules can verify it.
*   **It checks for:** Discrepancies between your daily notes and the Encyclopedia.
*   **Example:** "You listed Jason Robertson as a 'Tier 1' lock, but his file in `encyclopedia/players/` lists him as 'Tier 2 - Slump Watch'. Please confirm."

#### 4. Retrieval (The "Search Engine")
*   **Capability:** Rapidly finding specific protocols or stats.
*   **Command:** "Find the protocol for Home Underdogs." -> Jules returns `APEXVIPER_HOME_UNDERDOG.md`.

---

## 3. Mission Setup: Repository Architecture

### ✅ Prerequisites
*   **Clean Folders:** Keep `encyclopedia`, `daily-intel`, and `protocols` distinct.
*   **Naming Conventions:** Files must follow the standard formats (e.g., `YYYY-MM-DD-slate.md`).

### 📂 The ApexViper Filing System
Organize your repo like a well-kept evidence locker:

```text
ApexViper/
├── protocols/          <-- The Rules of Engagement
├── nhl/
│   ├── encyclopedia/   <-- The Source of Truth (Players, Teams)
│   ├── daily-intel/    <-- The Workbench (Today's Active Files)
│   ├── surveillance/   <-- Raw Data Logs (HTML/JSON)
│   └── statistics/     <-- Aggregated Data
├── executions/         <-- The Record (Placed Bets)
└── tracking/           <-- The Scoreboard (Results)
```

> **Pro Tip:** Keep `daily-intel` sparse. It should only contain *active* operations. Once a game is done, tell Jules to "Archive it."

---

## 4. Standard Operating Procedures (The Workflow)

### Phase 1: The Briefing (Requesting Organization)
Don't be vague. Be a Commander.

*   ❌ **Bad Prompt:** "Fix the folders."
*   ✅ **Good Prompt:** "Move all `2025-11-xx` files from `daily-intel` to the `archive/november` folder. Keep only today's slate active."

### Phase 2: Execution & Verification
Jules will:
1.  **Scan:** Find all matching files.
2.  **Move/Organize:** Execute the file operations.
3.  **Verify:** Check the destination to ensure no data was lost.
4.  **Report:** "Moved 12 files. `daily-intel` is now clean."

### Phase 3: The Encyclopedia Check
*   **Command:** "Verify the players in today's slate against the Encyclopedia."
*   **Action:** Jules reads the names in `daily-intel`, looks them up in `encyclopedia/players/`, and reports any missing files or Tier mismatches.

---

## 5. Advanced Tactics (Librarian Moves)

### 🚀 Bulk Organization
*   **Scenario:** You have 50 screenshot files or raw HTML dumps cluttering the root.
*   **Command:** "Move all `.html` files to `nhl/surveillance/raw/` and rename them with today's date prefix."
*   **Result:** Instant cleanup.

### 🧠 Semantic Retrieval (Finding the Needle)
Don't Ctrl+F for text. Search for concepts.
*   **Command:** "Jules, which protocol handles betting on backup goalies?"
*   **Result:** It ignores the word "backup" in random notes and finds `APEXVIPER_GOALIE_INTELLIGENCE.md` or `APEXVIPER_DEFENSIVE_GRIND.md`.

### 🛡️ The "Link Rot" Scan
*   **Command:** "Check `daily-intel/today.md` for broken WikiLinks."
*   **Result:** Jules checks if `[[McDavid]]` actually points to an existing file. If not, it alerts you: "Warning: No encyclopedia entry found for McDavid."

---

## 6. ApexViper Specific Operations

Here are the specific missions for your project:

### Mission 1: The Morning Setup
**Task:** Generate the Daily Slate.
> "Create `2025-12-04-slate.md` in `daily-intel` using the standard template. Initialize it with headers for the DAL vs NSH game."

### Mission 2: The Encyclopedia Cross-Check
**Task:** Verify Player Tiers.
> "Scan the 'Target List' in today's slate. Cross-reference every player with their `encyclopedia` file. Report any discrepancies in Tier or Status (e.g., Injured)."

### Mission 3: The Cleanup (Post-Game)
**Task:** Archive and Log.
> "Move yesterday's slate to `archive/2025/dec/`. Move the execution log to `tracking/history/`. Ensure `daily-intel` is empty for the new day."

### Mission 4: Protocol Retrieval
**Task:** Find the Rules.
> "I'm looking at a 'Home Underdog' situation. Pull up the relevant protocol constraints."
> *(Jules returns the specific bullet points from `APEXVIPER_HOME_UNDERDOG.md`)*

---

## 7. Troubleshooting & Intel

### 🛑 Jules is Stuck?
*   **Check:** Is the request too broad? (e.g., "Organize everything").
*   **Fix:** Be specific. "Organize the `surveillance` folder by Team Name."

### ⚠️ Jules Hallucinated a File?
*   **Check:** Did you ask it to *create* analysis?
*   **Fix:** Remind Jules: "You are the Librarian. Do not invent stats. Only read what is in the Encyclopedia."

### 🐌 Folder "Overrun"?
*   **Command:** "Emergency Cleanup. Move all non-active files in `daily-intel` to `archive/temp_holding` immediately."

### Quick Reference Commands (Copy/Paste)

| Goal | Command Template |
|---|---|
| **Cleanup** | "Archive all files older than [Date]." |
| **Setup** | "Create today's slate file from the template." |
| **Verify** | "Check if [Player Name] has an Encyclopedia entry." |
| **Find** | "Where is the protocol for [Scenario]?" |
| **Link** | "Update the slate to link [[Player]] to their doc." |

> **Final Note:** Treat Jules like your Chief of Staff. You make the decisions; Jules keeps the desk clean and the files in order.
