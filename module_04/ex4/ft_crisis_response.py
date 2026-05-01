def crisis_handle(file):
    print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
    try:
        with open(file, "r") as f:
            disply = f.read()
            print(f"SUCCESS: Archive recovered - ``{disply}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("Unexpected system anomaly detected")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    list_files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for file in list_files:
        crisis_handle(file)
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
