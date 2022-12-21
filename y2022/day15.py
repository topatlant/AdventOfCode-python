from dataclasses import dataclass
from typing import Iterator
import re
from itertools import tee, count


def get_input():
    with open("inputs/15.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle, row=2000000) -> int:
    sensors = get_sensors(puzzle)

    excluded_points = set(x for s in sensors for x in s.covered_x_positions(row))

    # beacons don't count
    n_beacons_in_row = len(set(s.beacon[0] for s in sensors if s.beacon[1] == row))

    return len(excluded_points) - n_beacons_in_row


def part2(puzzle, limit=4000000):
    sensors = get_sensors(puzzle)

    for s in sensors:
        for p in s.edge():
            if not (0 <= p[0] <= limit and 0 <= p[1] <= limit):
                continue

            if all(s2.is_outside(p) for s2 in sensors):
                print(p)
                return p[0] * 4000000 + p[1]


coordinates = tuple[int, int]


@dataclass
class Interval:
    start: int
    end: int


def pairwise_indexed(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(count(), a, b)


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    """intervals need to be sorted!"""
    if len(intervals) < 2:
        return intervals

    for index, i1, i2 in pairwise_indexed(intervals):

        if not (i1.end < i2.start - 1 or i2.end < i1.start - 1):
            # can be merged
            merged = Interval(min(i1.start, i2.start), max(i1.end, i2.end))
            return merge_intervals(
                intervals[:index] + [merged] + intervals[index + 2 :]
            )

    # fallthrough means no mergeable intervals found
    return intervals


@dataclass
class Sensor:
    position: coordinates
    beacon: coordinates

    def __post_init__(self):
        self.distance = manhattan_distance(self.position, self.beacon)

    def covered_x_positions(self, row) -> Iterator[int]:
        d = self.distance
        dy = abs(self.position[1] - row)
        if dy > d:
            return []  # we will never reach the row in question

        dx = d - dy
        return range(self.position[0] - dx, self.position[0] + dx + 1)

    def edge(self) -> Iterator[coordinates]:
        d = self.distance + 1
        for x in range(-d, d + 1):
            dy = d - abs(x)
            for y in {-dy, dy}:
                yield self.position[0] + x, self.position[1] + y

    def is_outside(self, p: coordinates) -> bool:
        return manhattan_distance(p, self.position) > self.distance


def manhattan_distance(p1: coordinates, p2: coordinates) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_sensors(puzzle) -> list[Sensor]:
    r = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    sensors = []
    for line in puzzle:
        x_sensor, y_sensor, x_beacon, y_beacon = r.match(line).groups()
        sensors.append(
            Sensor((int(x_sensor), int(y_sensor)), (int(x_beacon), int(y_beacon)))
        )
    return sensors


if __name__ == "__main__":
    main()
