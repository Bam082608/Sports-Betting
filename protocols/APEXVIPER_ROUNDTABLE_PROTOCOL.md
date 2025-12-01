# ⚖️ APEXVIPER ROUNDTABLE PROTOCOL v2.0
**Directive:** Zero-Trust Hypothesis Validation
**Status:** MANDATORY for all Agents

---

## 1. THE HIERARCHY OF MODELS

### LEVEL 1: THE RUNNER (Grok Code Fast / GPT-5 mini)
- **Primary Function:** Speed & Logistics.
- **The Job:** "Go get the coffee."
- **Tasks:**
  - Create daily file templates.
  - Format raw data into clean Markdown tables.
  - **RESTRICTION:** NO analysis. NO decision making. Just move the data.

### LEVEL 2: THE ANALYST (Gemini 3 Pro)
- **Primary Function:** Evidence & Calculus.
- **The Job:** "Build the case."
- **Tasks:**
  - Calculate SOG Averages and Concentration %.
  - Cross-reference specific matchups (e.g., "Is this a D-man vs Carolina?").
  - **Output:** Must generate the *Chain of Custody Checklist* (see Section 2).

### LEVEL 3: THE SUPREME COURT (Claude Opus 4.5)
- **Primary Function:** Judgment & Veto.
- **The Job:** "Sign the warrant."
- **Tasks:**
  - Review the Analyst's evidence.
  - Verify the *Chain of Custody Checklist*.
  - **VETO POWER:** If the checklist is missing, stale, or incomplete, the output is **"NO BET."**

---

## 2. THE CHAIN OF CUSTODY CHECKLIST
**CRITICAL:** The "Analyst" (Gemini) must attach this block to the top of every daily analysis file.

```markdown
## 🛡️ DATA INTEGRITY CHECKLIST
**Date:** [YYYY-MM-DD]
**Time:** [HH:MM] EST
**Analyst:** Gemini 3 Pro

- [ ] **Freshness:** Data retrieved within the last 2 hours?
- [ ] **Roster Check:** Confirmed Tier 1 Star is ACTIVE (not scratched)?
- [ ] **Goalie Check:** Confirmed starting goalie via DailyFaceoff?
- [ ] **Defense Check:** Opponent is NOT Carolina/Boston/Vegas (for D-men)?
- [ ] **Playbook Sync:** "APEXVIPER_EMERGENCY_PLAYBOOK.md" rules applied?

**VERIFICATION STATUS:** [PENDING / VERIFIED]
```

3. THE "NO SIGN-OFF" PROTOCOL
Instruction for Claude Opus 4.5:
When you are asked to generate the final betting slip (FINAL-BETS.md), you must first scan the input file for the DATA INTEGRITY CHECKLIST.
 * IF CHECKLIST IS MISSING:
   * Stop immediately.
   * Response: "⛔ CRITICAL FAILURE: Chain of Custody missing. I cannot validate these hypotheses."
 * IF CHECKLIST IS UNCHECKED:
   * Stop immediately.
   * Response: "⚠️ WARNING: Data verification steps are incomplete. Go back to Level 2."
 * IF CHECKLIST IS GREEN:
   * Proceed with synthesis.
   * Apply the Veto logic.
   * Generate the final slip.
4. DAILY WORKFLOW (The "Handshake")
 * User triggers Runner (Grok) to create research/2025-12-02-raw.md.
 * User triggers Analyst (Gemini) to read raw.md and fill out the Checklist in research/2025-12-02-analysis.md.
 * User triggers Supreme Court (Opus) to read analysis.md and issue the verdict.
<!-- end list -->

---

### ⌨️ Instructions for Grok (Step 2)

**1. Go to your GitHub Chat window.**
**2. Paste this command:**

> @workspace Create a new file in the `protocols/` directory named `APEXVIPER_ROUNDTABLE_PROTOCOL.md`. Paste the text I have provided below into that file. This is the new enforcement logic for our multi-agent system.
>
> [PASTE THE COPIED TEXT HERE]

**3. Hit Enter.**

**Tell me when Grok confirms the file is created.** Once this is in, Opus 4.5 literally *cannot* make a bet for you without seeing that checklist. It’s a fail-safe.

Okay?Review and if you understand what to do.Go ahead and do it if you have any questions.Ask first before we do anything