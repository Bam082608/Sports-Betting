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
    python apexviper_power_index.py --input master_matrix.csv --pp_team team_pp.csv --pp_player player_pp.csv
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

# --- LOGGING CONFIGURATION ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / f'power_index_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
SIGNAL_THRESHOLDS = {"low": 0.15, "mid": 0.25, "high": 0.40}


def safe_div(a: float, b: float) -> float:
    """
    Safely divide two numbers, avoiding division by zero.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Division result, or 0 if denominator is zero/invalid

    Examples:
        >>> safe_div(10, 2)
        5.0
        >>> safe_div(10, 0)
        0.0
    """
    if b == 0 or b is None or pd.isna(b):
        logger.debug(f"Safe division: {a}/{b} -> returning 0")
        return 0.0
    return float(a / b)


def grade_signal(value: float, low: float = 0.15, mid: float = 0.25, high: float = 0.40) -> str:
    """
    Convert numeric value to traffic light signal.

    Args:
        value: Numeric score to grade
        low: Minimum threshold for YELLOW
        mid: Minimum threshold for YELLOW (upper bound)
        high: Minimum threshold for GREEN

    Returns:
        Signal grade: RED, YELLOW, or GREEN

    Examples:
        >>> grade_signal(0.50)
        'GREEN'
        >>> grade_signal(0.20)
        'YELLOW'
        >>> grade_signal(0.10)
        'RED'
    """
    if value >= high:
        return "GREEN"
    if value >= mid:
        return "YELLOW"
    return "RED"


def validate_input_file(file_path: Path, file_type: str) -> pd.DataFrame:
    """
    Validate and load input file.

    Args:
        file_path: Path to file
        file_type: Description of file type for error messages

    Returns:
        Loaded DataFrame

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is invalid
    """
    if not file_path.exists():
        raise FileNotFoundError(f"{file_type} file not found: {file_path}")

    try:
        if file_path.suffix == ".csv":
            df = pd.read_csv(file_path)
            logger.info(f"Loaded {len(df)} rows from {file_type} CSV: {file_path}")
        elif file_path.suffix == ".json":
            df = pd.read_json(file_path)
            logger.info(f"Loaded {len(df)} rows from {file_type} JSON: {file_path}")
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

        if df.empty:
            logger.warning(f"{file_type} file is empty: {file_path}")

        return df

    except Exception as e:
        logger.error(f"Failed to load {file_type} file {file_path}: {e}")
        raise


def compute_power_index(
    df_matrix: pd.DataFrame,
    df_pp_team: Optional[pd.DataFrame] = None,
    df_pp_player: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """
    Compute ApexViper Power Index scores for teams.

    Combines team power play metrics with player PPSS data to calculate
    overall power index scores and signal grades.

    Args:
        df_matrix: Main team matrix DataFrame
        df_pp_team: Optional team power play metrics
        df_pp_player: Optional player PPSS metrics

    Returns:
        DataFrame with API_score and API_signal columns added

    Raises:
        KeyError: If required columns are missing
    """
    logger.info("Computing Power Index scores...")

    # Validate main matrix has 'team' column
    if "team" not in df_matrix.columns:
        raise KeyError("Main matrix must contain 'team' column")

    # Initialize empty DataFrames if not provided
    if df_pp_team is None:
        logger.info("No team PP data provided, using empty DataFrame")
        df_pp_team = pd.DataFrame(columns=["team", "pp_attempts", "pp_goals"])

    if df_pp_player is None:
        logger.info("No player PPSS data provided, using empty DataFrame")
        df_pp_player = pd.DataFrame(columns=["player", "team", "pp_shots", "pp_expected"])

    # Merge team PP metrics if available
    if "team" in df_pp_team.columns and not df_pp_team.empty:
        logger.info(f"Merging {len(df_pp_team)} team PP records")
        df_matrix = df_matrix.merge(df_pp_team, on="team", how="left")
    else:
        df_matrix["pp_attempts"] = np.nan
        df_matrix["pp_goals"] = np.nan

    # Fill missing values
    df_matrix["pp_attempts"] = df_matrix["pp_attempts"].fillna(0)
    df_matrix["pp_goals"] = df_matrix["pp_goals"].fillna(0)

    # Derived team-level PP stats
    logger.info("Calculating PP conversion rates...")
    df_matrix["pp_conversion"] = df_matrix.apply(lambda r: safe_div(r["pp_goals"], r["pp_attempts"]), axis=1)

    # Merge player PPSS if available (sum by team)
    if "team" in df_pp_player.columns and not df_pp_player.empty:
        logger.info(f"Aggregating {len(df_pp_player)} player PPSS records")
        grouped = (
            df_pp_player.groupby("team")
            .agg(
                team_pp_shots=("pp_shots", "sum"),
                team_pp_expected=("pp_expected", "sum"),
            )
            .reset_index()
        )
        df_matrix = df_matrix.merge(grouped, on="team", how="left")
    else:
        df_matrix["team_pp_shots"] = 0
        df_matrix["team_pp_expected"] = 0

    # Fill missing
    df_matrix["team_pp_shots"] = df_matrix["team_pp_shots"].fillna(0)
    df_matrix["team_pp_expected"] = df_matrix["team_pp_expected"].fillna(0)

    # APEXVIPER POWER INDEX score calculation
    logger.info("Calculating API scores...")
    df_matrix["API_score"] = (
        (df_matrix["team_pp_expected"] * 0.5) + (df_matrix["team_pp_shots"] * 0.3) + (df_matrix["pp_conversion"] * 0.2)
    )

    # Grade signal
    df_matrix["API_signal"] = df_matrix["API_score"].apply(lambda x: grade_signal(x, **SIGNAL_THRESHOLDS))

    # Log statistics
    green_count = len(df_matrix[df_matrix["API_signal"] == "GREEN"])
    yellow_count = len(df_matrix[df_matrix["API_signal"] == "YELLOW"])
    red_count = len(df_matrix[df_matrix["API_signal"] == "RED"])

    logger.info(f"API Score distribution: GREEN={green_count}, YELLOW={yellow_count}, RED={red_count}")

    return df_matrix


def main() -> int:
    """
    Main execution function.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    logger.info(f"🐍 ApexViper Power Index Engine starting... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    parser = argparse.ArgumentParser(
        description="ApexViper Power Index Engine - Team Advantage Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --input master_matrix.csv
  %(prog)s --input master_matrix.json --pp_team team_pp.csv
  %(prog)s --input master_matrix.csv --pp_team team_pp.csv --pp_player player_pp.csv
  %(prog)s --input data.csv --output-csv results.csv --output-json results.json
        """,
    )
    parser.add_argument("--input", required=True, help="Master matrix CSV or JSON file (required)")
    parser.add_argument("--pp_team", help="Optional team power play CSV file")
    parser.add_argument("--pp_player", help="Optional player PPSS CSV file")
    parser.add_argument(
        "--output-csv",
        default="enriched_matrix.csv",
        help="Output CSV filename (default: enriched_matrix.csv)",
    )
    parser.add_argument(
        "--output-json",
        default="enriched_matrix.json",
        help="Output JSON filename (default: enriched_matrix.json)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose debug logging")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")

    # Load main matrix file
    try:
        input_path = Path(args.input)
        df_matrix = validate_input_file(input_path, "Main matrix")

    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Failed to load input file: {e}")
        print(f"❌ ERROR: {e}")
        return 1

    # Optional: Load Team PP data
    df_pp_team = None
    if args.pp_team:
        try:
            pp_team_path = Path(args.pp_team)
            df_pp_team = validate_input_file(pp_team_path, "Team PP")

            # Validate required columns
            required_cols = ["team", "pp_attempts", "pp_goals"]
            missing = [col for col in required_cols if col not in df_pp_team.columns]
            if missing:
                raise ValueError(f"Team PP file missing required columns: {missing}")

        except (FileNotFoundError, ValueError) as e:
            logger.error(f"Team PP file error: {e}")
            print(f"❌ ERROR: {e}")
            return 1

    # Optional: Load Player PPSS data
    df_pp_player = None
    if args.pp_player:
        try:
            pp_player_path = Path(args.pp_player)
            df_pp_player = validate_input_file(pp_player_path, "Player PPSS")

            # Validate required columns
            required_cols = ["team", "pp_shots", "pp_expected"]
            missing = [col for col in required_cols if col not in df_pp_player.columns]
            if missing:
                raise ValueError(f"Player PPSS file missing required columns: {missing}")

        except (FileNotFoundError, ValueError) as e:
            logger.error(f"Player PPSS file error: {e}")
            print(f"❌ ERROR: {e}")
            return 1

    # Compute power index
    try:
        enriched = compute_power_index(df_matrix, df_pp_team, df_pp_player)

    except Exception as e:
        logger.error(f"Failed to compute power index: {e}")
        print(f"❌ ERROR: Power index calculation failed: {e}")
        return 1

    # Save outputs
    try:
        output_csv = Path(args.output_csv)
        output_json = Path(args.output_json)

        enriched.to_csv(output_csv, index=False)
        logger.info(f"Saved CSV output to {output_csv}")

        enriched.to_json(output_json, orient="records", indent=2)
        logger.info(f"Saved JSON output to {output_json}")

    except Exception as e:
        logger.error(f"Failed to save output files: {e}")
        print(f"❌ ERROR: Failed to save results: {e}")
        return 1

    # Print summary to console
    print("\n" + "=" * 80)
    print("🟢 TOP GREEN SIGNAL TEAMS (ELITE POWER INDEX)")
    print("=" * 80)
    greens = enriched[enriched["API_signal"] == "GREEN"].sort_values("API_score", ascending=False)

    if not greens.empty:
        display_cols = ["team", "API_score"]
        # Include PP metrics if they exist
        optional_cols = ["team_pp_expected", "pp_conversion"]
        for col in optional_cols:
            if col in greens.columns:
                display_cols.append(col)

        print(greens[display_cols].head(10).to_string(index=False))
    else:
        print("No GREEN signal teams found.")

    print("\n" + "=" * 80)
    print(f"✅ Output saved:")
    print(f"   📄 CSV:  {output_csv}")
    print(f"   📄 JSON: {output_json}")
    print("=" * 80)

    # Summary statistics
    print(f"\n📊 SIGNAL DISTRIBUTION:")
    print(f"   🟢 GREEN:  {len(enriched[enriched['API_signal'] == 'GREEN'])}")
    print(f"   🟡 YELLOW: {len(enriched[enriched['API_signal'] == 'YELLOW'])}")
    print(f"   🔴 RED:    {len(enriched[enriched['API_signal'] == 'RED'])}")

    logger.info("Power Index calculation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
