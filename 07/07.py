import glom
from pathlib import Path

def nested_get(d, *keys):
    for key in keys:
        d = d.get(key, {})
    return d


def day_7(file=None):
    file = file or Path(__file__).parent / "input.txt"
    graph = {"": {}}

    with open(file) as f:
        data = f.read()
        position = ""
        positions = []
        ls_active = False

        for line in data.split("\n"):
            if line.startswith("$ cd "):
                ls_active = False

                if line[5:].startswith("/"):
                    position = line[5:]
                elif line[5:].startswith(".."):
                    position = position.rsplit("/", 2)[0] + "/"
                elif line[5:].startswith("."):
                    pass
                else:
                    position += f"{line[5:]}/"
                    positions.append(position)
            elif line.startswith("$ ls"):
                ls_active = True
            elif ls_active:
                size, name = line.split(" ")
                temp_position = position + name
                position_in_graph = glom.Path(*temp_position.split("/"))

                if size == "dir":
                    glom.assign(graph, position_in_graph, {})
                else:
                    glom.assign(graph, position_in_graph, int(size))

    def get_size(d):
        return sum(get_size(v) for v in d.values() if isinstance(v, dict)) + sum(k for k in d.values() if isinstance(k, int))

    total_size = get_size(graph[""])

    sizes = []
    total = 0
    for p in positions:
        s = get_size(nested_get(graph, *p.rstrip("/").split("/")))
        sizes.append((p.rstrip("/"), s))
        if s < 100000:
            total += s

    for p, s in sorted(sizes, key=lambda x: x[1]):
        if s >= 30000000 - (70000000 - total_size):
            break

    smallest = p, s

    return total, smallest[1]


test_file = Path(__file__).parent / "test.txt"
assert day_7(test_file) == (95437, 24933642)

print(f"Sum of folders bellow 100000: %d, Smallest folder to make space: %d" % day_7())
