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
                x, y = coord.split(",")
                rock_lines[i].append((int(x), int(y)))

                m = max(m, int(y))
                n = max(n, int(x))

                m_min = min(m_min, int(y))
                n_min = min(n_min, int(x))


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
    t = True
    while t:
        # for i in range(1, len(matrix[0])):
        try:
            x, y = action(1, 500)
        except Exception as e:
            print(f"{e!r}")
            print(units_of_sand)
            # t = False
            break

        matrix[x][y] = "o"
        units_of_sand += 1
        print("")
        show_matrix()

    return units_of_sand

test_file = Path(__file__).parent / "test.txt"
assert day14(test_file) == 0