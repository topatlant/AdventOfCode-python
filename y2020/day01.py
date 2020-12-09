import itertools

data = open("input_day01.txt").readlines()
data = [int(d) for d in data]

# part 1
for x, y in itertools.combinations(data, 2):
    if x + y == 2020:
        print(f"{x} * {y} = {x * y}")
        break

# part 2
for x, y, z in itertools.combinations(data, 3):
    if x + y + z == 2020:
        print(f"{x} * {y} * {z} = {x * y * z}")
        break
