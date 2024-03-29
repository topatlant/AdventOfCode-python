from dataclasses import dataclass

SHINY_GOLD = "shiny gold"


def get_input():
    with open("inputs/07.txt") as f:
        return [line.strip() for line in f]


def main():
    puzzle = get_input()
    print("Part1:", part1(puzzle))
    print("Part2:", part2(puzzle))


def part1(puzzle):
    all_bags = parse_bags(puzzle)

    return sum(
        can_contain_shiny_gold(all_bags, color)
        for color in all_bags
        if color != SHINY_GOLD
    )


def part2(puzzle):
    all_bags = parse_bags(puzzle)
    return contains_recursive(all_bags, SHINY_GOLD) - 1
    # -1 -> without the shiny gold bag itself


@dataclass
class Bag:
    color: str
    contains: list[tuple[int, str]]  # quantity and color of contained bags

    @staticmethod
    def from_line(line: str) -> "Bag":
        assert line.endswith(".")
        line = line[:-1]
        own_color, contains = line.split(" bags contain ")

        if contains == "no other bags":
            return Bag(color=own_color, contains=[])

        sub_bags = contains.split(", ")
        return Bag(color=own_color, contains=[Bag.get_qty_col(b) for b in sub_bags])

    @staticmethod
    def get_qty_col(b: str) -> tuple[int, str]:
        components = b.split()
        assert components[-1] in ("bags", "bag")
        qty = int(components[0])
        color = " ".join(components[1:-1])
        return qty, color


def parse_bags(puzzle: list[str]) -> dict[str, Bag]:
    all_bags = {}
    for line in puzzle:
        b = Bag.from_line(line)
        all_bags[b.color] = b
    return all_bags


def can_contain_shiny_gold(all_bags: dict[str, Bag], bag_color: str) -> bool:
    if bag_color == SHINY_GOLD:
        return True
    for sub_bag in all_bags[bag_color].contains:
        if can_contain_shiny_gold(all_bags, sub_bag[1]):
            return True
    return False


def contains_recursive(all_bags: dict[str, Bag], bag_color: str) -> int:
    bag = all_bags[bag_color]
    if not bag.contains:
        return 1  # bag itself, no sub-bags

    return 1 + sum(b[0] * contains_recursive(all_bags, b[1]) for b in bag.contains)


if __name__ == "__main__":
    main()
