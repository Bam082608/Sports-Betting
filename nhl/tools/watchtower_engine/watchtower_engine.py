# 🕵️‍♂️ THE WATCHTOWER: SHOT MATRIX DECISION ENGINE (v1.0)
# OPERATOR: Apex
# PURPOSE: Automate Ticket Architecture based on Game Script


class GameIntel:
    def __init__(
        self,
        home_team,
        away_team,
        vegas_total,
        star_player,
        star_status,
        opponent_defense_rating,
        goalie_status="Starter",
    ):
        self.matchup = f"{away_team} @ {home_team}"
        self.total = vegas_total
        self.star = star_player
        self.star_status = star_status  # "Active", "Injured", "Unknown"
        self.defense_rating = opponent_defense_rating  # "Leak", "Average", "Wall"
        self.goalie = goalie_status  # "Starter", "Backup", "Elite"


def run_watchtower_protocol(game):
    print(f"\n{'='*60}")
    print(f"📡 ANALYZING TARGET: {game.matchup}")
    print(f"{'='*60}")

    # --- STEP 1: CLASSIFY THE GAME SCRIPT ---
    game_type = "UNKNOWN"

    # LOGIC BRANCH 1: THE GRIND
    if game.total <= 6.0 and game.defense_rating == "Wall":
        game_type = "THE GRIND (Type 1)"
        print(f"⚠️ CLASSIFICATION: {game_type}")
        print(">> Signal: Low Total + Elite Defense.")
        print(f">> PROTOCOL: DEPLOY 'THE SHIELD'")
        print("   1. Under 1.5 Goals (1st Period)")
        print("   2. No Goal First 10 Mins")
        print("   3. Under 6.5 Total Goals")
        print("   ❌ BANNED: Player Prop Parlays (Volume too low)")

    # LOGIC BRANCH 2: THE CHAOS / BACKUP EXPLOIT
    elif game.goalie == "Backup" and game.total >= 6.5:
        game_type = "THE SIEGE / CHAOS (Type 4)"
        print(f"🚨 CLASSIFICATION: {game_type}")
        print(">> Signal: High Total + Backup Goalie.")
        print(f">> PROTOCOL: DEPLOY 'THE SIEGE'")
        print("   1. Team Total OVER (Pivot from shots if blow-out risk)")
        print("   2. Rebound Hunter Props (e.g., Hyman 3+)")
        print("   3. Point Shots (Defensemen 2+)")

    # LOGIC BRANCH 3: THE ONE-MAN ARMY (LADDER)
    elif (
        game.star_status == "Active"
        and game.defense_rating == "Leak"
        and game.total >= 6.5
    ):
        # Check if it's One Man Army or Distributed
        if game.star in ["MacKinnon", "Kaprizov", "Pastrnak", "Kucherov"]:
            game_type = "ONE-MAN ARMY (Type 3)"
            print(f"🪜 CLASSIFICATION: {game_type}")
            print(">> Signal: Elite Star vs. Bad Defense.")
            print(f">> PROTOCOL: DEPLOY 'THE LADDER'")
            print(f"   1. {game.star} 3+ Shots (Unit: 1.0)")
            print(f"   2. {game.star} 4+ Shots (Unit: 0.5)")
            print(f"   3. {game.star} 5+ Shots (Unit: 0.25)")
            print("   ❌ BANNED: Parlaying Star with 3 other random guys.")
        else:
            # If it's a good offense but not a "Hog", it's a Shootout
            game_type = "THE SHOOTOUT (Type 2)"

    # LOGIC BRANCH 4: THE SHOOTOUT (DISTRIBUTED)
    if game_type == "THE SHOOTOUT (Type 2)" or (
        game.total >= 6.5 and game_type == "UNKNOWN"
    ):
        print(f"🔫 CLASSIFICATION: THE SHOOTOUT (Type 2)")
        print(">> Signal: High Volume, but Star is a Passer or Out.")
        print(f">> PROTOCOL: DEPLOY 'STAR & FLOOR'")
        print(f"   1. ANCHOR: {game.star} 4+ Shots (The King)")
        print("   2. PAWN A: Top-6 Winger 1+ Shot")
        print("   3. PAWN B: Top-4 Defenseman 1+ Shot")
        print("   4. OPPONENT: Best Player 2+ Shots")

    print("-" * 60)


# ==============================================================================
# 🎮 INPUT DATA: TONIGHT'S 10:00 PM SLATE
# ==============================================================================

# Game 1: Minnesota vs Vancouver
# Narrative: Kaprizov is the One Man Army. Vancouver has a leaky backup (Tolopilo).
game1 = GameIntel(
    home_team="VAN",
    away_team="MIN",
    vegas_total=6.0,  # Slightly lower total, but Narrative overrides
    star_player="Kaprizov",
    star_status="Active",
    opponent_defense_rating="Leak",  # Tolopilo is in net
    goalie_status="Backup",
)

# Game 2: Winnipeg vs Edmonton
# Narrative: The Siege. Backup goalie for WPG (Comrie). High Volume EDM.
game2 = GameIntel(
    home_team="EDM",
    away_team="WPG",
    vegas_total=6.5,
    star_player="McDavid",
    star_status="Active",
    opponent_defense_rating="Average",
    goalie_status="Backup",  # Comrie confirms Narrative change
)

# Game 3: Detroit vs Seattle
# Narrative: The Stay Away / Floor.
game3 = GameIntel(
    home_team="SEA",
    away_team="DET",
    vegas_total=6.0,
    star_player="McCann",
    star_status="Active",
    opponent_defense_rating="Leak",
    goalie_status="Starter",
)

# 🚀 EXECUTE ENGINE
if __name__ == "__main__":
    run_watchtower_protocol(game1)
    run_watchtower_protocol(game2)
    run_watchtower_protocol(game3)
