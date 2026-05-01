def main():

    file = "new_discovery.txt"
    try:
        print("""=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n
Initializing new storage unit: new_discovery.txt
Storage unit created successfully...
        """)
        print("Inscribing preservation data...")

        with open(file, "w") as rs:
            rs.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
            rs.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
            rs.write("{[}ENTRY 003{]} Archived by Data Archivist trainee")

        with open(file, "r") as vault:
            print(vault.read())

        print("""Data inscription complete. Storage unit sealed.
Archive 'new_discovery.txt' ready for long-term preservation.
""", end="")

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
