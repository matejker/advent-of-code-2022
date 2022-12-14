from pathlib import Path

STARTING_POINT = (500, 0)

def day14(file=None):
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
            print("".join(mm[493:]))

    matrix[STARTING_POINT[1]][STARTING_POINT[0]] = "+"

    def action(x, y):
        if len(matrix) - 1 == x and matrix[x][y] == ".":
            raise Exception("Found the end")

        if matrix[x][y] == "o":
            if matrix[x][y - 1] == ".":
                return action(x + 1, y - 1)
            elif matrix[x][y + 1] == ".":
                return action(x + 1, y + 1)
            else:
                return x - 1, y

        if matrix[x][y] == ".":
            return action(x + 1, y)

        if matrix[x][y] == "#":
            return x - 1, y


    def action2(x, y):
        if len(matrix) - 1 == x and matrix[x][y] == ".":
            raise Exception("Found the end")

        if matrix[x][y] in ("o", "#"):
            if 8 < x:
                return x - 1, y

            print(matrix[x][y], matrix[x + 1][y - 1], matrix[x + 1][y + 1])

            if matrix[x + 1][y - 1] == ".":
                print(x, y, "left")
                return action2(x + 1, y - 1)
            elif matrix[x + 1][y + 1] == ".":
                print(x, y, "right")
                return action2(x + 1, y + 1)
            return x - 1, y

        if matrix[x][y] == ".":
            print(matrix[x][y])
            return action2(x + 1, y)

    t = True
    while t:
        # for i in range(1, len(matrix[0])):
        try:
            _x, _y = action2(1, 500)
        except Exception as e:
            print(f"{e!r}")
            print(units_of_sand)
            break

        matrix[_x][_y] = "o"
        units_of_sand += 1
        print("")
        show_matrix()

    return units_of_sand

test_file = Path(__file__).parent / "test.txt"
assert day14(test_file) == 0