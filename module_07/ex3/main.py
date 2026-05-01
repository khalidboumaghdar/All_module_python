from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    try:
        print()
        print("=== DataDeck Game Engine ===")
        print()
        print("Configuring Fantasy Card Game...")
        factory = FantasyCardFactory()
        print("Factory:",  factory.__class__.__name__)
        strategy = AggressiveStrategy()
        print("Strategy:", strategy.__class__.__name__)
        print("Available types:", factory.get_supported_types())
        print()
        print("Simulating aggressive turn...")
        en = GameEngine()
        en.configure_engine(factory, strategy)
        hand = [f"{card.name} ({card.cost})" for card in en.hand]
        print(f"Hand: {hand}")
        print()
        print("Turn execution:")
        result = en.simulate_turn()
        print(f"Strategy: {result['strategy']}")
        print(f"Actions:  {result['actions']}")
        print()
        print("Game Report:")
        print(en.get_engine_status())
        print()
        print(
            "Abstract Factory+Strategy Pattern: Maximum flexibility achieved!"
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
