import os

walls = set()
start = ((-1, -1), (0, 1))
end = (-1, -1)
max_y = 0
max_x = 0

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    y = 0
    for line in file.readlines():
        x = 0
        for c in line.strip():
            if c == "#":
                walls.add((y, x))
            elif c == "S":
                start = ((y, x), (0, 1))
            elif c == "E":
                end = (y, x)
            x += 1
        y += 1
    max_y = y
    max_x = x

max_v = max_y * max_x - len(walls)

def deer_moves(position: tuple) -> list:
    res = []
    y, x = position
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls):
            res.append(m)
    return res

def count_points(direction: tuple, next_direction: tuple, total: int) -> int:
    if direction == next_direction:
        total += 1
        return total
    else:
        total += 1001
        return total

visited = set()
spt = {}
spt[start[0]] = [start[0], start[1], 0]

v = 0
while v < len(spt):
    v = 0
    for position in spt.copy():
        direction = spt[position][1]
        distance = spt[position][2]
        if position == end:
            v += 1
            continue
        if (position in visited):
            v += 1
        visited.add(position)
        moves = deer_moves(position)
        if not moves:
            v += 1
        for move in moves:
            y, x = position
            ny, nx = move
            nd = ny - y, nx - x
            t = count_points(direction, nd, distance)
            if move in spt:
                t2 = spt[move][2]
                if t < t2:
                    spt[move][0] = position
                    spt[move][1] = nd
                    spt[move][2] = t
            else:
                spt[move] = [position, nd, t]

print(spt[end][2])
