def get_input():
    with open("inputs/02.txt") as f:
        return f.read()


def part1(puzzle):
    instructions = [x.split() for x in puzzle.splitlines()]
    forward = sum(int(d) for i, d in instructions if i == "forward")
    depth = sum(int(d) for i, d in instructions if i == "down") - sum(
        int(d) for i, d in instructions if i == "up"
    )
    return forward * depth


def part2(puzzle):
    instructions = [(i, int(d)) for i, d in (x.split() for x in puzzle.splitlines())]
    forward, depth, aim = 0, 0, 0
    for i, d in instructions:
        if i == "forward":
            forward += d
            depth += aim * d
        elif i == "down":
            aim += d
        elif i == "up":
            aim -= d
        else:
            raise Exception()
    return forward * depth


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
