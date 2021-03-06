def get_input():
    return open("input_day03.txt").read()


def move(x, y, letter):
    if letter == "<":
        x -= 1
    elif letter == ">":
        x += 1
    elif letter == "^":
        y += 1
    elif letter == "v":
        y -= 1
    else:
        raise Exception("unknown direction")

    return x, y


def get_visited_spots(directions):
    x = 0
    y = 0
    visited = [(0, 0)]
    for letter in directions:
        x, y = move(x, y, letter)
        visited.append((x, y))
    return visited


def part1(puzzle):
    return len(set(get_visited_spots(puzzle)))


def part2(puzzle):
    santa = get_visited_spots(puzzle[::2])
    robo_santa = get_visited_spots(puzzle[1::2])

    return len(set(santa + robo_santa))


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
