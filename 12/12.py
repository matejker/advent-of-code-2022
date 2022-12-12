from pathlib import Path
from heapq import heappop, heapify


def dijkstra(graph, source, target):
    path = []
    if source == target:
        return path

    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    queue = list(graph.keys())

    def make_heap(distance, q):
        return [(di, n) for n, di in distance.items() if n in q]

    dist[source] = 0

    heap = make_heap(dist, queue)
    heapify(heap)

    while len(queue) > 0:
        d, v = heappop(heap)
        queue.remove(v)

        for u in graph[v]:
            alt = d + 1
            if alt < dist[u]:
                dist[u] = alt
                prev[u] = v
        heap = make_heap(dist, queue)
        heapify(heap)

    last_node = target
    m = sum(len(s) for s in graph.values())

    # Iterate till the source is not in the path, or we have visited all edges
    while source not in path and m > 0:
        path.append(last_node)
        last_node = prev[last_node]
        m -= 1

    if m == 0:
        raise ValueError(f"Source {source} is not connected with {target}")

    return dist


def day12(file=None):
    file = file or Path(__file__).parent / "input.txt"

    graph = {}
    matrix = []
    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            matrix.append(list(line))

    n, m = len(matrix), len(matrix[0])

    start_position = (0, 0)
    end_position = (-1, -1)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            graph[(i, j)] = set()

            if matrix[i][j] == "S":
                start_position = (i, j)
                matrix[i][j] = "a"
            elif matrix[i][j] == "E":
                end_position = (i, j)
                matrix[i][j] = "z"

    for i in range(n):
        for j in range(m):
            for d in directions:
                x, y = i + d[0], j + d[1]

                if 0 <= x < n and 0 <= y < m and ord(matrix[x][y]) >= ord(matrix[i][j]) - 1:
                    graph[(i, j)].add((x, y))

    distances = dijkstra(graph, end_position, start_position)

    edges = [(0, j) for j in range(m)] + [(n - 1, j) for j in range(m)] + \
            [(i, 0) for i in range(n)] + [(i, m - 1) for i in range(n)]

    a_edges = [(i, j) for i, j in edges if matrix[i][j] == "a"]

    return distances[start_position], min(distances.get(e, float("inf")) for e in a_edges)


def bfs(graph, start, target):
    queue = [(start, 0)]
    visited = set()
    distances = {target: 0}
    while queue:
        node, dist = queue.pop(0)
        if node == target:
            distances[node] = dist
            return distances
        if node in visited:
            continue
        visited.add(node)
        distances[node] = dist
        for n in graph[node]:
            queue.append((n, dist + 1))
    return -1


def day12_bfs(file=None):
    file = file or Path(__file__).parent / "input.txt"

    graph = {}
    matrix = []
    with open(file) as f:
        data = f.read()
        for line in data.split("\n"):
            matrix.append(list(line))

    n, m = len(matrix), len(matrix[0])

    start_position = (0, 0)
    end_position = (-1, -1)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            graph[(i, j)] = set()

            if matrix[i][j] == "S":
                start_position = (i, j)
                matrix[i][j] = "a"
            elif matrix[i][j] == "E":
                end_position = (i, j)
                matrix[i][j] = "z"

    for i in range(n):
        for j in range(m):
            for d in directions:
                x, y = i + d[0], j + d[1]

                if 0 <= x < n and 0 <= y < m and ord(matrix[x][y]) >= ord(matrix[i][j]) - 1:
                    graph[(i, j)].add((x, y))

    distances = bfs(graph, end_position, start_position)

    edges = [(0, j) for j in range(m)] + [(n - 1, j) for j in range(m)] + \
            [(i, 0) for i in range(n)] + [(i, m - 1) for i in range(n)]

    a_edges = [(i, j) for i, j in edges if matrix[i][j] == "a"]

    return distances[start_position], min(distances.get(e, float("inf")) for e in a_edges)


test_file = Path(__file__).parent / "test.txt"
# print(day12_bfs(test_file))
assert day12_bfs(test_file) == (31, 29)
print("Part 1: %d, Part 2: %d" % day12_bfs())
