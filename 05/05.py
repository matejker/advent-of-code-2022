from copy import deepcopy
from pathlib import Path


def read_file(file):
    with open(file) as f:
        data = f.read()

        stacks_text, instruction_text = data.split("\n\n")

        return stacks_text, instruction_text


def create_stacks(stack_text):
    rows = stack_text.split("\n")
    stacks = {int(i): [] for i in rows[-1].strip().split("   ")}
    for row in rows[:-1][::-1]:
        for i, c in enumerate(row.replace("    ", " ").split(" ")):
            if c:
                stacks[i + 1].append(c.strip("[").strip("]"))

    return stacks


def parse_instructions(instruction_text):
    instructions = []

    for inst in instruction_text.split("\n"):
        move = inst[5:].split(" from ")[0]
        _from = inst[5:].split(" from ")[1].split(" to ")[0]
        to =  inst[5:].split(" from ")[1].split(" to ")[1]

        instructions.append([int(move), int(_from), int(to)])

    return instructions


def follow_instructions(stacks, instructions, part2):
    for move, _from, to in instructions:
        cubes = deepcopy(stacks[_from][-move:])
        stacks[_from] = stacks[_from][:-move]
        if part2:
            stacks[to].extend(cubes)
        else:
            stacks[to].extend(cubes[::-1])

    return "".join([s.pop() for _, s in stacks.items()])


def test(part2=False):
    test_file = Path(__file__).parent / "test.txt"
    stacks_text, instruction_text = read_file(test_file)
    instructions = parse_instructions(instruction_text)
    stacks = create_stacks(stacks_text)

    return follow_instructions(stacks, instructions, part2)


def day5(part2=False):
    file = Path(__file__).parent / "input.txt"
    stacks_text, instruction_text = read_file(file)
    instructions = parse_instructions(instruction_text)
    stacks = create_stacks(stacks_text)

    return follow_instructions(stacks, instructions, part2)


assert test() == "CMZ"
assert test(part2=True) == "MCD"
print(day5(part2=True))