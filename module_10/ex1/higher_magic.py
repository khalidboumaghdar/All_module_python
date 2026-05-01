from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        return (
            spell1(*args, **kwargs),
            spell2(*args, **kwargs),
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage(x: int) -> int:
    return x


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon")
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {amplified(10)}")


if __name__ == "__main__":
    main()
