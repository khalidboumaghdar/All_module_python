import importlib


def main() -> None:
    packages = ["pandas", "numpy", "matplotlib", "requests"]

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    missing = []

    for pkg in packages:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - Ready")
        except ImportError:
            print(f"[MISSING] {pkg} - Please install it")
            missing.append(pkg)
        except Exception as e:
            print(f"An error occurred: {e}")

    if missing:
        print("\nSome packages are missing! Install them with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        return

    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import requests

        response = requests.get(
            "https://jsonplaceholder.typicode.com/comments", timeout=5
            )

        if response.status_code == 200:
            json_data = response.json()

            data = np.array([len(item["body"]) for item in json_data])

        print("\nAnalyzing Matrix data...")

        for i, _ in enumerate(data, 1):
            print(f"\rProcessing {i}/{len(data)} data points...", end="")

        print()
        print("Generating visualization...")

        plt.figure()
        plt.hist(data, bins=20, color="green", alpha=0.7)
        plt.title("Matrix Data Analysis")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete! Results saved to: matrix_analysis.png")

    except ImportError as e:
        print(f"Cannot run analysis: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
