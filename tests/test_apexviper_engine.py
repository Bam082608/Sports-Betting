"""
Test suite for apexviper_engine.py
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path to import module
sys.path.insert(0, str(Path(__file__).parent.parent))

from apexviper_engine import (
    parse_last_five,
    calculate_apex_score,
    get_signal,
    validate_dataframe,
    CHASE_BONUS,
    BLOWOUT_PENALTY,
    RESISTANCE_PENALTY
)


class TestParseLastFive:
    """Tests for parse_last_five function"""

    def test_valid_shot_string(self):
        """Test parsing valid shot string"""
        avg, hits = parse_last_five("3|4|4|5|4")
        assert avg == 4.0
        assert hits == 5  # 5 games with >= 2.5 shots (all values: 3, 4, 4, 5, 4)

    def test_all_high_shots(self):
        """Test string with all shots above target"""
        avg, hits = parse_last_five("5|5|5|5|5")
        assert avg == 5.0
        assert hits == 5

    def test_all_low_shots(self):
        """Test string with all shots below target"""
        avg, hits = parse_last_five("1|1|2|1|2")
        assert avg == 1.4
        assert hits == 0

    def test_mixed_shots(self):
        """Test mixed high and low shots"""
        avg, hits = parse_last_five("2|2|7|3|5")
        assert avg == 3.8
        assert hits == 3  # 7, 3, and 5 are >= 2.5

    def test_empty_string(self):
        """Test empty string returns zeros"""
        avg, hits = parse_last_five("")
        assert avg == 0.0
        assert hits == 0

    def test_invalid_string(self):
        """Test invalid format returns zeros"""
        avg, hits = parse_last_five("abc|def|ghi")
        assert avg == 0.0
        assert hits == 0

    def test_wrong_count(self):
        """Test string with wrong number of values still processes"""
        avg, hits = parse_last_five("3|4|5")  # Only 3 values instead of 5
        # Should still process but log warning
        assert avg > 0

    def test_with_spaces(self):
        """Test string with spaces gets stripped"""
        avg, hits = parse_last_five(" 3 | 4 | 4 | 5 | 4 ")
        assert avg == 4.0
        assert hits == 5


class TestCalculateApexScore:
    """Tests for calculate_apex_score function"""

    def test_basic_score_calculation(self):
        """Test basic APEX score calculation"""
        row = pd.Series({
            'player': 'Test Player',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'MODERATE'
        })
        score = calculate_apex_score(row)
        assert isinstance(score, float)
        assert 0.0 <= score <= 2.0  # Reasonable range with bonuses

    def test_chase_mode_bonus(self):
        """Test that CHASE_MODE applies bonus"""
        row_neutral = pd.Series({
            'player': 'Player A',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'MODERATE'
        })
        row_chase = pd.Series({
            'player': 'Player B',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'CHASE_MODE',
            'resistance_grade': 'MODERATE'
        })

        score_neutral = calculate_apex_score(row_neutral)
        score_chase = calculate_apex_score(row_chase)

        # Chase mode should have higher score by CHASE_BONUS amount
        assert score_chase == pytest.approx(score_neutral + CHASE_BONUS, abs=0.001)

    def test_blowout_penalty(self):
        """Test that BLOWOUT_RISK applies penalty"""
        row_neutral = pd.Series({
            'player': 'Player A',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'MODERATE'
        })
        row_blowout = pd.Series({
            'player': 'Player B',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'BLOWOUT_RISK',
            'resistance_grade': 'MODERATE'
        })

        score_neutral = calculate_apex_score(row_neutral)
        score_blowout = calculate_apex_score(row_blowout)

        # Blowout risk should have lower score
        assert score_blowout == pytest.approx(score_neutral + BLOWOUT_PENALTY, abs=0.001)

    def test_resistance_penalty(self):
        """Test that HIGH resistance applies penalty"""
        row_moderate = pd.Series({
            'player': 'Player A',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'MODERATE'
        })
        row_high = pd.Series({
            'player': 'Player B',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'HIGH'
        })

        score_moderate = calculate_apex_score(row_moderate)
        score_high = calculate_apex_score(row_high)

        # High resistance should have lower score
        assert score_high == pytest.approx(score_moderate + RESISTANCE_PENALTY, abs=0.001)

    def test_low_resistance_bonus(self):
        """Test that LOW resistance applies bonus"""
        row_moderate = pd.Series({
            'player': 'Player A',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'MODERATE'
        })
        row_low = pd.Series({
            'player': 'Player B',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'NEUTRAL',
            'resistance_grade': 'LOW'
        })

        score_moderate = calculate_apex_score(row_moderate)
        score_low = calculate_apex_score(row_low)

        # Low resistance should have higher score
        assert score_low > score_moderate

    def test_invalid_script_tag(self):
        """Test that invalid script tag defaults to NEUTRAL"""
        row = pd.Series({
            'player': 'Test Player',
            'last_5_shots': '3|4|4|5|4',
            'script_tag': 'INVALID_TAG',
            'resistance_grade': 'MODERATE'
        })
        # Should not raise error, should log warning and use NEUTRAL
        score = calculate_apex_score(row)
        assert isinstance(score, float)


class TestGetSignal:
    """Tests for get_signal function"""

    def test_green_signal(self):
        """Test scores >= 0.75 get GREEN"""
        assert get_signal(0.75) == "🟢 GREEN (ELITE)"
        assert get_signal(0.80) == "🟢 GREEN (ELITE)"
        assert get_signal(1.00) == "🟢 GREEN (ELITE)"

    def test_yellow_signal(self):
        """Test scores >= 0.60 and < 0.75 get YELLOW"""
        assert get_signal(0.60) == "🟡 YELLOW (PLAYABLE)"
        assert get_signal(0.65) == "🟡 YELLOW (PLAYABLE)"
        assert get_signal(0.74) == "🟡 YELLOW (PLAYABLE)"

    def test_red_signal(self):
        """Test scores < 0.60 get RED"""
        assert get_signal(0.59) == "🔴 RED (AVOID)"
        assert get_signal(0.30) == "🔴 RED (AVOID)"
        assert get_signal(0.00) == "🔴 RED (AVOID)"


class TestValidateDataframe:
    """Tests for validate_dataframe function"""

    def test_valid_dataframe(self):
        """Test valid DataFrame passes validation"""
        df = pd.DataFrame({
            'player': ['Player A', 'Player B'],
            'team': ['TOR', 'MTL'],
            'last_5_shots': ['3|4|5|4|3', '2|2|3|4|5'],
            'script_tag': ['NEUTRAL', 'CHASE_MODE'],
            'resistance_grade': ['MODERATE', 'LOW']
        })
        assert validate_dataframe(df) == True

    def test_missing_columns(self):
        """Test missing required columns raises error"""
        df = pd.DataFrame({
            'player': ['Player A'],
            'team': ['TOR']
            # Missing last_5_shots, script_tag, resistance_grade
        })
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_dataframe(df)

    def test_empty_dataframe(self):
        """Test empty DataFrame raises error"""
        df = pd.DataFrame()
        with pytest.raises(ValueError, match="empty"):
            validate_dataframe(df)

    def test_null_values_warning(self):
        """Test null values log warning but don't fail"""
        df = pd.DataFrame({
            'player': ['Player A', None],
            'team': ['TOR', 'MTL'],
            'last_5_shots': ['3|4|5|4|3', '2|2|3|4|5'],
            'script_tag': ['NEUTRAL', None],
            'resistance_grade': ['MODERATE', 'LOW']
        })
        # Should not raise error, but should log warning
        assert validate_dataframe(df) == True


class TestIntegration:
    """Integration tests for full workflow"""

    def test_full_dataframe_processing(self):
        """Test processing a complete DataFrame"""
        df = pd.DataFrame({
            'player': ['Player A', 'Player B', 'Player C'],
            'team': ['TOR', 'MTL', 'VAN'],
            'last_5_shots': ['5|5|5|5|5', '3|3|3|3|3', '1|1|1|1|1'],
            'script_tag': ['CHASE_MODE', 'NEUTRAL', 'BLOWOUT_RISK'],
            'resistance_grade': ['LOW', 'MODERATE', 'HIGH']
        })

        # Calculate scores
        df['APEX_SCORE'] = df.apply(calculate_apex_score, axis=1)
        df['SIGNAL'] = df['APEX_SCORE'].apply(get_signal)

        # Verify all scores calculated
        assert len(df) == 3
        assert 'APEX_SCORE' in df.columns
        assert 'SIGNAL' in df.columns
        assert df['APEX_SCORE'].notna().all()

        # Player A should have highest score (high shots + chase mode + low resistance)
        assert df.iloc[0]['APEX_SCORE'] > df.iloc[1]['APEX_SCORE']
        assert df.iloc[1]['APEX_SCORE'] > df.iloc[2]['APEX_SCORE']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
