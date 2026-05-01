from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard, ArtifactEffect
from ex1.Deck import Deck
from ex0.Card import Rarity


def main() -> None:
    try:
        print("=== DataDeck Deck Builder ===")
        print()
        print("Building deck with different card types...")
        deck = Deck()

        dr = CreatureCard("fire dragon", 5, Rarity.LEGENDARY, 7, 5)
        lg = SpellCard("Lightning Bolt", 3, Rarity.RARE, EffectType.DAMAGE)
        ar = ArtifactCard(
            "Mana Crystal", 2, Rarity.COMMON, 3, ArtifactEffect.BOOST
        )

        deck.add_card(lg)
        deck.add_card(ar)
        deck.add_card(dr)
        print("Deck stats:", deck.get_deck_stats())
        print()
        print("Drawing and playing cards:")
        print()
        while True:
            card = deck.draw_card()
            if not card:
                break
            info: dict = card.get_card_info()
            print(f"Drew: {card.name} ({info['type']})")
            print(f"Play result: {card.play({})}")
            print()

        print(
            "Polymorphism in action: Same interface, different card behaviors!"
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
