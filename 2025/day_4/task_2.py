import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def check_postition(data, y, x, my, mx):
    counter = 0
    positions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
    for p in positions:
        ny, nx = p[0] + y, p[1] + x
        if (0 <= ny < my) and (0 <= nx < mx):
            if data[ny][nx] == "@":
                counter += 1
    return counter


with open(f"{dir_path}/input.txt", "r") as file:
    rolls = [list(line.strip()) for line in file.readlines()]
    max_y, max_x = len(rolls), len(rolls[0])
    flag = True
    total = 0
    while True:
        res = set()
        for y in range(max_y):
            for x in range(max_x):
                if rolls[y][x] == "@":
                    r = check_postition(rolls, y, x, max_y, max_x)
                    if r < 4:
                        res.add((y, x))
                        rolls[y][x] = "."
        if len(res) == 0:
            break
        total += len(res)
    print(total)
