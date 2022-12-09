from pathlib import Path


def day9(file=None, knots=2):
    file = file or Path(__file__).parent / "input.txt"

    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    visited = set()
    rope = [(0, 0)] * knots
    visited.add((0, 0))

    def make_move(z, d):
        return z[0] + d[0], z[1] + d[1]

    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            split_line = line.split(" ")
            dir, n_steps = split_line[0], int(split_line[1])

            for _ in range(n_steps):
                rope[0] = make_move(rope[0], directions[dir])
                for k in range(1, knots):
                    delta = rope[k - 1][0] - rope[k][0], rope[k - 1][1] - rope[k][1]

                    if abs(max(delta, key=abs)) > 1:
                        move = delta[0] // (abs(delta[0]) or 1), delta[1] // (abs(delta[1]) or 1)
                        rope[k] = make_move(rope[k], move)

                visited.add(rope[-1])

    return len(visited)


test_file = Path(__file__).parent / "test.txt"
test_file2 = Path(__file__).parent / "test2.txt"

assert day9(test_file) == 13
assert day9(test_file2, knots=10) == 36

print("Part 1:", day9(knots=2))
print("Part 2:", day9(knots=10))