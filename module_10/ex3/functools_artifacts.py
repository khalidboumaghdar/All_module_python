from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(x):
        return "Unknown spell"

    @spell.register(int)
    def _(x: int):
        return f"Damage spell: {x}"

    @spell.register(str)
    def _(x: str):
        return f"Enchantment: {x}"

    @spell.register(list)
    def _(x: list):
        return [spell(i) for i in x]

    return spell


def base_enchant(power, element, target):
    return f"{element} enchant ({power}) on {target}"


def main():
    print("Testing spell reducer...")
    nums = [10, 20, 30, 40]
    print("Sum:", spell_reducer(nums, "add"))
    print("Product:", spell_reducer(nums, "multiply"))
    print("Max:", spell_reducer(nums, "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))


if __name__ == "__main__":
    main()
