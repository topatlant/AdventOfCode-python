from dataclasses import dataclass

from common import sign


def get_input():
    with open("inputs/09.txt") as f:
        return f.readlines()


def main():
    instructions = get_input()
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))


def part1(puzzle) -> int:
    return part2(puzzle, chain_length=2)


def part2(puzzle, chain_length=10) -> int:
    knots = [Position(0, 0) for _ in range(chain_length)]
    visited = set()

    for instruction in puzzle:
        direction, qty = instruction.split()

        for _ in range(int(qty)):
            knots = step(direction, knots)
            visited.add((knots[-1].x, knots[-1].y))

    return len(visited)


@dataclass
class Position:
    x: int
    y: int


def step(direction: str, knots: list[Position]) -> list[Position]:
    knots[0] = move_head(direction, knots[0])

    for i in range(1, len(knots)):
        knots[i] = move_tail(knots[i - 1], knots[i])

    return knots


def move_head(direction: str, head: Position) -> Position:
    if direction == "U":
        return Position(head.x, head.y + 1)
    if direction == "D":
        return Position(head.x, head.y - 1)
    if direction == "L":
        return Position(head.x - 1, head.y)
    if direction == "R":
        return Position(head.x + 1, head.y)
    raise ValueError("incorrect direction")


def move_tail(leader: Position, follower: Position) -> Position:
    if abs(leader.x - follower.x) <= 1 and abs(leader.y - follower.y) <= 1:
        # max 1 step apart
        return follower

    if leader.y == follower.y:
        # same row -> move left/right
        return Position(follower.x + sign(leader.x - follower.x), follower.y)

    if leader.x == follower.x:
        # same col -> move up/down
        return Position(follower.x, follower.y + sign(leader.y - follower.y))

    # move diagonally
    return Position(
        follower.x + sign(leader.x - follower.x),
        follower.y + sign(leader.y - follower.y),
    )


if __name__ == "__main__":
    main()
