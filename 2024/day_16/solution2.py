import os
from collections import defaultdict, deque

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

visited = set()

def deer_moves(position: tuple, vis: list) -> list:
    res = []
    y, x = position
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls) and (m not in vis):
            res.append(m)
    return res

def count_points(direction: tuple, next_direction: tuple, total: int) -> int:
    if direction == next_direction:
        total += 1
        return total
    else:
        total += 1001
        return total

spt = {}
spt[start[0]] = [start[0], start[1], 0, True]

def get_moves(position: tuple) -> list:
    res = []
    y, x = position
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls):
            res.append(m)
    return res

def check_neighbors(position: tuple) -> bool:
    neighbors = get_moves(position)
    for n in neighbors:
        if n not in spt:
            return False
    return True

while len(visited) < max_v:
    for position in spt.copy():
        if position == end:
            spt[position][3] = False
        active = spt[position][3]
        if active:
            y, x = position
            direction = spt[position][1]
            total = spt[position][2]
            moves = get_moves(position)
            if not moves:
                spt[position][3] = False
                continue
            for move in moves:
                ny, nx = move
                nd = ny - y, nx - x
                t = count_points(direction, nd, total)
                np = [position, nd, t, active]
                if move in spt:
                    old_d = spt[move][2]
                    if t < old_d:
                        spt[move] = np
                else:
                    spt[move] = np
        if check_neighbors(position):
            visited.add(position)
            spt[position][3] = False

visited = set()
routes = []
backtrack = defaultdict(int)
backtrack[start[0]] = 0
first_route = [start[0], start[1], 0, backtrack]
dq = deque()
dq.append(first_route)
ed = spt[end][2]

while dq:
    print(len(visited), "/", max_v)
    position, direction, total, backtrack = dq.popleft()
    if total > 3000 + spt[position][2]:
        continue
    visited.add(position)
    if total > ed:
        continue
    if position == end:
        if total == ed:
            routes.append(backtrack)
        continue
    y, x = position
    moves = deer_moves(position, backtrack)
    if moves:
        for move in moves:
            ny, nx = move
            nd = ny - y, nx - x
            t = count_points(direction, nd, total)
            bt = backtrack.copy()
            bt[move] = t
            new_route = [move, nd, t, bt]
            dq.append(new_route)

print(len(routes))

vp = set()

for route in routes:
    for pos in route:
        vp.add(pos)

print("Answer: ", len(vp))
