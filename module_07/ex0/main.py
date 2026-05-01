from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main():
    try:
        print("=== DataDeck Card Foundation ===")
        print("Testing Abstract Base Class Design:\n")

        fire_dr = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        gb_wa = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 3, 2)

        print("CreatureCard Info:")
        print(fire_dr.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"Playable: {fire_dr.is_playable(6)}")
        print(f"Play result: {fire_dr.play({})}")

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {fire_dr.attack_target(gb_wa)}")

        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {fire_dr.is_playable(3)}")

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
