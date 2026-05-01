

def main():
    try:
        print("""=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===
\nAccessing Storage Vault: ancient_fragment.txt
Connection established...\n""")
        file = open("ancient_fragment.txt", "r")

        print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except Exception as f:
        print(f"Error : {f}")
        print("\nData recovery incomplete.")


if __name__ == "__main__":
    main()
