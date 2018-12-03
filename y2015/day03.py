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


def part1(puzzle):
    x = 0
    y = 0
    visited = [(0, 0)]
    for letter in puzzle:
        x, y = move(x, y, letter)
        visited.append((x, y))

    result = len(set(visited))
    return result


def part2(puzzle):
    x = 0
    y = 0
    visited = [(0, 0)]
    # Santa
    for letter in puzzle[::2]:
        x, y = move(x, y, letter)
        visited.append((x, y))

    # Robo Santa
    x = 0
    y = 0
    for letter in puzzle[1::2]:
        x, y = move(x, y, letter)
        visited.append((x, y))

    result = len(set(visited))
    return result


if __name__ == "__main__":
    print("Part 1:", part1(get_input()))
    print("Part 2:", part2(get_input()))
