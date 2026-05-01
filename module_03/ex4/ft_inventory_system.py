data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 5,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common",
        },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare",
        },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common",
        },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary",
        },
        "code_bow": {
            "type": "weapon",
            "value": 200,
            "rarity": "uncommon",
        },
    },
}


def main():
    """Display player inventories, perform transactions, and show analytics."""
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")

    alice = data["players"]["alice"]
    alice_items = alice["items"]
    catalog = data["catalog"]

    t_value = 0
    t_items = 0
    find_categorei = {}

    for name, quantity in alice_items.items():
        info = catalog[name]
        type_i = info["type"]
        value_i = info["value"]
        rarity_i = info["rarity"]

        sum_i = quantity * value_i
        t_value += sum_i
        t_items += quantity

        print(
            f"{name} ({type_i}, {rarity_i}): "
            f"{quantity}x @ {value_i} gold each = "
            f"{sum_i} gold"
        )

        if type_i not in find_categorei:
            find_categorei[type_i] = 0
        find_categorei[type_i] += quantity

    print(f"\nInventory value: {t_value} gold")
    print(f"Item count: {t_items} items")
    print("Categories :", end=" ")

    count = 0
    total = len(find_categorei)

    for category in find_categorei:
        print(
            f"{category}({find_categorei[category]})",
            end="",
        )
        count += 1
        if count < total:
            print(", ", end="")

    print("\n")

    alice_items = data["players"]["alice"]["items"]
    bob_items = data["players"]["bob"]["items"]

    print("=== Transaction: Alice gives Bob 2 potions ===")

    if alice_items.get("health_byte", 0) >= 2:
        alice_items["health_byte"] -= 2
        bob_items["health_byte"] = (
            bob_items.get("health_byte", 0) + 2
        )
        print("Transaction successful!")
    else:
        print("Transaction faild!")

    print("\n=== Updated Inventories ===")
    print("Alice potions: ", alice_items["health_byte"])
    print("Bob potions: ", bob_items["health_byte"])

    print("\n=== Inventory Analytics ===")

    most_value = 0
    most_value_p = ""

    for name, data_p in data["players"].items():
        total = 0

        for name_i, qty in data_p["items"].items():
            value_i = data["catalog"][name_i]["value"]
            total += value_i * qty

        if total > most_value:
            most_value = total
            most_value_p = name

    print(
        f"Most valuable player: "
        f"{most_value_p.capitalize()} "
        f"({most_value} gold)"
    )

    most_items = 0
    most_items_p = ""

    for name, data_p in data["players"].items():
        count = 0
        for qty in data_p["items"].values():
            count += qty

        if count > most_items:
            most_items = count
            most_items_p = name

    print(
        f"Most items: "
        f"{most_items_p.capitalize()} "
        f"({most_items} items)"
    )

    itmes_i = []
    for item, info in data["catalog"].items():
        if info["rarity"] in ["rare", "legendary"]:
            itmes_i.append(item)

    print("Rarest items:", ", ".join(itmes_i))


if __name__ == "__main__":
    main()
