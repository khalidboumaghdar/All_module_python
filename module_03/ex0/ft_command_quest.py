import sys


def main():
    """Print program info and list command-line arguments."""
    len_args = len(sys.argv) - 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len_args}")
        a = 1
        while a <= len_args:
            print(f"Argument {a}: {sys.argv[a]}")
            a += 1

    print(f"Total arguments: {len(sys.argv)}")  # includes program name


if __name__ == "__main__":
    main()
