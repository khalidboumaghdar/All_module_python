class GardenError(Exception):
    """Base class for all garden-related custom errors."""
    def __init__(self, er_msg="A garden error occurred"):
        super().__init__(er_msg)


class PlantError(GardenError):
    """Raised for plant-specific errors."""
    def __init__(self, er_msg="A plant-related error occurred"):
        super().__init__(er_msg)


class WaterError(GardenError):
    """Raised for watering-specific errors."""
    def __init__(self, er_msg="A watering-related error occurred"):
        super().__init__(er_msg)


def test_erorr() -> None:
    """Demonstrate custom garden errors and their handling."""
    print("=== Custom Garden Errors Demo ===")

    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as p:
        print(f"Caught PlantError: {p}")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as w:
        print(f"Caught WaterError: {w}")

    print("Testing catching all garden errors...")
    for err_raise in [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]:
        try:
            raise err_raise
        except (PlantError, WaterError) as w:
            print(f"Caught GardenError: {w}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_erorr()
