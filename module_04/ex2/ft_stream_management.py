import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    in_id = input("Input Stream active. Enter archivist ID:")
    in_report = input("Input Stream active. Enter status report:")
    print("\n")

    print(
        f"{{[}}STANDARD{{]}} Archive status fro {in_id}:{in_report}\n",
        file=sys.stdout
    )
    print(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n",
        file=sys.stderr
    )
    print("{[}STANDARD{]} Data transmission complete\n", file=sys.stdout)

    print("\nThree-channel communication test successful.", file=sys.stderr)


if __name__ == "__main__":
    main()
