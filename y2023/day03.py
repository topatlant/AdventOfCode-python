import re
from dataclasses import dataclass
from math import prod


def get_input():
    with open("inputs/03.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: list[str]) -> int:
    numbers, symbols = parse_puzzle(puzzle)
    return sum(
        number.n for number in numbers if number.is_adjacent_to_any_symbol(symbols)
    )


def part2(puzzle):
    numbers, symbols = parse_puzzle(puzzle)
    return sum(s.gear_ratio(numbers) for s in symbols)


@dataclass
class Coord:
    x: int
    y: int

    def is_adjacent(self, other: "Coord") -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1


@dataclass
class Number:
    n: int
    coord: Coord

    def is_adjacent_to_symbol(self, s: "Symbol"):
        for offset in range(len(str(self.n))):
            if s.coord.is_adjacent(Coord(self.coord.x + offset, self.coord.y)):
                return True
        return False

    def is_adjacent_to_any_symbol(self, symbols: list["Symbol"]):
        return any(self.is_adjacent_to_symbol(symbol) for symbol in symbols)


@dataclass
class Symbol:
    s: str
    coord: Coord

    def gear_ratio(self, numbers: list[Number]):
        if self.s != "*":
            return 0
        adj_numbers = [x for x in numbers if x.is_adjacent_to_symbol(self)]
        if len(adj_numbers) != 2:
            return 0
        return prod(x.n for x in adj_numbers)


def parse_puzzle(puzzle: list[str]):
    numbers = []
    symbols = []
    numbers_rex = re.compile(r"\d+")
    symbol_rex = re.compile(r"[^\.\d]")
    for y, line in enumerate(puzzle):
        for m in numbers_rex.finditer(line.strip()):
            n = int(m[0])  # the number
            x = m.start()
            numbers.append(Number(n, Coord(x, y)))

        for m in symbol_rex.finditer(line.strip()):
            s = m[0]  # the symbol itself
            x = m.start()
            symbols.append(Symbol(s, Coord(x, y)))

    return numbers, symbols


if __name__ == "__main__":
    main()
