def get_input():
    with open("inputs/04.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle):
    n_fully_contained = sum(is_fully_contained(line) for line in puzzle)
    return n_fully_contained


def part2(puzzle):
    n_overlapping = sum(do_overlap(line) for line in puzzle)
    return n_overlapping


def is_fully_contained(line: str) -> bool:
    first, second = split(line)
    intersection = first.intersection(second)
    return intersection == first or intersection == second


def do_overlap(line: str) -> bool:
    first, second = split(line)
    return len(first.intersection(second)) > 0


def split(line: str) -> tuple[set[int], set[int]]:
    a, b = line.strip().split(",")
    x, y = (int(k) for k in a.split("-"))
    first = set(range(x, y + 1))
    x, y = (int(k) for k in b.split("-"))
    second = set(range(x, y + 1))

    return first, second


if __name__ == "__main__":
    main()
