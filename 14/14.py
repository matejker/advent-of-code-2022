from pathlib import Path

STARTING_POINT = (500, 0)

def day14(file=None, infinite=False):
    file = file or Path(__file__).parent / "input.txt"

    n, m = 0, 0
    n_min, m_min = 10000, 10000
    units_of_sand = 0

    with open(file) as f:
        rock_lines_str = f.read().splitlines()
        rock_lines = []
        for i, line in enumerate(rock_lines_str):
            rock_lines.append([])

            for coord in line.split(" -> "):
                _x, _y = coord.split(",")
                rock_lines[i].append((int(_x), int(_y)))

                m = max(m, int(_y))
                n = max(n, int(_x))

                m_min = min(m_min, int(_y))
                n_min = min(n_min, int(_x))

    if infinite:
        m = m + 2
        n = n + m
        rock_lines.append([(0, m), (n, m)])

    matrix = [["." for _ in range(n + 1)] for _ in range(m + 1)]
    # Draw rock lines
    for lines in rock_lines:
        for i in range(len(lines) - 1):
            x1, y1 = lines[i]
            x2, y2 = lines[i + 1]

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    matrix[y][x1] = "#"
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    matrix[y1][x] = "#"

    def show_matrix():
        for mm in matrix:
            print("".join(mm[:]))

    # matrix[STARTING_POINT[1]][STARTING_POINT[0]] = "+"

    def sand(x, y):
        if len(matrix) - 1 == x and matrix[x][y] == ".":
            raise Exception("Found the end")

        if matrix[x][y] == ".":
            if matrix[x + 1][y] == ".": # fall
                return sand(x + 1, y)
            if matrix[x + 1][y - 1] in ("o", "#"):
                if matrix[x + 1][y + 1] in ("o", "#"):
                    return x, y
                else:
                    return sand(x + 1, y + 1)
            else:
                return sand(x + 1, y - 1)

    while True:
        try:
            _x, _y = sand(0, 500)
        except Exception as e:
            break

        matrix[_x][_y] = "o"
        units_of_sand += 1

    # show_matrix()

    return units_of_sand


test_file = Path(__file__).parent / "test.txt"
assert day14(test_file) == 24
assert day14(test_file, infinite=True) == 93

print("Part 1:", day14())
print("Part 2:", day14(infinite=True))