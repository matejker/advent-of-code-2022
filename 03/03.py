from pathlib import Path

ALPHABET = "".join([chr(i) for i in range(97, 123)]) + "".join([chr(i) for i in range(65, 65 + 26)])


def rucksack_reorganization(file = None):
    file = file or Path(__file__).parent / "input.txt"

    priorities_sum = 0

    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            n = len(line)
            if n == 0:
                continue

            part1, part2 = set(line[:int(n / 2)]), set(line[int(n / 2):])
            shared_type = part1.intersection(part2).pop()

            priorities_sum += ALPHABET.index(shared_type) + 1


    return priorities_sum


def three_elves_rucksacks(file = None):
    file = file or Path(__file__).parent / "input.txt"
    priorities_sum = 0

    with open(file) as f:
        data = f.read().split("\n")
        n = len(data) // 3

        for i in range(n):
            elf1, elf2, elf3 = set(data[3 * i]), set(data[3 * i + 1]), set(data[3 * i + 2])
            shared_type = elf1.intersection(elf2).intersection(elf3).pop()

            priorities_sum += ALPHABET.index(shared_type) + 1

    return priorities_sum


test_file = Path(__file__).parent / "test.txt"
assert rucksack_reorganization(test_file) == 157
assert three_elves_rucksacks(test_file) == 70

if __name__ == '__main__':
    print("Sum of the priorities of those item types %d" % rucksack_reorganization())
    print("Sum of the priorities for 3 elfs %d" % three_elves_rucksacks())