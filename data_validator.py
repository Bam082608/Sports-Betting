#!/usr/bin/env python3
"""
APEXVIPER Data Validation Module

This module provides Pydantic models and validation functions for:
- Player prop data (master data CSV)
- Team power play data
- Player PPSS data

Usage:
    from data_validator import validate_player_data, PlayerDataRow

    # Validate a CSV file
    is_valid, errors = validate_player_data('apexviper_master_data.csv')
"""

import logging
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
from enum import Enum

import pandas as pd
from pydantic import BaseModel, Field, validator, ValidationError

# Setup logging
logger = logging.getLogger(__name__)


# --- ENUMERATIONS ---

class ResistanceGrade(str, Enum):
    """Valid resistance grade values"""
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class ScriptTag(str, Enum):
    """Valid script tag values"""
    CHASE_MODE = "CHASE_MODE"
    HISTORY_CHASE = "HISTORY_CHASE"
    BLOWOUT_RISK = "BLOWOUT_RISK"
    SUPPRESSED = "SUPPRESSED"
    NEUTRAL = "NEUTRAL"
    LOW_PACE = "LOW_PACE"


# --- PYDANTIC MODELS ---

class PlayerDataRow(BaseModel):
    """
    Validation model for player prop data (master data CSV).

    Attributes:
        player: Player name
        team: Team abbreviation (3 letters)
        opponent: Opponent team abbreviation
        odds_930am: Odds value (can be negative)
        last_5_shots: Pipe-delimited string of 5 shot counts
        avg_toi: Average time on ice in minutes
        resistance_grade: Defensive resistance rating
        script_tag: Game script classification
    """

    player: str = Field(..., min_length=1, max_length=100)
    team: str = Field(..., min_length=2, max_length=3)
    opponent: str = Field(..., min_length=2, max_length=3)
    odds_930am: float = Field(..., description="Betting odds at 9:30 AM")
    last_5_shots: str = Field(..., pattern=r'^\d+\|\d+\|\d+\|\d+\|\d+$')
    avg_toi: float = Field(..., ge=0, le=60, description="Average time on ice (0-60 minutes)")
    resistance_grade: ResistanceGrade
    script_tag: ScriptTag

    @validator('last_5_shots')
    def validate_shot_counts(cls, v):
        """Validate that shot counts are reasonable (0-15 per game)"""
        try:
            shots = [int(x) for x in v.split('|')]
            if any(s < 0 or s > 15 for s in shots):
                raise ValueError("Shot counts must be between 0 and 15")
            if len(shots) != 5:
                raise ValueError("Must have exactly 5 shot counts")
        except Exception as e:
            raise ValueError(f"Invalid shot string format: {e}")
        return v

    @validator('team', 'opponent')
    def validate_team_code(cls, v):
        """Ensure team codes are uppercase"""
        return v.upper()

    class Config:
        # Allow case-insensitive enum matching
        use_enum_values = True


class TeamPowerPlayRow(BaseModel):
    """
    Validation model for team power play data.

    Attributes:
        team: Team abbreviation
        pp_attempts: Number of power play attempts
        pp_goals: Number of power play goals scored
    """

    team: str = Field(..., min_length=2, max_length=3)
    pp_attempts: int = Field(..., ge=0, description="Must be non-negative")
    pp_goals: int = Field(..., ge=0, description="Must be non-negative")

    @validator('pp_goals')
    def goals_not_exceed_attempts(cls, v, values):
        """Validate that goals don't exceed attempts"""
        if 'pp_attempts' in values and v > values['pp_attempts']:
            raise ValueError("PP goals cannot exceed PP attempts")
        return v

    @validator('team')
    def validate_team_code(cls, v):
        """Ensure team code is uppercase"""
        return v.upper()


class PlayerPPSSRow(BaseModel):
    """
    Validation model for player power play shot share data.

    Attributes:
        player: Player name
        team: Team abbreviation
        pp_shots: Power play shots taken
        pp_expected: Expected power play performance metric
    """

    player: str = Field(..., min_length=1, max_length=100)
    team: str = Field(..., min_length=2, max_length=3)
    pp_shots: float = Field(..., ge=0, description="Must be non-negative")
    pp_expected: float = Field(..., ge=0, description="Must be non-negative")

    @validator('team')
    def validate_team_code(cls, v):
        """Ensure team code is uppercase"""
        return v.upper()


# --- VALIDATION FUNCTIONS ---

def validate_dataframe(
    df: pd.DataFrame,
    model: type[BaseModel],
    filename: str = "data"
) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Validate a DataFrame against a Pydantic model.

    Args:
        df: DataFrame to validate
        model: Pydantic model class to validate against
        filename: Name of file for error reporting

    Returns:
        Tuple of (is_valid, list_of_errors)
        where list_of_errors contains dicts with 'row', 'field', 'error'
    """
    errors = []
    is_valid = True

    logger.info(f"Validating {len(df)} rows from {filename}")

    for idx, row in df.iterrows():
        try:
            # Convert row to dict and validate
            row_dict = row.to_dict()
            model(**row_dict)

        except ValidationError as e:
            is_valid = False
            for error in e.errors():
                errors.append({
                    'row': idx + 2,  # +2 because 0-indexed and header row
                    'field': '.'.join(str(x) for x in error['loc']),
                    'error': error['msg'],
                    'value': error.get('input', 'N/A')
                })
                logger.error(
                    f"{filename} row {idx + 2}: {error['loc']} - {error['msg']}"
                )

        except Exception as e:
            is_valid = False
            errors.append({
                'row': idx + 2,
                'field': 'unknown',
                'error': str(e),
                'value': 'N/A'
            })
            logger.error(f"{filename} row {idx + 2}: Unexpected error - {e}")

    if is_valid:
        logger.info(f"✅ {filename}: All {len(df)} rows passed validation")
    else:
        logger.warning(f"❌ {filename}: {len(errors)} validation errors found")

    return is_valid, errors


def validate_player_data(file_path: str) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Validate player prop data CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    try:
        df = pd.read_csv(file_path)
        return validate_dataframe(df, PlayerDataRow, file_path)

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return False, [{'error': f'File not found: {file_path}'}]

    except Exception as e:
        logger.error(f"Failed to load {file_path}: {e}")
        return False, [{'error': f'Failed to load file: {e}'}]


def validate_team_pp_data(file_path: str) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Validate team power play data CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    try:
        df = pd.read_csv(file_path)
        return validate_dataframe(df, TeamPowerPlayRow, file_path)

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return False, [{'error': f'File not found: {file_path}'}]

    except Exception as e:
        logger.error(f"Failed to load {file_path}: {e}")
        return False, [{'error': f'Failed to load file: {e}'}]


def validate_player_ppss_data(file_path: str) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Validate player PPSS data CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    try:
        df = pd.read_csv(file_path)
        return validate_dataframe(df, PlayerPPSSRow, file_path)

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return False, [{'error': f'File not found: {file_path}'}]

    except Exception as e:
        logger.error(f"Failed to load {file_path}: {e}")
        return False, [{'error': f'Failed to load file: {e}'}]


def print_validation_report(errors: List[Dict[str, Any]], filename: str = "data"):
    """
    Print a formatted validation error report.

    Args:
        errors: List of error dictionaries from validation
        filename: Name of file for reporting
    """
    if not errors:
        print(f"✅ {filename}: All rows passed validation")
        return

    print(f"\n{'='*80}")
    print(f"❌ VALIDATION ERRORS: {filename}")
    print(f"{'='*80}\n")

    for error in errors:
        if 'row' in error:
            print(f"Row {error['row']}: {error.get('field', 'unknown')}")
            print(f"  Error: {error['error']}")
            if error.get('value') != 'N/A':
                print(f"  Value: {error['value']}")
            print()
        else:
            print(f"General Error: {error['error']}\n")

    print(f"{'='*80}")
    print(f"Total errors: {len(errors)}")
    print(f"{'='*80}\n")


# --- CLI INTERFACE ---

def main():
    """CLI interface for data validation"""
    import argparse

    parser = argparse.ArgumentParser(
        description="APEXVIPER Data Validator - Validate CSV data files"
    )
    parser.add_argument(
        "file",
        help="CSV file to validate"
    )
    parser.add_argument(
        "--type",
        choices=["player", "team_pp", "player_ppss"],
        default="player",
        help="Type of data file (default: player)"
    )

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Validate based on type
    if args.type == "player":
        is_valid, errors = validate_player_data(args.file)
    elif args.type == "team_pp":
        is_valid, errors = validate_team_pp_data(args.file)
    elif args.type == "player_ppss":
        is_valid, errors = validate_player_ppss_data(args.file)

    # Print report
    print_validation_report(errors, args.file)

    # Exit with appropriate code
    exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
