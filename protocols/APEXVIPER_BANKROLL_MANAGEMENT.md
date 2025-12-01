# 💰 APEXVIPER BANKROLL MANAGEMENT SYSTEM v1.0
**Owner:** Project Lead (Bam082608)  
**Directive:** Systematic bankroll tracking, unit sizing, and drawdown protection.

---

## 1. CURRENT BANKROLL SNAPSHOT

**Last Updated:** ____________

| Metric | Value |
|--------|-------|
| **Starting Bankroll** | $650.00 |
| **Current Bankroll** | $_______ |
| **Unit Size (1.5%)** | $10.00 |
| **Daily Max Risk (3%)** | $19.50 |
| **Weekly Max Risk (10%)** | $65.00 |

### Daily Snapshot Template
```
Date: ____________
Opening Bankroll: $_______
Bets Placed Today: $_______
Results: W/L/Push
Closing Bankroll: $_______
Daily P/L: $_______
```

---

## 2. UNIT SIZE CALCULATION

**Standard Unit = 1.5% of Bankroll**

| Bankroll | Unit Size (1.5%) | Half Unit | Double Unit |
|----------|------------------|-----------|-------------|
| $500 | $7.50 | $3.75 | $15.00 |
| $600 | $9.00 | $4.50 | $18.00 |
| **$650** | **$10.00** | **$5.00** | **$20.00** |
| $700 | $10.50 | $5.25 | $21.00 |
| $800 | $12.00 | $6.00 | $24.00 |
| $1,000 | $15.00 | $7.50 | $30.00 |
| $1,500 | $22.50 | $11.25 | $45.00 |
| $2,000 | $30.00 | $15.00 | $60.00 |

### Quick Unit Lookup
```
Unit Size = Bankroll × 0.015
Half Unit = Bankroll × 0.0075
Double Unit = Bankroll × 0.03
```

---

## 3. UNIT SIZING ADJUSTMENT RULES

### When to INCREASE Unit Size

| Condition | Action | New Unit Calculation |
|-----------|--------|---------------------|
| Bankroll grows 15%+ | Recalculate units | New bankroll × 1.5% |
| Hit 3 consecutive winning days | Lock in gains, recalculate | New bankroll × 1.5% |
| Reach milestone ($700, $1000, etc.) | Milestone adjustment | Use new tier |

**INCREASE TRIGGERS:**
- [ ] Bankroll reaches $750 → Recalculate to $11.25 unit
- [ ] Bankroll reaches $1,000 → Recalculate to $15.00 unit
- [ ] Bankroll reaches $1,500 → Recalculate to $22.50 unit

### When to DECREASE Unit Size

| Condition | Action | New Unit Calculation |
|-----------|--------|---------------------|
| Bankroll drops 10% | Immediate recalculation | New bankroll × 1.5% |
| 3 consecutive losing days | Reduce by 25% | Current unit × 0.75 |
| Hit stop-loss trigger | Emergency reduction | See Section 5 |

**DECREASE TRIGGERS:**
- [ ] Bankroll drops to $585 (10% loss) → Recalculate to $8.75 unit
- [ ] Bankroll drops to $520 (20% loss) → Recalculate to $7.80 unit
- [ ] Emergency stop-loss hit → See Section 5

---

## 4. WEEKLY P&L TRACKING TABLE

### Week of: ____________

| Day | Opening | Bets Placed | Total Wagered | Won | Lost | Closing | Daily P/L |
|-----|---------|-------------|---------------|-----|------|---------|-----------|
| Mon | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Tue | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Wed | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Thu | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Fri | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Sat | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| Sun | $______ | ______ | $______ | $______ | $______ | $______ | $______ |
| **TOTALS** | | | | | | | **$______** |

### Weekly Summary
```
Week Starting Bankroll: $_______
Week Ending Bankroll: $_______
Total Bets: _______
Win Rate: ______%
Weekly P/L: $_______
Weekly ROI: ______%
```

---

## 5. DRAWDOWN PROTECTION RULES

### Daily Stop-Loss Limits

| Bankroll Level | Max Daily Loss | Action When Hit |
|----------------|----------------|-----------------|
| $650+ | $20 (3% of bankroll) | Stop betting for day |
| $500-$649 | $15 (3% of bankroll) | Stop betting for day |
| $400-$499 | $12 (3% of bankroll) | Stop betting for day |
| Below $400 | $10 flat | Stop betting, reassess system |

### Weekly Stop-Loss Limits

| Bankroll Level | Max Weekly Loss | Action When Hit |
|----------------|-----------------|-----------------|
| $650+ | $65 (10% of bankroll) | Forced cooldown (2 days) |
| $500-$649 | $50 (10% of bankroll) | Forced cooldown (2 days) |
| Below $500 | $40 flat | Forced cooldown (3 days) |

### Emergency Stop-Loss (CIRCUIT BREAKER)

**TRIGGER:** Bankroll drops 25% from peak in any 7-day period

**ACTIONS:**
1. 🛑 STOP all betting immediately
2. 📝 Document what went wrong
3. ⏳ Mandatory 5-day cooldown period
4. 🔍 Full system review before resuming
5. 📉 Reduce unit size by 50% when resuming

---

## 6. FORCED COOLDOWN PERIODS

### Automatic Cooldown Triggers

| Trigger | Cooldown Duration | Resume Conditions |
|---------|-------------------|-------------------|
| Daily stop-loss hit | Rest of day | Next day, fresh slate |
| Weekly stop-loss hit | 2 full days | 3rd day, reduced units |
| 3 consecutive losing days | 1 full day | After review, reduced units |
| Circuit breaker (25% drop) | 5 full days | Full system review required |
| Emotional tilt detected | Rest of day | Must document trigger |

### Cooldown Protocol
- [ ] Document why cooldown was triggered
- [ ] No bets placed during cooldown (no exceptions)
- [ ] Review recent bets for pattern issues
- [ ] Adjust unit size if necessary before resuming
- [ ] Return with clear head and fresh perspective

---

## 7. MONTHLY BANKROLL REVIEW

### Month: ____________

| Week | Starting | Ending | P/L | Win Rate | Notes |
|------|----------|--------|-----|----------|-------|
| Week 1 | $______ | $______ | $______ | ______% | |
| Week 2 | $______ | $______ | $______ | ______% | |
| Week 3 | $______ | $______ | $______ | ______% | |
| Week 4 | $______ | $______ | $______ | ______% | |
| **MONTH** | **$______** | **$______** | **$______** | **______%** | |

### Monthly Assessment Questions
1. Did I hit any stop-loss triggers? ______
2. Largest single-day loss: $_______
3. Largest single-day win: $_______
4. Average daily P/L: $_______
5. Most profitable day of week: _______
6. Least profitable day of week: _______

---

## 8. STAKE SIZING BY CONFIDENCE TIER

| Tier | Confidence | Stake | Example ($650 bankroll) |
|------|------------|-------|-------------------------|
| **A (Core)** | High (80%+) | 1.0 unit | $10.00 |
| **B (Standard)** | Medium (60-80%) | 0.5 unit | $5.00 |
| **C (Value)** | Lower (40-60%) | 0.25 unit | $2.50 |
| **D (Lottery)** | Longshot (<40%) | 0.1 unit | $1.00 |

### Max Daily Allocation by Tier

| Tier | Max # of Bets | Max Total Stake |
|------|---------------|-----------------|
| A (Core) | 2 per day | $20.00 |
| B (Standard) | 3 per day | $15.00 |
| C (Value) | 4 per day | $10.00 |
| D (Lottery) | 2 per day | $2.00 |
| **TOTAL** | **11 max** | **$47.00 max** |

---

## 9. WITHDRAWAL MILESTONES

| Milestone | Bankroll | Action | Withdrawal Amount |
|-----------|----------|--------|-------------------|
| **Level 1** | $1,000 | First withdrawal | $200 (profit lock) |
| **Level 2** | $1,500 | Second withdrawal | $300 (profit lock) |
| **Level 3** | $2,500 | Third withdrawal | $500 (profit lock) |
| **Level 4** | $5,000 | Major withdrawal | $1,500 (30% of bankroll) |
| **Level 5** | $10,000+ | Regular withdrawals | 20% monthly |

**Rule:** Never withdraw below your operating minimum ($500).

---

## 10. QUICK REFERENCE CARD

### Current Status ($650 Bankroll)
```
┌─────────────────────────────────────┐
│ UNIT SIZE:           $10.00        │
│ HALF UNIT:           $5.00         │
│ MAX DAILY RISK:      $19.50 (3%)   │
│ DAILY STOP-LOSS:     $20.00        │
│ WEEKLY STOP-LOSS:    $65.00        │
│ CIRCUIT BREAKER:     $162.50 (25%) │
└─────────────────────────────────────┘
```

### Emergency Numbers
- **Daily Stop-Loss:** If down $20, STOP
- **Weekly Stop-Loss:** If down $65, COOLDOWN 2 days
- **Circuit Breaker:** If bankroll hits $487.50, STOP 5 days

---

## 🎯 CROSS-REFERENCE

This protocol integrates with:
- `tracking/bankroll.md` - Daily bankroll updates
- `tracking/bet-log.md` - Individual bet tracking
- `protocols/APEXVIPER_PORTFOLIO_CONSTRUCTION.md` - Stake sizing

---

**Version:** 1.0  
**Owner:** Project Lead (Bam082608)  
**Purpose:** Protect bankroll through systematic risk management and drawdown controls.
