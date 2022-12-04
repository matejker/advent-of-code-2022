from pathlib import Path

ID = list(range(1, 100))


def camp_cleanup(file = None):
    file = file or Path(__file__).parent / "input.txt"

    subset_score = 0
    overlap_score = 0

    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            elf1, elf2 = line.split(",")
            e11, e12 = elf1.split("-")
            e21, e22 = elf2.split("-")

            set_1, set_2 = set(ID[int(e11) - 1:int(e12)]), set(ID[int(e21) - 1:int(e22)])

            is_subset = set_1.issubset(set_2) or set_2.issubset(set_1)
            overlap = set_1.intersection(set_2)
            subset_score += is_subset * 1
            overlap_score += (len(overlap) > 0) * 1

    return subset_score, overlap_score

test_file = Path(__file__).parent / "test.txt"
assert camp_cleanup(test_file) == (2, 4)

if __name__ == '__main__':
    print("Subsets number %d, overlap number %d" % camp_cleanup())