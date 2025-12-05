# 🐍 ApexViper Power Index (API)

The **ApexViper Power Index** is an advantage engine used to quantify
team-level and player-level power play strength using:

- Team PP attempts/goals
- Player PP shot share (PPSS)
- Expected PP shot rates
- Derived conversion percentages
- Weighted scoring model
- Automatic GREEN/YELLOW/RED signal system

---

## 🚀 How to Run

### 1️⃣ Install dependencies

pip install pandas numpy

### 2️⃣ Run the engine

python apexviper_power_index.py --input sample_master_matrix.csv

### Optional (recommended):

python apexviper_power_index.py
--input sample_master_matrix.csv
--pp_team sample_team_pp.csv
--pp_player sample_player_ppss.csv

---

## 📤 Outputs

| File | Description |
|------|-------------|
| **enriched_matrix.csv** | Full computed model with all signals |
| **enriched_matrix.json** | Same, but JSON for web tools |
| **Terminal Summary** | Top GREEN teams ranked |

---

## 🧮 API Model Breakdown

**API Score =**

team_pp_expected * 0.5

team_pp_shots * 0.3

pp_conversion * 0.2


**Signal Rules:**

| Score | Signal |
|-------|--------|
| ≥ 0.40 | GREEN |
| ≥ 0.25 | YELLOW |
| < 0.25 | RED |

---

## ✔ Example Input Format
### sample_master_matrix.csv

team,gf,ga,shots_for,shots_against BOS,88,61,900,840 TOR,95,84,880,899 DET,77,91,875,921

### sample_team_pp.csv

team,pp_attempts,pp_goals BOS,72,19 TOR,68,17 DET,64,10

### sample_player_ppss.csv

player,team,pp_shots,pp_expected Pastrnak,BOS,34,4.3 Marchand,BOS,21,2.1 Matthews,TOR,29,3.7

---

## 📘 Summary
You now have:

✔ A full scoring engine
✔ A signal-based rating system
✔ Ready-to-run scripts
✔ Example inputs
✔ CSV + JSON output formats
✔ GitHub-ready structure

This repository can be expanded into:

- A live-updating dashboard
- Betting projection tool
- Simulation engine
- Team-level nightly forecast system
