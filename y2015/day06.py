def get_input():
    return open("input_day06.txt").read()


def get_iterator(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            yield i, j


def turn_on(it):
    for (i, j) in it:
        lights1[i][j] = True
        lights2[i][j] += 1


def turn_off(it):
    for (i, j) in it:
        lights1[i][j] = False

        lights2[i][j] -= 1
        if lights2[i][j] < 0:
            lights2[i][j] = 0


def toggle(it):
    for (i, j) in it:
        lights1[i][j] ^= True
        lights2[i][j] += 2


# main calculation
lights1 = []
for i in range(1000):
    lights1.append([False] * 1000)
lights2 = []
for i in range(1000):
    lights2.append([0] * 1000)

for task in get_input().splitlines():
    q, w = task.split("through")
    x1, y1 = map(int, q.strip().split(" ")[-1].split(","))
    x2, y2 = map(int, w.strip().split(","))
    it = get_iterator(x1, y1, x2, y2)
    if task.startswith("turn on"):
        turn_on(it)
    elif task.startswith("turn off"):
        turn_off(it)
    elif task.startswith("toggle"):
        toggle(it)


def part1():
    return sum(line.count(True) for line in lights1)


def part2():
    return sum(sum(line) for line in lights2)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
