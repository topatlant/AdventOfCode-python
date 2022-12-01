from common import split_by_blanks


def get_input():
    with open("inputs/01.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle):
    elves = split_by_blanks(puzzle)
    return max(get_calory_sum(elf) for elf in elves)


def part2(puzzle):
    elves = split_by_blanks(puzzle)
    calories = [get_calory_sum(elf) for elf in elves]
    calories.sort(reverse=True)
    return sum(calories[:3])


def get_calory_sum(elf: list[str]) -> int:
    return sum(int(line) for line in elf)


if __name__ == "__main__":
    main()
