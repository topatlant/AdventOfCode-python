from itertools import combinations


def get_input():
    with open("inputs/02.txt") as f:
        return f.read()


def part1(puzzle):
    two = sum(any_letter_n_times(x, 2) for x in puzzle.splitlines())
    three = sum(any_letter_n_times(x, 3) for x in puzzle.splitlines())
    return two * three


def any_letter_n_times(x, n):
    for l in x:
        if x.count(l) == n:
            return 1
    return 0


def part2(puzzle):
    x, y = find_almost_identical_ids(puzzle.splitlines())
    return get_intersection(x, y)


def differs_by_one_char(x, y):
    assert len(x) == len(y)
    n = sum(a != b for a, b in zip(x, y))
    return n == 1


def find_almost_identical_ids(ids):
    for x, y in combinations(ids, 2):
        if differs_by_one_char(x, y):
            return x, y


def get_intersection(x, y):
    assert len(x) == len(y)
    return "".join(a for a, b in zip(x, y) if a == b)


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
