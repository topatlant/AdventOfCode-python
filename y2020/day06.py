from common import split_by_blanks


def get_input():
    with open("inputs/06.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    print("Part2:", part2(puzzle))


def part1(puzzle):
    groups = split_by_blanks(puzzle)
    return sum(get_unique_count(g) for g in groups)


def part2(puzzle):
    groups = split_by_blanks(puzzle)
    return sum(get_all_answered_count(g) for g in groups)


def get_unique_count(answers: list[str]) -> int:
    return len(get_used_letters(answers))


def get_all_answered_count(answers: list[str]) -> int:
    letters = get_used_letters(answers)
    count = 0
    for letter in letters:
        if all(letter in line for line in answers):
            count += 1
    return count


def get_used_letters(answers: list[str]) -> set[str]:
    letters = set(char for line in answers for char in line)
    return letters


if __name__ == "__main__":
    main()
