def get_input():
    return open("inputs/06.txt").read()


def get_square_iterator(x1, y1, x2, y2):
    return ((i, j) for i in range(x1, x2 + 1) for j in range(y1, y2 + 1))


def turn_on(it, lights1, lights2):
    for (i, j) in it:
        lights1[i][j] = True
        lights2[i][j] += 1


def turn_off(it, lights1, lights2):
    for (i, j) in it:
        lights1[i][j] = False

        lights2[i][j] -= 1
        if lights2[i][j] < 0:
            lights2[i][j] = 0


def toggle(it, lights1, lights2):
    for (i, j) in it:
        lights1[i][j] ^= True
        lights2[i][j] += 2


def fill_lights(puzzle):
    # main calculation
    lights1 = [[False] * 1000 for _ in range(1000)]
    lights2 = [[0] * 1000 for _ in range(1000)]

    for task in puzzle.splitlines():
        q, w = task.split("through")
        x1, y1 = map(int, q.strip().split(" ")[-1].split(","))
        x2, y2 = map(int, w.strip().split(","))
        square_iterator = get_square_iterator(x1, y1, x2, y2)

        if task.startswith("turn on"):
            turn_on(square_iterator, lights1, lights2)
        elif task.startswith("turn off"):
            turn_off(square_iterator, lights1, lights2)
        elif task.startswith("toggle"):
            toggle(square_iterator, lights1, lights2)

    return lights1, lights2


def part1(lights):
    return sum(line.count(True) for line in lights)


def part2(lights):
    return sum(sum(line) for line in lights)


def main_method():
    l1, l2 = fill_lights(get_input())
    print("Part 1:", part1(l1))
    print("Part 2:", part2(l2))


if __name__ == "__main__":
    main_method()
