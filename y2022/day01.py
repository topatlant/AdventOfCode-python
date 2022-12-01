from common import split_by_blanks


def get_input():
    with open("inputs/01.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle):
    groups = split_by_blanks(puzzle)
    return max(get_calory_sum(g) for g in groups)


def part2(puzzle):
    groups = split_by_blanks(puzzle)
    calories = [get_calory_sum(g) for g in groups]
    calories.sort(reverse=True)
    return sum(calories[:3])


def get_calory_sum(elve: list[str]) -> int:
    return sum(int(line) for line in elve)


if __name__ == "__main__":
    main()
