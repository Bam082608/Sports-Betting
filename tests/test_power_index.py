"""
Test suite for apexviper_power_index.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "apexviper-power-index"))

from apexviper_power_index import SIGNAL_THRESHOLDS, compute_power_index, grade_signal, safe_div


class TestSafeDiv:
    """Tests for safe_div function"""

    def test_normal_division(self):
        """Test normal division works"""
        assert safe_div(10, 2) == 5.0
        assert safe_div(15, 3) == 5.0
        assert safe_div(7, 2) == 3.5

    def test_division_by_zero(self):
        """Test division by zero returns 0"""
        assert safe_div(10, 0) == 0.0
        assert safe_div(100, 0) == 0.0

    def test_division_by_none(self):
        """Test division by None returns 0"""
        assert safe_div(10, None) == 0.0

    def test_division_by_nan(self):
        """Test division by NaN returns 0"""
        assert safe_div(10, np.nan) == 0.0

    def test_zero_numerator(self):
        """Test zero numerator works normally"""
        assert safe_div(0, 5) == 0.0

    def test_float_division(self):
        """Test float division"""
        assert safe_div(10.5, 2.0) == 5.25


class TestGradeSignal:
    """Tests for grade_signal function"""

    def test_green_signal(self):
        """Test values >= high threshold get GREEN"""
        assert grade_signal(0.50, low=0.15, mid=0.25, high=0.40) == "GREEN"
        assert grade_signal(0.40, low=0.15, mid=0.25, high=0.40) == "GREEN"
        assert grade_signal(1.00, low=0.15, mid=0.25, high=0.40) == "GREEN"

    def test_yellow_signal(self):
        """Test values >= mid and < high get YELLOW"""
        assert grade_signal(0.25, low=0.15, mid=0.25, high=0.40) == "YELLOW"
        assert grade_signal(0.30, low=0.15, mid=0.25, high=0.40) == "YELLOW"
        assert grade_signal(0.39, low=0.15, mid=0.25, high=0.40) == "YELLOW"

    def test_red_signal(self):
        """Test values < mid get RED"""
        assert grade_signal(0.10, low=0.15, mid=0.25, high=0.40) == "RED"
        assert grade_signal(0.24, low=0.15, mid=0.25, high=0.40) == "RED"
        assert grade_signal(0.00, low=0.15, mid=0.25, high=0.40) == "RED"

    def test_default_thresholds(self):
        """Test default threshold values work"""
        assert grade_signal(0.50) == "GREEN"
        assert grade_signal(0.30) == "YELLOW"
        assert grade_signal(0.10) == "RED"


class TestComputePowerIndex:
    """Tests for compute_power_index function"""

    def test_basic_computation_no_pp_data(self):
        """Test basic computation without PP data"""
        df_matrix = pd.DataFrame({"team": ["TOR", "MTL", "VAN"]})

        result = compute_power_index(df_matrix)

        # Check columns were added
        assert "API_score" in result.columns
        assert "API_signal" in result.columns
        assert "pp_conversion" in result.columns

        # All scores should be 0 since no PP data
        assert (result["API_score"] == 0.0).all()
        assert (result["API_signal"] == "RED").all()

    def test_with_team_pp_data(self):
        """Test computation with team PP data"""
        df_matrix = pd.DataFrame({"team": ["TOR", "MTL"]})
        df_pp_team = pd.DataFrame({"team": ["TOR", "MTL"], "pp_attempts": [100, 80], "pp_goals": [25, 20]})

        result = compute_power_index(df_matrix, df_pp_team)

        # Check PP conversion was calculated
        assert result.loc[result["team"] == "TOR", "pp_conversion"].values[0] == pytest.approx(0.25)
        assert result.loc[result["team"] == "MTL", "pp_conversion"].values[0] == pytest.approx(0.25)

    def test_with_player_pp_data(self):
        """Test computation with player PPSS data"""
        df_matrix = pd.DataFrame({"team": ["TOR", "MTL"]})
        df_pp_player = pd.DataFrame(
            {
                "team": ["TOR", "TOR", "MTL"],
                "player": ["Player A", "Player B", "Player C"],
                "pp_shots": [10, 15, 12],
                "pp_expected": [5, 7, 6],
            }
        )

        result = compute_power_index(df_matrix, df_pp_player=df_pp_player)

        # Check aggregation worked
        assert result.loc[result["team"] == "TOR", "team_pp_shots"].values[0] == 25  # 10 + 15
        assert result.loc[result["team"] == "TOR", "team_pp_expected"].values[0] == 12  # 5 + 7
        assert result.loc[result["team"] == "MTL", "team_pp_shots"].values[0] == 12
        assert result.loc[result["team"] == "MTL", "team_pp_expected"].values[0] == 6

    def test_complete_calculation(self):
        """Test complete API score calculation with all data"""
        df_matrix = pd.DataFrame({"team": ["TOR"]})
        df_pp_team = pd.DataFrame({"team": ["TOR"], "pp_attempts": [100], "pp_goals": [20]})
        df_pp_player = pd.DataFrame(
            {"team": ["TOR", "TOR"], "player": ["Player A", "Player B"], "pp_shots": [10, 10], "pp_expected": [5, 5]}
        )

        result = compute_power_index(df_matrix, df_pp_team, df_pp_player)

        # Manual calculation:
        # pp_conversion = 20/100 = 0.20
        # team_pp_expected = 10 (5+5)
        # team_pp_shots = 20 (10+10)
        # API_score = (10 * 0.5) + (20 * 0.3) + (0.20 * 0.2)
        #           = 5.0 + 6.0 + 0.04 = 11.04

        expected_score = (10 * 0.5) + (20 * 0.3) + (0.20 * 0.2)
        actual_score = result["API_score"].values[0]

        assert actual_score == pytest.approx(expected_score, abs=0.01)

    def test_signal_assignment(self):
        """Test that signals are assigned correctly"""
        df_matrix = pd.DataFrame({"team": ["Team_High", "Team_Mid", "Team_Low"]})
        df_pp_player = pd.DataFrame(
            {
                "team": ["Team_High", "Team_Mid", "Team_Low"],
                "player": ["A", "B", "C"],
                "pp_shots": [100, 50, 10],  # Different shot volumes
                "pp_expected": [100, 50, 10],  # Different expectations
            }
        )

        result = compute_power_index(df_matrix, df_pp_player=df_pp_player)

        # Team_High should have highest score
        high_score = result.loc[result["team"] == "Team_High", "API_score"].values[0]
        mid_score = result.loc[result["team"] == "Team_Mid", "API_score"].values[0]
        low_score = result.loc[result["team"] == "Team_Low", "API_score"].values[0]

        assert high_score > mid_score > low_score

    def test_missing_team_column_raises_error(self):
        """Test that missing team column raises KeyError"""
        df_matrix = pd.DataFrame({"not_team": ["TOR", "MTL"]})

        with pytest.raises(KeyError, match="team"):
            compute_power_index(df_matrix)

    def test_partial_team_coverage(self):
        """Test handling when PP data doesn't cover all teams"""
        df_matrix = pd.DataFrame({"team": ["TOR", "MTL", "VAN"]})
        df_pp_team = pd.DataFrame({"team": ["TOR"], "pp_attempts": [100], "pp_goals": [20]})  # Only TOR has data

        result = compute_power_index(df_matrix, df_pp_team)

        # TOR should have data, others should have 0
        tor_conversion = result.loc[result["team"] == "TOR", "pp_conversion"].values[0]
        mtl_conversion = result.loc[result["team"] == "MTL", "pp_conversion"].values[0]

        assert tor_conversion == 0.20
        assert mtl_conversion == 0.0


class TestIntegration:
    """Integration tests"""

    def test_full_workflow(self):
        """Test complete workflow with realistic data"""
        # Setup realistic team data
        teams = ["TOR", "MTL", "VAN", "CGY", "EDM"]
        df_matrix = pd.DataFrame({"team": teams})

        # Setup team PP data
        df_pp_team = pd.DataFrame({"team": teams, "pp_attempts": [100, 90, 110, 95, 105], "pp_goals": [25, 18, 27, 19, 28]})

        # Setup player PP data
        df_pp_player = pd.DataFrame(
            {
                "team": ["TOR", "TOR", "MTL", "VAN", "VAN", "CGY", "EDM"],
                "player": ["A", "B", "C", "D", "E", "F", "G"],
                "pp_shots": [15, 12, 10, 18, 14, 11, 20],
                "pp_expected": [8, 6, 5, 9, 7, 5, 10],
            }
        )

        result = compute_power_index(df_matrix, df_pp_team, df_pp_player)

        # Verify all teams present
        assert len(result) == 5

        # Verify all required columns exist
        assert all(
            col in result.columns
            for col in [
                "team",
                "pp_attempts",
                "pp_goals",
                "pp_conversion",
                "team_pp_shots",
                "team_pp_expected",
                "API_score",
                "API_signal",
            ]
        )

        # Verify signals are valid
        assert result["API_signal"].isin(["RED", "YELLOW", "GREEN"]).all()

        # Verify scores are non-negative
        assert (result["API_score"] >= 0).all()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
