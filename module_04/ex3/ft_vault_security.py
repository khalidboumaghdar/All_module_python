def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\n SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as cl:
            print(cl.read())

        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as sc:
            sc.write("{[}CLASSIFIED{]} New security protocols archived")
            print("{[}CLASSIFIED{]} New security protocols archived")

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
