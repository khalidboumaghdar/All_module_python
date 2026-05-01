def mage_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int):
    total = initial_power

    def accumulator(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str):
    def enchant(item: str):
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault():
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage[key] if key in storage else "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(ice("Shield"))


if __name__ == "__main__":
    main()
