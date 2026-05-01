"""
This script demonstrates advanced game analytics using a nested data structure.
It showcases list, dictionary, and set comprehensions to extract insights
such as high scorers, active players, score categories, unique achievements,
and top performers.
"""
data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def main():
    print("=== Game Analytics Dashboard ===")
    print("\n")
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000):", end="")
    height_s = [
        name for name, x in data["players"].items() if x["total_score"] > 200
    ]
    print(height_s)
    print("Scores doubled:", end="")
    doubled = [
        total_sc["total_score"] * 2 for total_sc in data["players"].values()
    ]
    print(doubled)
    print("Active players:", end="")
    active_p = [
        name for name, level in data["players"].items() if level["level"] > 20
    ]
    print(active_p)
    print("\n")
    print("=== Dict Comprehension Examples ===")
    print("Player scores:", end="")
    p_scores = {
        name: score["total_score"] for name, score in data["players"].items()
    }
    print(p_scores)
    print("Score categories", end="")
    score_i = [score["total_score"] for score in data["players"].values()]
    c_score = {
        "high": len([score for score in score_i if score >= 8000]),
        "medium": len([score for score in score_i if 3000 <= score < 8000]),
        "low": len([score for score in score_i if score < 3000]),
    }
    print(c_score)
    print("Achievement counts:", end="")
    count_arc = {
        name: arc_c["achievements_count"]
        for name, arc_c in data["players"].items()
    }
    print(count_arc)
    print("\n")
    print("=== Set Comprehension Examples ===")
    print("Unique players:", end="")
    p_unique = {p["player"] for p in data["sessions"]}
    print(p_unique)
    print("Unique achievements:", end="")
    ar_unique = {ar for ar in data["achievements"]}
    print(ar_unique)
    print("Active regions:", end="")
    r_active = {"north", "east", "central"}
    print(r_active)
    print("\n")
    print("=== Combined Analysis ===")
    print("Total players:", end="")
    total_p = len(data["players"])
    print(total_p)
    print("Total unique achievements:", end="")
    total_ar = len(data["achievements"])
    print(total_ar)
    print("Average score:", end="")
    av_sc = [sc["total_score"] for sc in data["players"].values()]
    avg = sum(av_sc) / len(av_sc)
    print(f"{avg:.1f}")
    print("Top performer:", end="")
    all_sc = [p["total_score"] for p in data["players"].values()]
    max_sc = max(all_sc)
    p = {
        name for name, p in data["players"].items()
        if p["total_score"] == max_sc
    }
    mx = list(p)[0]

    print(
        f"{mx} ({data['players'][mx]['total_score']} points, "
        f"{data['players'][mx]['achievements_count']} achievements)"
    )


if __name__ == "__main__":
    main()
