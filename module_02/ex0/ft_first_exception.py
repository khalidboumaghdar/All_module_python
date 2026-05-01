def check_temperature(temp_str):
    """Check if temperature is suitable for plants (0–40°C)."""
    try:
        tmp = int(temp_str)
        if tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
            return None
        if tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
            return None

        print(f"Temperature {tmp}°C is perfect for plants!")
        return tmp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


if __name__ == "__main__":
    """Run tests for check_temperature with valid and invalid inputs."""
    print("=== Garden Temperature Checker ===")

    print("Testing temperature: 25")
    check_temperature(25)

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature(100)

    print("Testing temperature: -50")
    check_temperature(-50)

    print("All tests completed - program didn't crash!")
