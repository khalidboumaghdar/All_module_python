import math


def main():
    """
    Demonstrate coordinate handling, distance calculation, and error parsing.
    """
    tuple1 = (10, 20, 5)
    x, y, z = tuple1
    distance = math.sqrt(x**2 + y**2 + z**2)
    print("=== Game Coordinate System ===")
    print(f"Position created: ({x}, {y}, {z})")
    print(f"Distance between (0, 0, 0) and ({x}, {y}, {z}): {distance:.2f}")
    print("\n")

    tuple2 = "3,4,0"
    sp = tuple2.split(",")
    x1 = int(sp[0])
    y1 = int(sp[1])
    z1 = int(sp[2])
    distance1 = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f'Parsing coordinates: "{x1}, {y1}, {z1}"')
    print(f"Parsed position: ({x1}, {y1}, {z1})")
    print(
        f"Distance between (0, 0, 0) and ({x1}, {y1}, {z1}): {distance1:.1f}"
    )
    print("\n")

    tuple3 = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{tuple3}"')
    try:
        sp1 = tuple3.split(",")
        int(sp1[0])
        int(sp1[1])
        int(sp1[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print("\n")

    print("Unpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


if __name__ == "__main__":
    main()
