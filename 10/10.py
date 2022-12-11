from pathlib import Path


def day10(file=None):
    file = file or Path(__file__).parent / "input.txt"

    cycle_values = [1]

    with open(file) as f:
        data = f.read().split("\n")
        for line in data:
            if " " in line:
                _, value = line.split(" ")
                cycle_values.extend([cycle_values[-1], cycle_values[-1] + int(value)])
            else:
                cycle_values.append(cycle_values[-1])

    # Draw
    string = ""
    for i, v in enumerate(cycle_values):
        i_mod_40 = i % 40
        if i_mod_40 - 1 <= v <= i_mod_40 + 1:
            string += "#"
        else:
            string += "."
        if i_mod_40 == 39:
            string += "\n"
    print(string)

    cycles = (20, 60, 100, 140, 180, 220)
    return sum([cycle_values[v - 1] * v for v in cycles])


test_file = Path(__file__).parent / "test.txt"
assert day10(test_file) == 13140
print("Part1: ", day10())