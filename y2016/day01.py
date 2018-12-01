def get_input():
    return open("input_day01.txt").read()


def part1(puzzle):
    directions = puzzle.split(", ")

    position = [0, 0]
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
        if facing == 1:
            position[1] += steps
        elif facing == 2:
            position[0] += steps
        elif facing == 3:
            position[1] -= steps
        elif facing == 4:
            position[0] -= steps

    return abs(position[0]) + abs(position[1])


def part2(puzzle):
    directions = puzzle.split(", ")

    positions = [[0, 0]]
    position = [0,0]
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
        if facing == 1:
            position[1] += steps
        elif facing == 2:
            position[0] += steps
        elif facing == 3:
            position[1] -= steps
        elif facing == 4:
            position[0] -= steps

        # check
        # fixme use all intermediate positions as well
        if position in positions:
            return abs(position[0]) + abs(position[1])
        else:
            positions.append(position[:])


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
