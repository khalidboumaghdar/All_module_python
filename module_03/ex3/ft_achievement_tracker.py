data = {
    "alice": {
        "first_blood",
        "pixel_perfect",
        "speed_runner",
    },
    "bob": {
        "level_master",
        "boss_hunter",
        "treasure_seeker",
    },
    "charlie": {
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
    },
    "diana": {
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
    },
    "eve": {
        "level_master",
        "treasure_seeker",
        "first_blood",
    },
    "frank": {
        "explorer",
        "boss_hunter",
        "first_blood",
    },
}

alice = data["alice"]
bob = data["bob"]
charlie = data["charlie"]


def main():
    """Display player achievements and perform basic achievement analytics."""
    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n")

    print("=== Achievement Analytics ===")
    un = alice.union(bob, charlie)
    print(f"All unique achievements: {un}")
    print(f"Total unique achievements: {len(un)}")
    print("\n")

    inst = alice.intersection(bob, charlie)
    print(f"Common to all players: {inst}")

    df_al = alice.difference(bob.union(charlie))
    df_bob = bob.difference(alice.union(charlie))
    df_charlie = charlie.difference(alice.union(bob))

    un_ar = df_al.union(df_bob, df_charlie)
    print(f"Rare achievements (1 player): {un_ar}")
    print("\n")

    common = bob.intersection(alice)
    print(f"Alice vs Bob common: {common}")

    al_uq = alice.difference(bob)
    print(f"Alice unique: {al_uq}")

    bo_uq = bob.difference(alice)
    print(f"Bob unique: {bo_uq}")


if __name__ == "__main__":
    main()
