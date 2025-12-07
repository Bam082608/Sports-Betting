# THE WATCHTOWER: SHOT MATRIX DECISION ENGINE (v1.0)

## Overview
The Watchtower is a decision engine designed to automate ticket architecture based on game scripts, totals, and player statuses. It classifies games into specific tactical categories ("THE GRIND", "THE SIEGE", "ONE-MAN ARMY", "THE SHOOTOUT") and prescribes specific betting protocols for each.

## Usage
This tool is a Python script that can be executed directly. It contains a `GameIntel` class for defining game parameters and a `run_watchtower_protocol` function to analyze and output the strategy.

To run the engine:
```bash
python3 nhl/tools/watchtower_engine/watchtower_engine.py
```

## Input Data
The script currently contains hardcoded input data for a specific slate. To use it for a new slate, update the `INPUT DATA` section in `watchtower_engine.py` with the relevant game intelligence.

## Protocols
- **THE GRIND (Type 1):** Low Total + Elite Defense. Focus on Unders.
- **THE SIEGE / CHAOS (Type 4):** High Total + Backup Goalie. Focus on Overs and Props.
- **ONE-MAN ARMY (Type 3):** Elite Star + Bad Defense. Ladder betting on the star.
- **THE SHOOTOUT (Type 2):** High Volume, Distributed Offense. "Star & Floor" strategy.
