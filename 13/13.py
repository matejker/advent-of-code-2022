from pathlib import Path
from functools import cmp_to_key


def is_right_ordered(left, right, idx=0):
    if isinstance(left, int) or left is None:
        left = [left]
    if isinstance(right, int) or right is None:
        right = [right]

    for i, l in enumerate(left):
        if len(right) <= i:
            return False

        if isinstance(l, list) or isinstance(right[i], list):
            return is_right_ordered(l, right[i], idx + i)

        if l > right[i]:
            return False

    return True


def try_again(left, right):
    if type(left) != type(right):
        if type(left) == int:
            return try_again([left], right)
        else:
            return try_again(left, [right])

    if type(left) == int:
        if left == right:
            return None
        return left < right

    for l, r in zip(left, right):
        a = try_again(l, r)
        if a is not None:
            return a

    if len(left) != len(right):
        return len(left) < len(right)


def compare(left, right):
    return 1 - try_again(left, right) * 2


def day13(file=None):
    file = file or Path(__file__).parent / "input.txt"

    with open(file) as f:
        data = f.read()
        packets = data.split("\n\n")

        sum_idx = 0
        for i, packet in enumerate(packets):
            left, right = packet.split("\n")

            left = eval(left)
            right = eval(right)

            a = try_again(left, right)

            sum_idx += (i + 1) * a

        new_packets = [eval(p) for pa in packets for p in pa.split("\n")] + [[[2]]] + [[[6]]]
        s = sorted(new_packets, key=cmp_to_key(compare))

    return sum_idx, (s.index([[2]]) + 1) * (s.index([[6]]) + 1)


test_file = Path(__file__).parent / "test.txt"
assert day13(test_file) == (13, 140)
print("Part 1: %d, Part 2: %d" % day13())
