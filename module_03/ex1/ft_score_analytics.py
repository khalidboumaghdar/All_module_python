import sys


def main():
    """
    Process player scores from command-line arguments and display analytics.
    Shows total, average, high, low, and score range.
    """
    try:
        len_argv = len(sys.argv) - 1
        i = 1
        sum_total = 0

        if len_argv == 0:
            raise ValueError(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ..."
            )

        list_scor = []
        while i <= len_argv:
            argv = int(sys.argv[i])
            list_scor.append(argv)
            i += 1

        print("=== Player Score Analytics ===")
        print("Scores processed:", end=" ")
        print(list_scor)
        print(f"Total players: {i - 1}")

        sum_total = sum(list_scor)
        print(f"Total score: {sum_total}")
        print(f"Average score: {sum_total / len_argv}")

        heigh_scor = max(list_scor)
        print(f"High score: {heigh_scor}")

        min_sc = min(list_scor)
        print(f"Low score: {min_sc}")

        range_sc = heigh_scor - min_sc
        print(f"Score range: {range_sc}\n")

    except ValueError:
        print("=== Player Score Analytics ===")
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )


if __name__ == "__main__":
    main()
