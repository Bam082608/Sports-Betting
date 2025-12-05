#!/usr/bin/env python3
"""
ApexViper Power Index (API) - Team & Player Advantage Engine
Author: ApexViper

This tool ingests:
- Master Team Matrix (CSV or JSON)
- Optional Team PP Metrics (CSV)
- Optional Player PPSS Metrics (CSV)

It outputs:
- enriched_matrix.csv
- enriched_matrix.json
- On-screen ranked GREEN/YELLOW/RED signals

Run:
    python apexviper_power_index.py --input master_matrix.csv
"""

import argparse
import pandas as pd
import numpy as np
import json
import sys


# --------------------------
# HELPER FUNCTIONS
# --------------------------
def safe_div(a, b):
    """Avoid division errors."""
    if b == 0 or b is None or pd.isna(b):
        return 0
    return a / b


def grade_signal(value, low, mid, high):
    """
    Returns RED / YELLOW / GREEN depending on thresholds.
    Higher = better
    """
    if value >= high:
        return "GREEN"
    if value >= mid:
        return "YELLOW"
    return "RED"


# --------------------------
# CORE ENGINE
# --------------------------
def compute_power_index(df_matrix, df_pp_team=None, df_pp_player=None):

    # If no PP data was supplied, create placeholder zeros
    if df_pp_team is None:
        df_pp_team = pd.DataFrame(columns=["team", "pp_attempts", "pp_goals"])
    if df_pp_player is None:
        df_pp_player = pd.DataFrame(columns=["player", "team", "pp_shots", "pp_expected"])

    # Merge team PP metrics if available
    if "team" in df_pp_team.columns:
        df_matrix = df_matrix.merge(df_pp_team, on="team", how="left")
    else:
        df_matrix["pp_attempts"] = np.nan
        df_matrix["pp_goals"] = np.nan

    # Fill missing
    df_matrix["pp_attempts"] = df_matrix["pp_attempts"].fillna(0)
    df_matrix["pp_goals"] = df_matrix["pp_goals"].fillna(0)

    # Derived team-level PP stats
    df_matrix["pp_conversion"] = df_matrix.apply(
        lambda r: safe_div(r["pp_goals"], r["pp_attempts"]), axis=1
    )

    # Merge player PPSS if available (sum by team)
    if "team" in df_pp_player.columns:
        grouped = df_pp_player.groupby("team").agg(
            team_pp_shots=("pp_shots", "sum"),
            team_pp_expected=("pp_expected", "sum"),
        ).reset_index()
        df_matrix = df_matrix.merge(grouped, on="team", how="left")
    else:
        df_matrix["team_pp_shots"] = 0
        df_matrix["team_pp_expected"] = 0

    # Fill missing
    df_matrix["team_pp_shots"] = df_matrix["team_pp_shots"].fillna(0)
    df_matrix["team_pp_expected"] = df_matrix["team_pp_expected"].fillna(0)

    # APEXVIPER POWER INDEX score calculation
    df_matrix["API_score"] = (
        (df_matrix["team_pp_expected"] * 0.5)
        + (df_matrix["team_pp_shots"] * 0.3)
        + (df_matrix["pp_conversion"] * 0.2)
    )

    # Grade signal
    df_matrix["API_signal"] = df_matrix["API_score"].apply(
        lambda x: grade_signal(x, low=0.15, mid=0.25, high=0.4)
    )

    return df_matrix


# --------------------------
# MAIN RUNTIME
# --------------------------
def main():

    parser = argparse.ArgumentParser(description="ApexViper Power Index Engine")
    parser.add_argument("--input", required=True, help="Master matrix CSV or JSON")
    parser.add_argument("--pp_team", help="Optional team power play CSV")
    parser.add_argument("--pp_player", help="Optional player PPSS CSV")

    args = parser.parse_args()

    # Load main file
    if args.input.endswith(".csv"):
        df_matrix = pd.read_csv(args.input)
    elif args.input.endswith(".json"):
        df_matrix = pd.read_json(args.input)
    else:
        sys.exit("ERROR: Input must be CSV or JSON.")

    # Optional: Team PP
    df_pp_team = None
    if args.pp_team:
        df_pp_team = pd.read_csv(args.pp_team)

    # Optional: Player PP
    df_pp_player = None
    if args.pp_player:
        df_pp_player = pd.read_csv(args.pp_player)

    # Compute index
    enriched = compute_power_index(df_matrix, df_pp_team, df_pp_player)

    # Save outputs
    enriched.to_csv("enriched_matrix.csv", index=False)
    enriched.to_json("enriched_matrix.json", orient="records")

    # Print summary
    print("\n=== TOP GREEN SIGNAL TEAMS ===")
    greens = enriched[enriched["API_signal"] == "GREEN"].sort_values("API_score", ascending=False)
    print(greens[["team", "API_score", "team_pp_expected", "pp_conversion"]].head(10))

    print("\nOutput Saved:")
    print(" - enriched_matrix.csv")
    print(" - enriched_matrix.json")


if __name__ == "__main__":
    main()
