#!/usr/bin/env python3
"""
APEXVIPER: OPERATION DECEMBER 5
Logic Engine v2.0
"""

import pandas as pd
import numpy as np
import argparse
import sys
from datetime import datetime

# --- CONFIGURATION ---
TARGET_SHOTS = 2.5  # The standard line we are looking to beat
CHASE_BONUS = 0.15  # Bonus points for "Chase Mode"
BLOWOUT_PENALTY = -0.20  # Penalty for "Blowout Risk"
RESISTANCE_PENALTY = -0.10 # Penalty for High Block Teams (SJS)

def parse_last_five(shot_string):
    """Converts '3|4|4|5|4' into a list of integers and returns average."""
    try:
        shots = [int(x) for x in shot_string.split('|')]
        return np.mean(shots), sum(1 for x in shots if x >= TARGET_SHOTS)
    except:
        return 0, 0

def calculate_apex_score(row):
    """
    The Secret Sauce.
    Combines Volume (Last 5) + Opportunity (TOI) + Script Intelligence.
    """
    # 1. Base Volume Score (0.0 to 1.0)
    avg_shots, hit_count = parse_last_five(row['last_5_shots'])
    volume_score = (avg_shots / 5.0)  # Normalize to 5 shots

    # 2. Consistency Bonus
    consistency_score = (hit_count / 5.0) * 0.2

    # 3. Script Adjustments (The Intelligent Layer)
    script_mod = 0
    if row['script_tag'] == 'CHASE_MODE':
        script_mod += CHASE_BONUS
    elif row['script_tag'] == 'HISTORY_CHASE':
        script_mod += CHASE_BONUS
    elif row['script_tag'] == 'BLOWOUT_RISK':
        script_mod += BLOWOUT_PENALTY
    elif row['script_tag'] == 'SUPPRESSED':
        script_mod += -0.15

    # 4. Resistance Adjustment (The "Wall" Check)
    resistance_mod = 0
    if row['resistance_grade'] == 'HIGH': # e.g. San Jose blocking shots
        resistance_mod += RESISTANCE_PENALTY
    elif row['resistance_grade'] == 'LOW': # e.g. Anaheim bleeding shots
        resistance_mod += 0.05 # Bonus for soft defense

    final_score = volume_score + consistency_score + script_mod + resistance_mod
    return round(final_score, 3)

def get_signal(score):
    if score >= 0.75: return "🟢 GREEN (ELITE)"
    if score >= 0.60: return "🟡 YELLOW (PLAYABLE)"
    return "🔴 RED (AVOID)"

def main():
    print(f"🐍 APEXVIPER INITIALIZING... {datetime.now().strftime('%H:%M:%S')}")

    try:
        df = pd.read_csv("apexviper_master_data.csv")
    except FileNotFoundError:
        sys.exit("❌ ERROR: Data file 'apexviper_master_data.csv' not found.")

    # Apply Logic
    df['APEX_SCORE'] = df.apply(calculate_apex_score, axis=1)
    df['SIGNAL'] = df['APEX_SCORE'].apply(get_signal)

    # Sort by Score (Best to Worst)
    df = df.sort_values(by='APEX_SCORE', ascending=False)

    # OUTPUT
    print("\n--- 🎯 TARGET PRIORITY LIST ---")
    print(df[['player', 'team', 'script_tag', 'APEX_SCORE', 'SIGNAL']].to_string(index=False))

    # Save Enriched Data
    df.to_csv("apexviper_results.csv", index=False)
    print("\n✅ ANALYSIS COMPLETE. Results saved to 'apexviper_results.csv'")

if __name__ == "__main__":
    main()
