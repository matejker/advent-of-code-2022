from pathlib import Path

GAME_MAPPING = {
    "A": ["Z", "X", "Y"],
    "B": ["X", "Y", "Z"],
    "C": ["Y", "Z", "X"]
}

ACTION_VALUES = ["X", "Y", "Z"]


def black_rock_scissors(file = None):
    file = file or Path(__file__).parent / "input.txt"

    score = 0
    strategy_score = 0

    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            opponent, you = line.split(" ")
            outcome = GAME_MAPPING[opponent].index(you) * 3
            score += (ACTION_VALUES.index(you) + 1) + outcome

            new_you = GAME_MAPPING[opponent][ACTION_VALUES.index(you)]
            strategy_score += ACTION_VALUES.index(new_you) + 1 + GAME_MAPPING[opponent].index(new_you) * 3


    return score, strategy_score

test_file = Path(__file__).parent / "test.txt"
assert black_rock_scissors(test_file) == (15, 12)

if __name__ == '__main__':
    print("Classic strategy %d, ultra top secret strategy %d" % black_rock_scissors())