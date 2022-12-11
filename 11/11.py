from math import prod
from pathlib import Path


def day11(file=None, divide_by_three=True, rounds=20):
    file = file or Path(__file__).parent / "input.txt"
    mp = {}

    with open(file) as f:
        data = f.read()
        monkeys = data.split("\n\n")
        for monkey in monkeys:
            monkey_id = 0
            for m in monkey.split("\n"):
                if m.startswith("Monkey "):
                    monkey_id = int(m[-2:-1])
                    mp[monkey_id] = {"throw_to": {"true": 0, "false": 0}, "counter": 0}
                elif m.startswith("  Starting items: "):
                    mp[monkey_id]["levels"] = [int(i) for i in m[18:].split(", ")]
                elif m.startswith("  Operation: new = "):
                    mp[monkey_id]["operation"] = m[19:]
                elif m.startswith("  Test: divisible by "):
                    mp[monkey_id]["test"] = int(m[20:])
                elif m.startswith("    If true: throw to monkey "):
                    mp[monkey_id]["throw_to"]["true"] = int(m[-1])
                elif m.startswith("    If false: throw to monkey "):
                    mp[monkey_id]["throw_to"]["false"] = int(m[-1])

    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Statement
    field_size = prod(v["test"] for v in mp.values())

    n = len(mp)
    for t in range(n * rounds):
        i = t % n
        for worry_level in mp[i]["levels"]:
            mp[i]["counter"] += 1

            new_worry_level = eval(mp[i]["operation"].replace("old", str(worry_level)))
            new_worry_level %= field_size
            if divide_by_three:
                new_worry_level //= 3

            is_divisible = str(new_worry_level % mp[i]["test"] == 0).lower()
            mp[mp[i]["throw_to"][is_divisible]]["levels"].append(new_worry_level)

        # Delete old levels
        mp[i]["levels"] = []

    inspected = []
    for monkey in mp:
        # print(f"Monkey {monkey} inspected items {mp[monkey]['counter']} times.")
        inspected.append(mp[monkey]["counter"])

    inspected.sort(reverse=True)
    return inspected[0] * inspected[1]


test_file = Path(__file__).parent / "test.txt"
assert day11(test_file) == 10605
assert day11(test_file, divide_by_three=False, rounds=10000) == 2713310158

print("Part 1:", day11())
print("Part 2:", day11(divide_by_three=False, rounds=10000))
