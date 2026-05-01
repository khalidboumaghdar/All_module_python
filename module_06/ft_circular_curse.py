from alchemy.grimoire import validate_ingredients, record_spell
from alchemy.grimoire.spellbook import record_spell as late_import_spell

print("=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
result0 = validate_ingredients("fire air")
print(f'validate_ingredients("fire air"):     {result0}')
result1 = validate_ingredients("dragon scales")
print(f'validate_ingredients("dragon scales"): {result1}')
print("\nTesting spell recording with validation:")
result2 = record_spell("Fireball", "fire air")
result3 = record_spell("Dark Magic", "shadow")
print(f'record_spell("Fireball", "fire air"):    {result2}')
print(f'record_spell("Dark Magic", "shadow"):    {result3}')

print("\nTesting late import technique:")
result4 = late_import_spell("Lightning", "air")
print(f'record_spell("Lightning", "air"):       {result4}')

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
