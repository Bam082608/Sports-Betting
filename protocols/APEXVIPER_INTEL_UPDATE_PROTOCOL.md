# 🧠 APEXVIPER INTEL UPDATE PROTOCOL v1.0

**Directive:** Turn "Spotter Reports" into **Permanent Team DNA**.  
**Trigger:** Post-analysis of any Spotter Target.  
**Status:** **MANDATORY** — Requires Analyst evidence + Opus (or designated human) verification.

---

## 1. THE OBJECTIVE

When a "Deep Dive" or "Spotter Report" reveals a **structural truth** about a team  
(e.g., *"Philadelphia systematically blocks Centers"*), you must **update that Team's DNA file** under:

```text
nhl/team-dna/<team-name>.md
```

**Non‑negotiable:** Do **not** let critical intel die in ephemeral chat logs.

---

## 2. KEY GUARDIAN IDENTIFICATION

When analysis reveals an "Elite Defender" or "Shot Blocking Specialist":

1. Identify the player and role (e.g., *Nick Seeler*).
2. Tag the role explicitly:
   - `"[BLOCKER]"` — shot blocking / volume suppression
   - `"[LOCKDOWN]"` — matchup/usage-based defensive denial
3. Create or update:

```text
nhl/team-dna/<team-name>.md
```

---

## 3. UPDATE WORKFLOW (MEMORY DUMP)

### A. Preconditions (MUST be true before updating DNA)

- An analysis file exists:

  ```text
  research/YYYY-MM-DD-*-analysis.md
  ```

- The analysis file includes a **Data Integrity Checklist**.
- Checklist status is `VERIFIED` (not DRAFT, PENDING, or UNVERIFIED).
- Evidence sources are listed (e.g., **NaturalStatTrick**, **EvolvingHockey**, **DailyFaceoff**, etc.).
- **Analyst signature** is present (e.g., `Author: Gemini 3 Pro`).
- **Verifier signature** is present (e.g., `Verifier: Claude Opus 4.5` or named human).

If any of the above are missing or unverified, the update is **blocked** (see Section 4).

---

### B. Update steps (Chain of Custody)

1. **Analyst** proposes Team DNA edits as a **patch/diff**, including:
   - Precise locations in `nhl/team-dna/<team-name>.md`.
   - Reference to the analysis file (path + short description).
2. **Runner** (Copilot/Grok/Mini or similar) opens a **PR against `main`** that includes:
   - The edited:

     ```text
     nhl/team-dna/<team-name>.md
     ```

   - A link to the source analysis file:

     ```text
     research/YYYY-MM-DD-*-analysis.md
     ```

   - Checklist location and status (`VERIFIED`).
   - Commit message format:

     ```text
     INTEL: Update <team-name> DNA — [KEY_GUARDIAN] — [YYYY-MM-DD]
     ```

3. **CI checks run** (see Section 6) and must pass.
4. **Verifier / Reviewer** (Claude Opus 4.5 or designated human):
   - Confirms evidence, checklist, and schema.
   - Either **approves** or **rejects** with rationale.
5. On approval and merge, the PR commit becomes the **canonical record**.

---

### C. TEAM FILE SCHEMA (REQUIRED FORMAT)

Every team file **must** conform to this schema:

```markdown
# 🟠 <TEAM DISPLAY NAME> (Team DNA)
**Defense Grade:** [ELITE / STRONG / AVERAGE / WEAK]
**Key Vulnerability:** [short text]

## 🛡️ THE NO-FLY ZONE (Do Not Bet Against)
- **<Player Name> [BLOCKER | LOCKDOWN]:** one-line description + stat signal (e.g., blocks/game, xGA/60, usage)
- **<Player Name> [LOCKDOWN]:** matchup role and minutes played (e.g., top-pair LD, PK1, ~21 TOI)

## 🎯 TARGETING PROFILE
- Position-level guidance (e.g., Centers: 🔴 FADE; Wingers: 🟡 CAUTION; Point Shots: 🟢 GREEN)
- Volume shooter guidance (e.g., "Avoid unders on high-volume shooters unless [BLOCKER] inactive.")

## EVIDENCE & LINKS
- Analysis File: research/YYYY-MM-DD-*-analysis.md
- Sources: [NaturalStatTrick], [EvolvingHockey], [DailyFaceoff], ...
- Retrieved_At: YYYY-MM-DDTHH:MM:SSZ
- Author: <Analyst Name or Agent>  (e.g., Gemini 3 Pro)
- Verifier: <Opus or Human Reviewer> (e.g., Claude Opus 4.5)

## CHANGE LOG
- YYYY-MM-DD — Author — Brief rationale — PR#: #### — Analysis: research/YYYY-MM-DD-*-analysis.md
```

**Enforcement rule:** PRs that modify `nhl/team-dna/*` **must** also update the `CHANGE LOG` and reference the analysis file.

---

## 4. VERIFICATION & VETO

- Only proceed with Team DNA updates if the Data Integrity Checklist in the analysis file is marked `VERIFIED`.
- If the checklist is **missing**, **UNVERIFIED**, or **FAILED**:
  - The update is **blocked**.
  - The Verifier responds with a NO SIGN-OFF decision (per Roundtable Protocol v2.0, if present).
- Human owner retains **ultimate veto power**, either directly or via `CODEOWNERS` for `nhl/team-dna/`.

---

## 5. AUDIT TRAIL & PROVENANCE

Every Team DNA change **must** cite:

- Analysis file:
  - Path: `research/YYYY-MM-DD-*-analysis.md`
  - (Optionally) commit SHA where that analysis was introduced.
- Data sources and reference windows (e.g., "Last 10 games", "Season to date").
- Author (Analyst) and Verifier (Opus/human).
- PR number and merge date.

**Do not** edit Team DNA files directly on `main`.  
All changes must pass through a **PR-based workflow** to preserve history and review.

---

## 6. CI / AUTOMATION RECOMMENDATIONS

Recommended CI gate for PRs touching `nhl/team-dna/*`:

1. **Checklist Validation**
   - Ensure the referenced analysis file:
     - Exists under `research/`.
     - Contains a **Data Integrity Checklist**.
     - Has status `VERIFIED`.

2. **Metadata Enforcement**
   - Required keys in the `EVIDENCE & LINKS` section:
     - `Analysis File`
     - `Sources`
     - `Retrieved_At`
     - `Author`
     - `Verifier`

3. **Schema Enforcement**
   - Team file must contain:
     - Top-level heading: `# 🟠 <TEAM DISPLAY NAME> (Team DNA)`
     - Sections: `THE NO-FLY ZONE`, `TARGETING PROFILE`, `EVIDENCE & LINKS`, `CHANGE LOG`.
   - At least one `[BLOCKER]` or `[LOCKDOWN]` entry if the PR claims to add a key defensive guardian.

4. **Notification Automation (Optional)**
   - On PR open:
     - Bot comment tagging relevant analysts + Opus reviewer.
     - Summary of affected teams and players (e.g., "Updated: PHI — Nick Seeler [BLOCKER]").

---

## 7. READ-BEFORE-ACT RULE (RUNTIME BEHAVIOR)

For **any** agent preparing new analysis or betting recommendations involving a team:

1. The agent **must read**:

   ```text
   nhl/team-dna/<team-name>.md
   ```

   before issuing verdicts.

2. If a player is tagged in the Team DNA as `[BLOCKER]` or `[LOCKDOWN]` and is **expected to play**:
   - The agent must:
     - **Flag** the structural risk explicitly to the user.
     - Consider **downgrading** or **blocking**:
       - High-volume shot overs **against** this team.
       - Fragile edges built on raw Corsi without accounting for shot suppression.
     - Provide a rationale referencing the Team DNA entry (player, tag, and source analysis).

3. If the player is **injured / scratched / minutes drastically reduced**:
   - The agent must:
     - Note the discrepancy.
     - Either:
       - Treat historical DNA as **partially suspended**, or
       - Recommend a new spotter analysis before large exposure.

---

## 8. ROLE RESPONSIBILITIES

- **Analyst (e.g., Gemini 3 Pro):**
  - Produce evidence-rich Spotter/Deep Dive reports.
  - Flag structural truths and propose **specific** DNA changes (with patch-style proposals).
  - Maintain a **Chain of Custody checklist** in the analysis file.

- **Runner (e.g., Copilot, Grok, Mini Agents):**
  - Implement the mechanical steps:
    - File creation/updates.
    - PR creation.
  - **Do not invent new structural claims.**
  - Only apply Analyst + Verifier authorized edits.

- **Verifier / Supreme Court (e.g., Claude Opus 4.5 or human):**
  - Validate the Data Integrity Checklist and evidence.
  - Enforce this protocol and veto weak or speculative updates.
  - Approve or reject PRs touching `nhl/team-dna/`.

- **Project Lead / Repo Owner (You):**
  - Maintain `CODEOWNERS` if desired to control who can approve `nhl/team-dna/` changes.
  - Periodically review Team DNA files for drift and necessary refactors.

---

**Version:** 1.0 — APEXVIPER INTEL UPDATE PROTOCOL  
**Scope:** `nhl/team-dna/*`, `research/*`  
**Goal:** Convert ephemeral edge detection into durable, verifiable Team DNA.
