from math import prod
from pathlib import Path


def day_8(file=None):
    file = file or Path(__file__).parent / "input.txt"
    grid = []
    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            grid.append(list(line))

    n, m = len(grid), len(grid[0])

    def is_visible(i, j):
        if not (0 < i < n - 1 and 0 < j < m - 1):
            return True

        # Test left
        if max(grid[i][:j]) < grid[i][j]:
            return True

        # Test right
        if max(grid[i][j + 1:]) < grid[i][j]:
            return True

        # Test up
        if max(grid[k][j] for k in range(i)) < grid[i][j]:
            return True

        # Test down
        if max(grid[k][j] for k in range(i + 1, n)) < grid[i][j]:
            return True

        return False

    def number_of_visible_trees(i, j):
        num = [0, 0, 0, 0]
        # Test left
        for x in grid[i][:j][::-1]:
            num[0] += 1
            if x >= grid[i][j]:
                break

        # Test right
        for x in grid[i][j + 1:]:
            num[1] += 1
            if x >= grid[i][j]:
                break

        # Test up
        for x in [grid[k][j] for k in range(i)][::-1]:
            num[2] += 1
            if x >= grid[i][j]:
                break

        # Test down
        for x in [grid[k][j] for k in range(i + 1, n)]:
            num[3] += 1
            if x >= grid[i][j]:
                break

        return prod(num)


    return sum([is_visible(i, j) for i in range(n) for j in range(m)]), max([number_of_visible_trees(i, j) for i in range(n) for j in range(m)])

test_file = Path(__file__).parent / "test.txt"
assert day_8(test_file) == (21, 8)

print("Number of visible trees: %d, max visibility: %d" % day_8())
