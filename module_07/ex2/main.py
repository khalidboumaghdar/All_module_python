from ex2.EliteCard import EliteCard
from ex2.Combatable import CombatType
from ex2.Magical import MagicType
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("=== DataDeck Ability System ===")
        print()
        print("EliteCard capabilities:")
        card_methods = [m for m in dir(Card) if not m.startswith('_')]
        combat_methods = [m for m in dir(Combatable) if not m.startswith('_')]
        magic_methods = [m for m in dir(Magical) if not m.startswith('_')]
        print(f"- Card:       {card_methods}")
        print(f"- Combatable: {combat_methods}")
        print(f"- Magical:    {magic_methods}")

        card = EliteCard(
            "Arcane Warrior", 6, Rarity.LEGENDARY, 5, 3, 4,
            combat_type=CombatType.MELEE, magic_type=MagicType.ARCANE
            )
        enemy = CreatureCard("Enemy",  3, Rarity.COMMON, 3, 3)
        enemy1 = CreatureCard("Enemy1", 2, Rarity.COMMON, 2, 2)
        enemy2 = CreatureCard("Enemy2", 2, Rarity.COMMON, 2, 2)

        print(f"\nPlaying {card.name} (Elite Card):")
        print()
        print("Combat phase:")
        print(f"Attack result:  {card.attack(enemy)}")
        print(f"Defense result: {card.defend(5)}")
        print()
        print("Magic phase:")
        print(f"Spell cast:   {card.cast_spell('Fireball', [enemy1, enemy2])}")
        print(f"Mana channel: {card.channel_mana(3)}")
        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
