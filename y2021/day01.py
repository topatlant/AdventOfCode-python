from itertools import tee


def get_input():
    with open("inputs/01.txt") as f:
        return f.read()


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable):
    """Return overlapping triplets from an iterable"""
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def part1(puzzle):
    depths = [int(x) for x in puzzle.splitlines()]
    return sum(map(lambda x: x[1] > x[0], pairwise(depths)))


def part2(puzzle):
    depths = [int(x) for x in puzzle.splitlines()]
    sliding_windows_sums = map(sum, triplewise(depths))
    return sum(map(lambda x: x[1] > x[0], pairwise(sliding_windows_sums)))


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
