#!/usr/bin/env python3
"""
ANAHEIM DUCKS @ NY ISLANDERS - WATCHTOWER ANALYSIS
Date: December 11, 2025
Time: 7:00 PM EST
Venue: UBS Arena, New York

This script runs the Watchtower Decision Engine on the ANA @ NYI matchup
to generate game script classification and betting recommendations.
"""

import sys
from pathlib import Path

# Add parent directory to path to import watchtower_engine
sys.path.insert(0, str(Path(__file__).parent / "nhl" / "tools" / "watchtower_engine"))

from watchtower_engine import GameIntel, run_watchtower_protocol


def main():
    """
    Execute Watchtower analysis for Anaheim Ducks @ NY Islanders
    """
    print("\n" + "=" * 80)
    print("🏒 APEXVIPER WATCHTOWER ENGINE - ANA @ NYI ANALYSIS")
    print("=" * 80)
    print("Date: December 11, 2025 | Time: 7:00 PM EST | Venue: UBS Arena")
    print("=" * 80 + "\n")

    # Game Intelligence Data
    game = GameIntel(
        home_team="NYI",
        away_team="ANA",
        vegas_total=6.5,  # High total indicates scoring potential
        star_player="Bo Horvat",  # NYI's top scorer and volume shooter
        star_status="Active",
        opponent_defense_rating="Leak",  # ANA is 23rd in GA, 27th PK%
        goalie_status="Starter",  # Rittich is starter, Sorokin rested
    )

    # Run the Watchtower Protocol
    run_watchtower_protocol(game)

    # Additional Game Context
    print("\n" + "=" * 80)
    print("📊 ADDITIONAL GAME INTELLIGENCE")
    print("=" * 80)

    print("\n🎯 KEY MATCHUP FACTORS:")
    print("   • ANA Offense: 2nd in NHL in goals (107), fast youth movement")
    print("   • ANA Defense: 23rd in GA (98), 27th in PK% (75.5%) - LEAK CITY")
    print("   • NYI Offense: 14th in goals (90), structured but limited")
    print("   • NYI Defense: 13th in GA (86), 5th in PK% (84.3%) - ELITE")
    print("   • Goalie Edge: Neutral (Husso .893 SV% vs Rittich .901 SV%)")

    print("\n🚨 POWER PLAY OPPORTUNITIES:")
    print("   • ANA PP: 18.6% (20th) - Heating up (2 PPG vs CHI)")
    print("   • NYI PP: 15.0% (28th) - Ice cold")
    print("   • ANA PK: 75.5% (27th) - VULNERABLE ⚠️")
    print("   • NYI PK: 84.3% (5th) - Shutdown unit ✅")
    print("\n   >> NYI should capitalize on PP chances against ANA's weak PK")
    print("   >> ANA needs volume shooting on PP to beat NYI's elite PK")

    print("\n📈 MOMENTUM & TRENDS:")
    print("   • ANA: 4-1-0 in last 5 (Win streak after UTA blowout)")
    print("   • NYI: 4-1-0 in last 5 (Strong home stretch)")
    print("   • Head-to-Head: Split recent meetings, high-scoring games")
    print("   • ANA Road: Usually struggles on Long Island, BUT new faster team")
    print("   • NYI Home: Solid, but just gave up 4 goals to VGK")

    print("\n🎭 NARRATIVE INTELLIGENCE:")
    print("   • ANA: 'Youth Movement' - Playing loose, fast, dangerous")
    print("   • NYI: 'Stabilizer' - Needs to win these games for Metro playoff race")
    print("   • NYI cannot afford to trade chances with ANA's explosive offense")
    print("   • If ANA scores first, game opens up (CHAOS)")
    print("   • If NYI scores first, they shut it down (STRUCTURE)")

    print("\n" + "=" * 80)
    print("🎯 APEXVIPER PRIMARY TARGETS")
    print("=" * 80)

    targets = [
        ("Bo Horvat", "2.5+ Shots", "-135", "ANCHOR - vs ANA leak defense"),
        ("Noah Dobson", "2.5+ Shots", "-125", "PP1 QB vs 27th PK"),
        ("Leo Carlsson", "2.5+ Shots", "-125", "Youth movement, heating up"),
        ("Anders Lee", "2.5+ Shots", "-120", "Net-front vs Husso (.893 SV%)"),
        ("Troy Terry", "2.5+ Shots", "-115", "Safe veteran floor play"),
    ]

    print("\n🟢 GREEN SIGNAL (ELITE):")
    for i, (player, prop, odds, reason) in enumerate(targets[:3], 1):
        print(f"   {i}. {player:15s} | {prop:12s} | {odds:6s} | {reason}")

    print("\n🟡 YELLOW SIGNAL (PLAYABLE):")
    for i, (player, prop, odds, reason) in enumerate(targets[3:], 4):
        print(f"   {i}. {player:15s} | {prop:12s} | {odds:6s} | {reason}")

    print("\n" + "=" * 80)
    print("🪜 THE LADDER STRATEGY (PARLAY OPTIONS)")
    print("=" * 80)

    print("\n📋 OPTION A: 'Distributed Volume' (4-Leg, ~+450 odds)")
    print("   1. Bo Horvat 2.5+ Shots")
    print("   2. Leo Carlsson 2.5+ Shots")
    print("   3. Noah Dobson 2.5+ Shots")
    print("   4. Anders Lee 2.5+ Shots")
    print("   >> Risk: Moderate | Expected Hit Rate: 65-70%")

    print("\n📋 OPTION B: 'Star & Floor' (3-Leg, ~+250 odds)")
    print("   1. Bo Horvat 3.5+ Shots (ANCHOR)")
    print("   2. Olen Zellweger 1.5+ Shots (FLOOR)")
    print("   3. Troy Terry 2.5+ Shots (FLOOR)")
    print("   >> Risk: Lower | Expected Hit Rate: 70-75%")

    print("\n" + "=" * 80)
    print("⚠️ BANNED STRATEGIES")
    print("=" * 80)
    print("   ❌ Parlaying Cutter Gauthier 3.5+ shots (too volatile, 0-shot games)")
    print("   ❌ Trusting Husso to hold NYI under 2.5 goals (.893 SV%, shaky)")
    print("   ❌ ANA team total OVER + NYI team total OVER (contradictory)")

    print("\n" + "=" * 80)
    print("🔮 FINAL PREDICTION")
    print("=" * 80)
    print("   Score: NY Islanders 4, Anaheim Ducks 3")
    print("   Winner: NYI (Regulation or OT)")
    print("   Total: OVER 6.5 ✅ (Borderline)")
    print("   Best Bet: Bo Horvat 2.5+ Shots (-135) - 1.0 unit")
    print("=" * 80 + "\n")

    print("✅ WATCHTOWER ANALYSIS COMPLETE")
    print("📊 Classification: THE SHOOTOUT (Type 2)")
    print("🎯 Protocol: STAR & FLOOR (Distributed Scoring)")
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()
