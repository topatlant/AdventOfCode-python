def get_input():
    return open("input_day01.txt").read()


def part1(puzzle):
    return puzzle.count("(") - puzzle.count(")")


def part2(puzzle):
    floor = 0
    for i, c in enumerate(puzzle):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i + 1


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
