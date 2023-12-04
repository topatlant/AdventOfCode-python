def get_input():
    with open("inputs/04.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle) -> int:
    return sum(get_card_points(line) for line in puzzle)


def part2(puzzle) -> int:
    n_cards = [1] * len(puzzle)

    for i, line in enumerate(puzzle):
        n_wins = n_winning_numbers(line)
        n_copies = n_cards[i]
        for j in range(n_wins):
            n_cards[i + 1 + j] += n_copies

    return sum(n_cards)


def n_winning_numbers(line: str) -> int:
    winning_numbers = set(int(x) for x in line.split(":")[1].split("|")[0].split())
    our_numbers = set(int(x) for x in line.split(":")[1].split("|")[1].split())
    return len(winning_numbers.intersection(our_numbers))


def get_card_points(line: str) -> int:
    n_wins = n_winning_numbers(line)

    if n_wins == 0:
        return 0

    return 2 ** (n_wins - 1)


if __name__ == "__main__":
    main()
