# 🧠 APEXVIPER MASTER QUERY PROTOCOL v1.0
**Directive:** Mandatory "Pre-Flight Check" for all betting analysis.  
**Scope:** Applies to ALL NHL betting questions asked by the Project Lead.

---

## 1. THE "TRIANGULATION" RULE

Before recommending **ANY** bet, the Agent must perform a **3‑point check**:

### Point A: The Macro Context  
**Read:** `protocols/APEXVIPER_MACRO_INTELLIGENCE.md`

**Macro Check Questions:**
- Is this a **Road Dog** spot (Road underdog +1.5 or ML)?
- Is there a **Variance Void** (Elite "System Goalie" out)?
- Is this a **Fatigue / Olympic Squeeze** spot (3-in-4, back-to-back with travel, home off long road trip)?
- Is this team classified as **High Event** or **Trap** in the macro file?

> If any macro law clearly applies, the Agent must state it explicitly in the response.

---

### Point B: The Micro Matchup  
**Read:** `nhl/team-dna/[opponent-team].md` AND, if available, `nhl/team-dna/[player-team].md`

**Micro Check Questions:**
- Does the opponent have a tagged defender like `[BLOCKER]`, `[LOCKDOWN]`, or `[WALL]` that affects this prop?
- Is the opponent classified as **High Event**, **Trap**, **Over Machine**, etc. in their Team DNA?
- Does the Team DNA recommend **FADE** or **GREEN** for this **position archetype** (Center vs Winger vs D-man)?

> If no Team DNA file exists yet, the Agent must explicitly say:  
> "No Team DNA file found for [Team]; falling back to Macro Intelligence + market data only."

---

### Point C: The Asset Status  
**Read:** One or more of:
- `research/YYYY-MM-DD-slate-data.md` (daily odds and averages), and/or
- `nhl/players/[player-name].md` (if a dedicated player profile exists), and/or
- The most relevant `research/YYYY-MM-DD-*-analysis.md` file for that slate.

**Asset Check Questions:**
- What is the player's **role and position** (C vs W vs D)? Does it collide with any Team DNA warnings?
- What is the **average SOG / iCF / usage** vs the current line and price?
- Is this leg **priced fairly**, **valuable**, or **a trap** given the macro + micro context?

---

## 2. THE RESPONSE FORMAT (STANDARD OUTPUT)

All analysis outputs must follow this structure:

**🎯 TARGET:**  
- [Player/Team/Market]  
  - e.g., "Owen Tippett 2+ SOG vs PIT" or "Penguins Team Total Over 2.5"

**📊 TRIANGLE CHECK:**
- **Macro:**  
  - Brief statement about Road Dog / Fatigue / Variance Void / High Event vs Trap.  
  - Example: "Road Dog angle active; home team on back‑to‑back with travel."
- **Micro (Team DNA):**  
  - Key Team DNA notes for both sides.  
  - Example: "PHI DNA = Fade Centers; Seeler [BLOCKER] active."
- **Asset (Price & Role):**  
  - Core stats, odds, and role notes.  
  - Example: "Averages 2.46 SOG, line 2+ at -280; winger vs soft defense."

**🐍 VERDICT:**  
- One of: **GREEN / YELLOW / RED**  
  - **GREEN:** Strong alignment across Macro, Micro, and Asset (high WBS).  
  - **YELLOW:** Mixed signals; playable but sized down or only in specific constructions.  
  - **RED:** Structural conflict (e.g., betting Centers vs Philly, unders in Variance Void spots).

> The Agent must clearly justify the color using the three points above.

---

## 3. THE "AUTO-FAIL" TRIGGERS (HARD STOPS)

The Agent must **NOT** recommend a bet if any of the following conditions are true:

1. **Team DNA Hard Conflict**
   - If Opponent DNA explicitly says **FADE** this archetype (e.g., "Fade Centers vs PHI") and the proposed bet is that exact archetype (e.g., Crosby SOG over vs PHI), the default is:
     - **VERDICT:** RED — **HARD PASS**, unless the Project Lead explicitly asks to override.

2. **Variance Void vs Unders**
   - If `APEXVIPER_MACRO_INTELLIGENCE.md` flags a **Variance Void** (System Goalie OUT) and the proposed bet is a **full‑game Under** or **opponent Team Total Under**, then:
     - **VERDICT:** RED — **HARD PASS**.

3. **Data Integrity Missing**
   - If the relevant `research/YYYY-MM-DD-*-analysis.md` or `research/YYYY-MM-DD-slate-data.md` is **missing** or clearly **out of date**, the Agent must:
     - State that data freshness is not confirmed.
     - Either **downgrade** to YELLOW with a warning, or **decline** to issue a GREEN verdict.

---

## 4. OPERATIONAL SHORTCUTS

When the Project Lead issues a command like:

> "Run the Protocol on Bedard vs [Team] tonight."

The Agent must:

1. Identify:
   - Opponent Team → load `nhl/team-dna/[opponent].md`
   - Player Team → load `nhl/team-dna/[player-team].md` if it exists
   - Current date's slate file → `research/YYYY-MM-DD-slate-data.md` (if present)
2. Execute the **Triangulation Rule** (Macro → Micro → Asset).
3. Respond using the **Response Format** above, ending with a clear **GREEN / YELLOW / RED** verdict.

---

Version: 1.0 — APEXVIPER MASTER QUERY PROTOCOL  
Owner: Project Lead (Bam082608)  
Purpose: Force every analysis to consult Macro Intelligence, Team DNA, and Slate Data before speaking.
