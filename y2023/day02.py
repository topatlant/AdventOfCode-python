from dataclasses import dataclass


def get_input():
    with open("inputs/02.txt") as f:
        return f.readlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle: list[str]) -> int:
    games = parse_puzzle(puzzle)
    return sum(g.id for g in games if is_possible(g))


def part2(puzzle: list[str]) -> int:
    games = parse_puzzle(puzzle)
    return sum(get_power(g) for g in games)


@dataclass
class Set:
    n_red: int
    n_green: int
    n_blue: int

    @classmethod
    def from_str(cls, s: str):
        red = green = blue = 0
        for x in s.split(","):
            match x.strip().split():
                case [n, "blue"]:
                    blue = int(n)
                case [n, "red"]:
                    red = int(n)
                case [n, "green"]:
                    green = int(n)
                case _:
                    raise Exception("unknown color")
        return Set(n_green=green, n_blue=blue, n_red=red)


@dataclass
class Game:
    id: int
    sets: list[Set]

    @classmethod
    def from_line(cls, line: str):
        n, rest = line.split(":")
        if not n.startswith("Game "):
            raise Exception("line ill-formatted")
        n = int(n[5:])
        sets = [Set.from_str(x) for x in rest.split(";")]
        return Game(n, sets)


def parse_puzzle(puzzle: list[str]) -> list[Game]:
    return [Game.from_line(line) for line in puzzle]


def is_possible(game: Game) -> bool:
    max_red = 12
    max_green = 13
    max_blue = 14
    for s in game.sets:
        if s.n_red > max_red or s.n_blue > max_blue or s.n_green > max_green:
            return False
    return True


def get_power(game: Game) -> int:
    min_red = max(s.n_red for s in game.sets)
    min_blue = max(s.n_blue for s in game.sets)
    min_green = max(s.n_green for s in game.sets)
    # print(f"we need {min_red} red, {min_green} green and {min_blue} blue balls")
    return min_green * min_red * min_blue


if __name__ == "__main__":
    main()
