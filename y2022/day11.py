from collections import deque
from functools import reduce

from common import split_by_blanks


def get_input():
    with open("inputs/11.txt") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle) -> int:
    # Part1 is using
    # - division by three
    # - but no modulo arithmetics
    return part2(puzzle, rounds=20, pt1=True)


def part2(puzzle, rounds=10000, pt1=False) -> int:
    all_monkeys = parse(puzzle)

    Monkey.part1 = pt1
    if not pt1:
        Monkey.lcm = reduce(lambda x, y: x * y, [m.division for m in all_monkeys])

    for _ in range(rounds):
        one_round(all_monkeys)

    inspections = [m.n_inspected for m in all_monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


class Monkey:
    part1: bool
    lcm: int = None  # least common multiple

    def __init__(
        self,
        starting_items: deque[int],
        operation,
        division_test: int,
        monkey_to_throw: tuple[int, int],
    ):
        self.inventory = starting_items
        self.operation = operation
        self.division = division_test
        self.target_ids = {True: monkey_to_throw[0], False: monkey_to_throw[1]}

        self.n_inspected = 0

    @staticmethod
    def from_definition(puzzle: list[str]) -> "Monkey":
        assert puzzle[0].startswith("Monkey ")
        assert puzzle[1].startswith("Starting items:")
        items = deque([int(x) for x in puzzle[1].split(":")[-1].split(",")])
        assert puzzle[2].startswith("Operation: new = ")
        operation = Operation.parse(puzzle[2].split("=")[-1].strip())
        assert puzzle[3].startswith("Test: divisible by")
        divisible = int(puzzle[3].split()[-1])
        assert puzzle[4].startswith("If true: throw to monkey")
        monkey_true = int(puzzle[4].split()[-1])
        assert puzzle[5].startswith("If false: throw to monkey")
        monkey_false = int(puzzle[5].split()[-1])
        return Monkey(items, operation, divisible, (monkey_true, monkey_false))

    def take_turn(self, all_monkeys: list["Monkey"]) -> None:
        while self.inventory:
            self.inspect_and_throw(self.inventory.popleft(), all_monkeys)

    def inspect_and_throw(self, item: int, all_monkeys) -> None:
        worry_level = self.operation.apply(item)

        if Monkey.part1:
            worry_level = worry_level // 3
        else:
            worry_level = worry_level % Monkey.lcm

        other_monkey = all_monkeys[self.target_ids[worry_level % self.division == 0]]
        other_monkey.catch(worry_level)

        self.n_inspected += 1

    def catch(self, item: int):
        self.inventory.append(item)


class Operation:
    @staticmethod
    def parse(line: str) -> "Operation":
        if line.startswith("old +"):
            return Addition(int(line.split("+")[-1]))
        elif line.startswith("old * old"):
            return Square()
        elif line.startswith("old *"):
            return Multiplication(int(line.split("*")[-1]))
        raise ValueError("unrecognized Monkey Operation")


class Addition(Operation):
    def __init__(self, n: int):
        self.n = n

    def apply(self, item: int):
        return self.n + item


class Multiplication(Operation):
    def __init__(self, n: int):
        self.n = n

    def apply(self, item: int) -> int:
        return self.n * item


class Square(Operation):
    def apply(self, item: int) -> int:
        return item * item


def one_round(monkeys: list[Monkey]) -> None:
    for m in monkeys:
        m.take_turn(monkeys)


def parse(puzzle: list[str]) -> list[Monkey]:
    return [Monkey.from_definition(lines) for lines in split_by_blanks(puzzle)]


if __name__ == "__main__":
    main()
