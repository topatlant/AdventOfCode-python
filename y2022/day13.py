from common import split_by_blanks
from functools import cmp_to_key
from itertools import zip_longest
import ast


# import json


def get_input():
    with open("inputs/13.txt") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


def part1(puzzle) -> int:
    indices = [
        i + 1
        for i, ordered in enumerate(
            is_ordered(group) for group in split_by_blanks(puzzle)
        )
        if ordered
    ]
    return sum(indices)


def part2(puzzle) -> int:
    lines = [line for line in puzzle if line] + ["[[2]]", "[[6]]"]
    signals = [parse(line) for line in lines]
    signals.sort(key=cmp_to_key(compare))
    index1 = signals.index([[2]])
    index2 = signals.index([[6]])
    return (index1 + 1) * (index2 + 1)


def is_ordered(group: list[str]) -> bool:
    assert len(group) == 2
    one, two = (parse(line) for line in group)
    return compare(one, two) == -1


def parse(line: str):
    return ast.literal_eval(line)
    # return json.loads(line)


def compare(list1: list, list2: list) -> int:
    for e1, e2 in zip_longest(list1, list2):

        if e1 is None:
            return -1  # right order ("smaller than")
        if e2 is None:
            return 1  # wrong order ("larger than")

        if isinstance(e1, int) and isinstance(e2, int):
            if e1 == e2:
                continue
            return -1 if e1 < e2 else 1

        if isinstance(e1, int) and isinstance(e2, list):
            e1 = [e1]
        elif isinstance(e1, list) and isinstance(e2, int):
            e2 = [e2]

        if isinstance(e1, list) and isinstance(e2, list):
            cmp = compare(e1, e2)
            if cmp == 0:
                continue
            return cmp

        raise ValueError(f"unsupported types for comparison: {type(e1)} and {type(e2)}")

    return 0  # we've run out of elements while comparing so the lists are "equal"


if __name__ == "__main__":
    main()
