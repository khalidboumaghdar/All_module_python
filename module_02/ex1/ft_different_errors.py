def garden_operations() -> None:
    """Demonstrate catching common Python errors in garden context."""
    try:
        print("Testing ValueError...")
        int("khalid")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("Testing ZeroDivisionError...")
        a = 10
        a / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        print("Testing KeyError...")
        plants = {"rose": "red", "tulip": "yellow"}
        print(plants["blue"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types() -> None:
    """Run garden_operations and demonstrate multi-error catching."""
    print("=== Garden Error Types Demo ===")

    garden_operations()

    try:
        int("khalid") / 0
        open("file.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
