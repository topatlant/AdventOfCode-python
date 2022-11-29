def get_input():
    with open("inputs/01.txt") as f:
        return f.read()


def walk(directions):
    p = []  # list of all positions reached by walking

    position = (0, 0)
    facing = 1  # 1=N, 2=E, 3=S, 4=W

    for d in directions:
        turn = d[0]
        steps = int(d[1:])

        # turn
        if turn == "R":
            facing += 1
        elif turn == "L":
            facing -= 1
        else:
            raise Exception("unknown direction")
        while facing > 4:
            facing -= 4
        while facing < 1:
            facing += 4

        # walk
        for i in range(steps):
            position = walk_one_step(position, facing)
            p.append(position)

    return p


def walk_one_step(position, facing):
    if facing == 1:
        return position[0], position[1] + 1
    elif facing == 2:
        return position[0] + 1, position[1]
    elif facing == 3:
        return position[0], position[1] - 1
    elif facing == 4:
        return position[0] - 1, position[1]


def distance(p):
    return abs(p[0]) + abs(p[1])


def part1(puzzle):
    directions = puzzle.split(", ")
    final_position = walk(directions)[-1]
    return distance(final_position)


def part2(puzzle):
    directions = puzzle.split(", ")
    positions = walk(directions)
    for p in positions:
        if positions.count(p) > 1:
            return distance(p)


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
