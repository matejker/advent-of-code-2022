from pathlib import Path
from typing import Tuple, List
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Sensor:
    def __init__(self, position: Tuple[int, int], beacon: Tuple[int, int]):
        self.position = position
        self.distance = self.count_distance(beacon)

    def count_distance(self, beacon: Tuple[int, int]) -> int:
        return abs(self.position[0] - beacon[0]) + abs(self.position[1] - beacon[1])

    def is_under_radar(self, coord: Tuple[int, int]) -> bool:
        return self.count_distance(coord) <= self.distance

    def max_reach(self) -> Tuple[int, int]:
        return self.position[0] + self.distance, self.position[1] + self.distance

    def min_reach(self, position: Tuple[int, int] = None) -> Tuple[int, int]:
        position = position or self.position
        return position[0] - self.distance, position[1] - self.distance

    def plot(self):
        polygon = [
            (self.position[0] + self.distance, self.position[1]),
            (self.position[0], self.position[1] + self.distance),
            (self.position[0] - self.distance, self.position[1]),
            (self.position[0], self.position[1] - self.distance),
            (self.position[0] + self.distance, self.position[1])
        ]
        # plt.plot(*zip(*polygon), color="red", alpha=0.2)
        plt.fill(*zip(*polygon), color="red", alpha=0.2)

    def get_borders(self, n_max):
        for i in range(0, self.distance + 1):
            j = self.distance + 1 - i
            if 0 <= self.position[0] + i <= n_max and 0 <= self.position[1] + j <= n_max:
                yield self.position[0] + i, self.position[1] + j
            if 0 <= self.position[0] + i <= n_max and 0 <= self.position[1] - j <= n_max:
                yield self.position[0] + i, self.position[1] - j
            if 0 <= self.position[0] - i <= n_max and 0 <= self.position[1] + j <= n_max:
                yield self.position[0] - i, self.position[1] + j
            if 0 <= self.position[0] - i <= n_max and 0 <= self.position[1] - j <= n_max:
                yield self.position[0] - i, self.position[1] - j


def day15(file=None, check_line=2000000, max_search=4000000):
    file = file or Path(__file__).parent / "input.txt"
    sensors: List[Sensor] = []
    beacons = set()
    unavailable_positions = 0
    offset = len("Sensor at x=")

    with open(file) as f:
        lines = f.read().splitlines()
        for line in lines:
            position, beacon = line[offset:].split(": closest beacon is at x=")
            position = tuple(map(int, position.split(", y=")))
            beacon = tuple(map(int, beacon.split(", y=")))
            sensors.append(Sensor(position, beacon))
            beacons.add(beacon)

    borders = set()
    for s in sensors:
        borders.update(set(list(s.get_borders(max_search))))

    for b in borders:
        under_radar = True
        for s in sensors:
            under_radar = under_radar and not s.is_under_radar(b)

        if under_radar:
            print(b)
            return b[0] * 4000000 + b[1]

    x_min, x_max = min(ss.min_reach()[0] for ss in sensors), max(ss.max_reach()[0] for ss in sensors)

    for i in range(x_min - 10, x_max + 10):
        if (i, check_line) in beacons:
            continue


        for s in sensors:
            if s.is_under_radar((i, check_line)):
                unavailable_positions += 1
                break

    # plt.figure(figsize=(100, 100))
    #
    # plt.xlim(0, max_search)
    # plt.ylim(0, max_search)
    #
    # for s in sensors:
    #     s.plot()
    # plt.savefig(f'sensors_{unavailable_positions}.png')

    # print(f"Unavailable positions: {unavailable_positions}")
    # return unavailable_positions


test_file = Path(__file__).parent / "test.txt"
# assert day15(test_file, check_line=10, max_search=20) == 26
assert day15(test_file, check_line=10, max_search=20) == 56000011

if __name__ == "__main__":
    print("Part 1 ", day15())