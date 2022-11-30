def get_input():
    with open("inputs/05.txt") as f:
        return f.read()


def main():
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))


def part1(puzzle):
    return sum(is_nice_part1(x) for x in puzzle.splitlines())


def part2(puzzle):
    return sum(is_nice_part2(x) for x in puzzle.splitlines())


def is_nice_part1(x):
    return (
        has_at_least_three_vowels(x)
        and has_double_letter(x)
        and not contains_bad_string(x)
    )


def is_nice_part2(x):
    return contains_double_pair(x) and contains_repeating_letter_with_gap(x)


def has_at_least_three_vowels(x):
    vowels = ("a", "e", "i", "o", "u")
    n_vowels = sum(1 for s in x if s in vowels)
    return n_vowels >= 3


def has_double_letter(x):
    pred = ""
    for letter in x:
        if letter == pred:
            return True
        pred = letter
    return False


def contains_bad_string(x):
    bad = ("ab", "cd", "pq", "xy")
    for b in bad:
        if b in x:
            return True
    return False


def contains_double_pair(x):
    for i in range(len(x) - 1):
        pair = x[i : i + 2]
        if x.count(pair) >= 2:
            return True
    return False


def contains_repeating_letter_with_gap(x):
    for i in range(len(x) - 2):
        if x[i] == x[i + 2]:
            return True
    return False


if __name__ == "__main__":
    main()
