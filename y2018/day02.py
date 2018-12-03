import string


def get_input():
    return open("input_day02.txt").read()


def part1(puzzle):
    two = sum(any_letter_n_times(x, 2) for x in puzzle.splitlines())
    three = sum(any_letter_n_times(x, 3) for x in puzzle.splitlines())
    return two * three


def any_letter_n_times(x, n):
    for l in string.ascii_lowercase:
        if x.count(l) == n:
            return 1
    return 0


def part2(puzzle):
    pass


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
