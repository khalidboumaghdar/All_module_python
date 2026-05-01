def water_plants(plant_list) -> None:
    """Water each plant in the list; handle invalid plants safely."""
    try:
        print("Opening watering system")

        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")

        print("Watering completed successfully!")

    except ValueError as v:
        print(f"Error: {v}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test watering system with normal and invalid plant data."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    g_plant = ["tomato", "lettuce", "carrots"]
    water_plants(g_plant)

    print("Testing with error...")
    b_plant = ["tomato", None, "carrots"]
    water_plants(b_plant)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
