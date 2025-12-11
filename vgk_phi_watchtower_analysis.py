#!/usr/bin/env python3
"""
WATCHTOWER ANALYSIS: VGK @ PHI
Date: December 11, 2025
Operator: APEXVIPER
"""

import sys

sys.path.append("nhl/tools/watchtower_engine")
from watchtower_engine import GameIntel, run_watchtower_protocol  # noqa: E402

# VGK @ PHI Game Setup
vgk_phi_game = GameIntel(
    home_team="PHI",
    away_team="VGK",
    vegas_total=5.5,
    star_player="Trevor Zegras",
    star_status="Active",
    opponent_defense_rating="Average",  # VGK has high shot blocking but Zegras is heating up
    goalie_status="Starter",  # Both Schmid and Vladar are starters
)

print("\n" + "=" * 80)
print("🕵️ WATCHTOWER ENGINE: GAME SCRIPT ANALYSIS")
print("=" * 80)
print("Game: VGK @ PHI")
print(f"Total: {vgk_phi_game.total}")
print("Away Goalie: Akira Schmid (SV% .908 L5)")
print("Home Goalie: Dan Vladar (SV% .898 L5)")
print("VGK Form: 4-0-1 L5 (Coming off SO loss)")
print("PHI Form: 3-2-0 L5 (Youth movement heating up)")
print("=" * 80)

# Run Watchtower Protocol
run_watchtower_protocol(vgk_phi_game)

# Custom Analysis for this specific game
print("\n" + "=" * 80)
print("🎯 CUSTOM GAME INTELLIGENCE")
print("=" * 80)
print("\n📊 GAME TYPE: MODIFIED GRIND / LOW-VOLUME SHOOTOUT")
print("\nKey Factors:")
print("  • Total = 5.5 (Below league average)")
print("  • VGK = HIGH shot blocking team (McNabb leads league)")
print("  • PHI = MODERATE shot blocking")
print("  • Both goalies = Starters with decent form")
print("  • Vegas on East Coast swing (travel fatigue)")
print("\n🎭 NARRATIVE INTELLIGENCE:")
print("  ✓ VGK in CHASE MODE (Blew SO loss to NYI)")
print("  ✓ PHI YOUTH MOVEMENT (Zegras/Michkov clicking)")
print("  ✓ Historical: PHI plays tight vs VGK at home")
print("  ⚠️  Goalie edge: Schmid > Vladar (slight)")
print("\n⚔️ SHOT VOLUME PROJECTION:")
print("  VGK Expected Shots: 28-31")
print("  PHI Expected Shots: 25-28")
print("  Total Shots Projection: 53-59")
print("\n🚨 GAME SCRIPT RISK:")
print("  • GRIND RISK: Medium-High (5.5 total, high blocks)")
print("  • BLOWOUT RISK: Low (Both teams structured)")
print("  • PACE SUPPRESSION: VGK blocks will limit PHI volume")
print("\n✅ RECOMMENDED ARCHITECTURE:")
print("  PRIMARY: 'The Floor' - Focus on high-volume Tier 1s")
print("  SECONDARY: 'The Ladder' - Zegras volume play")
print("  AVOID: Random 4-leg parlays (Volume uncertainty)")
print("=" * 80)
