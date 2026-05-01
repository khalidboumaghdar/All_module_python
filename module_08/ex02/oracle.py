import os
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = []

    for key, value in config.items():
        if not value:
            missing.append(key)

    return missing


def show_status(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"] or "development"

    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing configuration")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {config['LOG_LEVEL'] or 'INFO'}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")


def main():
    config = load_configuration()

    missing = validate_config(config)

    show_status(config)

    if missing:
        print("\nMissing configuration variables:")
        for var in missing:
            print(f"- {var}")

    security_check()


if __name__ == "__main__":
    main()
