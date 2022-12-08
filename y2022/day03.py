from functools import reduce


def get_input():
    with open("inputs/03.txt") as f:
        return [line.strip() for line in f.readlines()]


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle):
    prio = sum(priority(get_duplicate_letter(line)) for line in puzzle)
    return prio


def part2(puzzle):
    prio = sum(priority(get_letter_in_all(lines)) for lines in groups_of_three(puzzle))
    return prio


def get_duplicate_letter(x: str) -> str:
    assert len(x) % 2 == 0
    middle = len(x) // 2
    return get_letter_in_all([x[:middle], x[middle:]])


def get_letter_in_all(lines: list[str]) -> str:
    # Option 1 - check each letter in first line to also be present
    # in all other lines
    for letter in lines[0]:
        if all(letter in line for line in lines[1:]):
            return letter

    raise AssertionError("no common letter found")

    # Option 2 - calculate intersection of all sets of letters
    # there should be only one letter left

    # all_letters = [set(a for a in line) for line in lines]
    # repeated_letters = reduce(lambda s1, s2: s1.intersection(s2), all_letters)
    # assert len(repeated_letters) == 1
    # return repeated_letters.pop()


def groups_of_three(lines: list):
    assert len(lines) % 3 == 0
    for i in range(0, len(lines), 3):
        yield lines[i: i + 3]


def priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    elif letter.isupper():
        return ord(letter) - 38
    else:
        raise TypeError("only letters allowed")


if __name__ == "__main__":
    main()
