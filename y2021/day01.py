from common.itertools import pairwise, triplewise


def get_input():
    with open("inputs/01.txt") as f:
        return f.read()


def main():
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))


def part1(puzzle):
    depths = [int(x) for x in puzzle.splitlines()]
    return sum(map(lambda x: x[1] > x[0], pairwise(depths)))


def part2(puzzle):
    depths = [int(x) for x in puzzle.splitlines()]
    sliding_windows_sums = map(sum, triplewise(depths))
    return sum(map(lambda x: x[1] > x[0], pairwise(sliding_windows_sums)))


if __name__ == "__main__":
    main()
