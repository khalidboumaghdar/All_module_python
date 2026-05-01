class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when plant data is invalid."""
    pass


class WaterError(GardenError):
    """Raised when watering fails."""
    pass


class GardenManager:
    """Manage a garden with plants, watering, and health checks."""

    def __init__(self):
        """Initialize the garden manager with an empty plant dict."""
        self.plants = {}

    def add_plant(self, name: str, water_level: int, sunlight_hours: int):
        """Add a plant with water and sunlight levels.

        Raises PlantError if name is empty.
        """
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": water_level, "sun": sunlight_hours}
            print(f"Added {name} successfully")
        except PlantError as err:
            print(f"Error adding plant: {err}")

    def water_plants(self):
        """Water all plants. Uses finally to close system."""
        print("Watering plants...")
        try:
            print("Opening watering system")
            if not self.plants:
                raise WaterError("No plants to water")
            for name in self.plants:
                print(f"Watering {name} - success")
        except WaterError as err:
            print(f"Caught GardenError: {err}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """Check water and sunlight for each plant; handle invalid data."""
        print("Checking plant health...")
        for name, data in self.plants.items():
            try:
                water = data["water"]
                sun = data["sun"]
                if water < 1:
                    raise PlantError("Water level too low (min 1)")
                if water > 10:
                    raise PlantError("Water level too high (max 10)")
                if sun < 2:
                    raise PlantError("Sunlight hours too low (min 2)")
                if sun > 12:
                    raise PlantError("Sunlight hours too high (max 12)")
                print(f"{name}: healthy (water: {water}, sun: {sun})")
            except PlantError as err:
                print(f"Error checking {name}: {err}")


def main() -> None:
    """Run tests for the GardenManager."""
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 6)
    manager.add_plant("", 3, 4)

    manager.water_plants()
    manager.check_plant_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
