from pathlib import Path


def marker_detector(file=None, n=4):
    file = file or Path(__file__).parent / "input.txt"

    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            for i in range(len(line)):
                if len(set(line[i:i + n])) == n:
                    yield i + n
                    break


def marker_detector_one_liner(file=Path(__file__).parent / "input.txt", n=4):
    with open(file) as f:
        data = f.read()
        return [next((i + n for i in range(len(l)) if len(set(l[i:i + n])) == n)) for l in data.split("\n")]


test_file = Path(__file__).parent / "test.txt"
assert list(marker_detector(test_file)) == [7, 5, 6, 10, 11]
assert list(marker_detector(test_file, n=14)) == [19, 23, 23, 29, 26]

assert marker_detector_one_liner(test_file) == [7, 5, 6, 10, 11]
assert marker_detector_one_liner(test_file, n=14) == [19, 23, 23, 29, 26]

print(list(marker_detector(n=14)))
