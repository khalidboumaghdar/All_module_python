from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def main() -> None:
    try:
        print("=== DataDeck Tournament Platform ===")
        print()
        print("Registering Tournament Cards...")
        pl = TournamentPlatform()
        dr = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        wz = TournamentCard("Ice Wizard", 4, Rarity.RARE, 5, 6)

        dr_id = pl.register_card(dr)
        wz_id = pl.register_card(wz)
        print()
        print(f"{dr.name} (ID: {dr_id}):")
        print(f"- Interfaces: {dr.get_tournament_stats()['interfaces']}")
        print(f"- Rating : {dr.rating}")
        print(f"- Record:{dr.wins}-{dr.losses}")
        print()
        print(f"{wz.name} (ID : {wz_id}):")
        print(f"- Interfaces: {wz.get_tournament_stats()['interfaces']}")
        print(f"- Rating: {wz.rating}")
        print(f"- Record:{wz.wins}-{wz.losses}")
        print()
        print("Creating tournament match...")
        match_rs = pl.create_match(dr_id, wz_id)
        print("Match result:", match_rs)
        print()
        l_bord = pl.get_leaderboard()
        for i, entry in enumerate(l_bord, 1):
            print(
                f"""{i}.{entry['name']}-Rating:{entry['rating']}({entry['record']})
                """
            )
        print("\nPlatform Report:")
        print(pl.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"Eroor {e}")


if __name__ == "__main__":
    main()
