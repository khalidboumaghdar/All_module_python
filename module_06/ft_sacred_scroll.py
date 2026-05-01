import alchemy
from alchemy import elements

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print(f"alchemy.elements.create_fire(): {elements.create_fire()}")
print(f"alchemy.elements.create_water(): {elements.create_water()}")
print(f"alchemy.elements.create_earth(): {elements.create_earth()}")
print(f"alchemy.elements.create_air(): {elements.create_air()}")

print("\nTesting package-level access (controlled by __init__.py):")
print(f"alchemy.create_fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")

try:
    alchemy.create_earth()
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    alchemy.create_air()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
