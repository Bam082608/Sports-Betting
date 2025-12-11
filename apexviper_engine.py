#!/usr/bin/env python3
"""
APEXVIPER: OPERATION DECEMBER 5
Logic Engine v2.0

This engine calculates APEX scores for player prop betting opportunities by combining:
- Volume (last 5 games shot data)
- Consistency (hit rate on target)
- Script intelligence (game narrative adjustments)
- Resistance factors (opponent defensive strength)
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
import pandas as pd

# --- LOGGING CONFIGURATION ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / f'apexviper_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
TARGET_SHOTS = 2.5  # The standard line we are looking to beat
CHASE_BONUS = 0.15  # Bonus points for "Chase Mode"
BLOWOUT_PENALTY = -0.20  # Penalty for "Blowout Risk"
RESISTANCE_PENALTY = -0.10  # Penalty for High Block Teams (SJS)

# Valid values for validation
VALID_RESISTANCE_GRADES = {"LOW", "MODERATE", "HIGH"}
VALID_SCRIPT_TAGS = {
    "CHASE_MODE",
    "HISTORY_CHASE",
    "BLOWOUT_RISK",
    "SUPPRESSED",
    "NEUTRAL",
    "LOW_PACE",
}


def parse_last_five(shot_string: str) -> Tuple[float, int]:
    """
    Converts shot string into average and hit count.

    Args:
        shot_string: Pipe-delimited string like '3|4|4|5|4'

    Returns:
        Tuple of (average_shots, hit_count) where hit_count is number of games >= TARGET_SHOTS

    Raises:
        ValueError: If shot_string format is invalid

    Examples:
        >>> parse_last_five('3|4|4|5|4')
        (4.0, 4)
        >>> parse_last_five('2|2|7|3|5')
        (3.8, 2)
    """
    if not shot_string or not isinstance(shot_string, str):
        logger.warning(f"Invalid shot_string type or empty: {shot_string}")
        return 0.0, 0

    try:
        shots = [int(x.strip()) for x in shot_string.split("|")]

        if len(shots) != 5:
            logger.warning(f"Expected 5 shots, got {len(shots)} in: {shot_string}")
            # Still process, but log the warning

        if any(s < 0 for s in shots):
            logger.error(f"Negative shot counts found in: {shot_string}")
            return 0.0, 0

        avg_shots = float(np.mean(shots))
        hit_count = sum(1 for x in shots if x >= TARGET_SHOTS)

        logger.debug(f"Parsed {shot_string} -> avg={avg_shots:.2f}, hits={hit_count}")
        return avg_shots, hit_count

    except ValueError as e:
        logger.error(f"Failed to parse shot string '{shot_string}': {e}")
        return 0.0, 0
    except Exception as e:
        logger.error(f"Unexpected error parsing shot string '{shot_string}': {e}")
        raise


def calculate_apex_score(row: pd.Series) -> float:
    """
    Calculate APEX score combining volume, consistency, script, and resistance.

    The Secret Sauce combines:
    1. Base Volume Score (0.0 to 1.0) - normalized average shots
    2. Consistency Bonus - hit rate multiplier
    3. Script Adjustments - narrative-based modifiers
    4. Resistance Adjustment - opponent defensive strength

    Args:
        row: DataFrame row containing player data

    Returns:
        APEX score (typically 0.0 to 1.0, can exceed with bonuses)

    Raises:
        KeyError: If required columns are missing
    """
    try:
        # 1. Base Volume Score (0.0 to 1.0)
        avg_shots, hit_count = parse_last_five(row["last_5_shots"])
        volume_score = avg_shots / 5.0  # Normalize to 5 shots

        # 2. Consistency Bonus
        consistency_score = (hit_count / 5.0) * 0.2

        # 3. Script Adjustments (The Intelligent Layer)
        script_mod = 0.0
        script_tag = row.get("script_tag", "NEUTRAL").upper()

        # Validate script tag
        if script_tag not in VALID_SCRIPT_TAGS:
            logger.warning(f"Invalid script_tag '{script_tag}' for {row.get('player', 'Unknown')}. Using NEUTRAL.")
            script_tag = "NEUTRAL"

        if script_tag == "CHASE_MODE":
            script_mod += CHASE_BONUS
            logger.debug(f"Applied CHASE_MODE bonus: +{CHASE_BONUS}")
        elif script_tag == "HISTORY_CHASE":
            script_mod += CHASE_BONUS
            logger.debug(f"Applied HISTORY_CHASE bonus: +{CHASE_BONUS}")
        elif script_tag == "BLOWOUT_RISK":
            script_mod += BLOWOUT_PENALTY
            logger.debug(f"Applied BLOWOUT_RISK penalty: {BLOWOUT_PENALTY}")
        elif script_tag == "SUPPRESSED":
            script_mod += -0.15
            logger.debug(f"Applied SUPPRESSED penalty: -0.15")

        # 4. Resistance Adjustment (The "Wall" Check)
        resistance_mod = 0.0
        resistance_grade = row.get("resistance_grade", "MODERATE").upper()

        # Validate resistance grade
        if resistance_grade not in VALID_RESISTANCE_GRADES:
            logger.warning(
                f"Invalid resistance_grade '{resistance_grade}' for {row.get('player', 'Unknown')}. Using MODERATE."
            )
            resistance_grade = "MODERATE"

        if resistance_grade == "HIGH":  # e.g. San Jose blocking shots
            resistance_mod += RESISTANCE_PENALTY
            logger.debug(f"Applied HIGH resistance penalty: {RESISTANCE_PENALTY}")
        elif resistance_grade == "LOW":  # e.g. Anaheim bleeding shots
            resistance_mod += 0.05  # Bonus for soft defense
            logger.debug(f"Applied LOW resistance bonus: +0.05")

        final_score = volume_score + consistency_score + script_mod + resistance_mod

        logger.info(
            f"{row.get('player', 'Unknown')}: "
            f"vol={volume_score:.3f} + cons={consistency_score:.3f} + "
            f"script={script_mod:+.3f} + resist={resistance_mod:+.3f} = {final_score:.3f}"
        )

        return round(final_score, 3)

    except KeyError as e:
        logger.error(f"Missing required column in data: {e}")
        raise
    except Exception as e:
        logger.error(f"Error calculating APEX score for row: {e}")
        raise


def get_signal(score: float) -> str:
    """
    Convert APEX score to signal rating.

    Args:
        score: APEX score value

    Returns:
        Signal string with emoji indicator
    """
    if score >= 0.75:
        return "🟢 GREEN (ELITE)"
    if score >= 0.60:
        return "🟡 YELLOW (PLAYABLE)"
    return "🔴 RED (AVOID)"


def validate_dataframe(df: pd.DataFrame) -> bool:
    """
    Validate input DataFrame has required columns and data quality.

    Args:
        df: Input DataFrame to validate

    Returns:
        True if valid, raises ValueError if invalid

    Raises:
        ValueError: If validation fails
    """
    # Check for empty DataFrame first
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    required_columns = [
        "player",
        "team",
        "last_5_shots",
        "script_tag",
        "resistance_grade",
    ]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Check for null values in critical columns
    null_counts = df[required_columns].isnull().sum()
    if null_counts.any():
        logger.warning(f"Null values found in columns: {null_counts[null_counts > 0].to_dict()}")

    logger.info(f"DataFrame validation passed: {len(df)} rows, {len(df.columns)} columns")
    return True


def main() -> int:
    """
    Main execution function.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    logger.info(f"🐍 APEXVIPER INITIALIZING... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    parser = argparse.ArgumentParser(
        description="APEXVIPER Logic Engine - Player Prop Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Use default apexviper_master_data.csv
  %(prog)s --input custom_data.csv  # Use custom input file
  %(prog)s --output results.csv     # Specify output file
        """,
    )
    parser.add_argument(
        "--input",
        default="apexviper_master_data.csv",
        help="Input CSV file with player data (default: apexviper_master_data.csv)",
    )
    parser.add_argument(
        "--output",
        default="apexviper_results.csv",
        help="Output CSV file for results (default: apexviper_results.csv)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose debug logging")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")

    # Load data
    try:
        input_path = Path(args.input)
        if not input_path.exists():
            logger.error(f"Input file not found: {input_path}")
            print(f"❌ ERROR: Data file '{input_path}' not found.")
            return 1

        logger.info(f"Loading data from {input_path}")
        df = pd.read_csv(input_path)
        logger.info(f"Loaded {len(df)} rows from {input_path}")

    except Exception as e:
        logger.error(f"Failed to load input file: {e}")
        print(f"❌ ERROR: Failed to load data file: {e}")
        return 1

    # Validate data
    try:
        validate_dataframe(df)
    except ValueError as e:
        logger.error(f"Data validation failed: {e}")
        print(f"❌ ERROR: Data validation failed: {e}")
        return 1

    # Apply Logic
    try:
        logger.info("Calculating APEX scores...")
        df["APEX_SCORE"] = df.apply(calculate_apex_score, axis=1)
        df["SIGNAL"] = df["APEX_SCORE"].apply(get_signal)
        logger.info("APEX score calculation complete")

    except Exception as e:
        logger.error(f"Failed to calculate APEX scores: {e}")
        print(f"❌ ERROR: Failed to calculate scores: {e}")
        return 1

    # Sort by Score (Best to Worst)
    df = df.sort_values(by="APEX_SCORE", ascending=False)

    # OUTPUT
    print("\n" + "=" * 80)
    print("🎯 TARGET PRIORITY LIST")
    print("=" * 80)
    print(df[["player", "team", "script_tag", "APEX_SCORE", "SIGNAL"]].to_string(index=False))
    print("=" * 80)

    # Save Enriched Data
    try:
        output_path = Path(args.output)
        df.to_csv(output_path, index=False)
        logger.info(f"Results saved to {output_path}")
        print(f"\n✅ ANALYSIS COMPLETE. Results saved to '{output_path}'")

        # Summary statistics
        green_count = len(df[df["SIGNAL"].str.contains("GREEN")])
        yellow_count = len(df[df["SIGNAL"].str.contains("YELLOW")])
        red_count = len(df[df["SIGNAL"].str.contains("RED")])

        print(f"\n📊 SUMMARY:")
        print(f"   🟢 GREEN (ELITE):    {green_count}")
        print(f"   🟡 YELLOW (PLAYABLE): {yellow_count}")
        print(f"   🔴 RED (AVOID):      {red_count}")

        return 0

    except Exception as e:
        logger.error(f"Failed to save results: {e}")
        print(f"❌ ERROR: Failed to save results: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
