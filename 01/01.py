from pathlib import Path

def calories(file = None):
    file = file or Path(__file__).parent / "input.txt"

    elf_calories = [0]
    with open(file) as f:
        for line in f.readlines():
            if line == "\n":
                elf_calories.append(0)
            else:
                elf_calories[-1] = elf_calories[-1] + int(line.strip("\n"))

    elf_calories.sort(reverse=True)
    return elf_calories[0], sum(elf_calories[:3])


test_file = Path(__file__).parent / "test.txt"
assert calories(test_file) == (24000, 45000)

if __name__ == '__main__':
    print("Most caloric Elf %d, Sum of top 3 %d" % calories())
