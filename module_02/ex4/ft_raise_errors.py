def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check plant's health; raise ValueError for invalid inputs."""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(
            f"Water level {water_level} too low (min 1)"
        )

    if water_level > 10:
        raise ValueError(
            f"Water level {water_level} too high (max 10)"
        )

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} too low (min 2)"
        )

    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} too high (max 12)"
        )

    return f"Plant {plant_name} is healthy!"


def test_plant_checks() -> None:
    """Run tests for check_plant_health with good and bad values."""
    print("=== Garden Plant Health Checker ===")

    try:
        print("Testing good values...")
        test1 = check_plant_health("tomato", 5, 6)
        print(test1)
    except ValueError as em:
        print(f"Error: {em}")

    try:
        print("Testing bad water level...")
        test2 = check_plant_health("tomato", 15, 6)
        print(test2)
    except ValueError as em:
        print(f"Error: {em}")

    try:
        print("Testing bad sunlight hours...")
        test3 = check_plant_health("tomato", 5, 0)
        print(test3)
    except ValueError as em:
        print(f"Error: {em}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
