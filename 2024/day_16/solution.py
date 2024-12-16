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

def deer_move(position: tuple, visited: set) -> list:
    res = []
    y, x = position[0]
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls) and (m not in visited):
            res.append(m)
    return res

def count_points(position: tuple, next_direction: tuple, total: int) -> int:
    direction = position[1]
    if direction == next_direction:
        total += 1
        return total
    else:
        total += 1001
        return total

routes = []
routes.append([start, 0, set()])
route = routes.pop()
pos = route[0]
total = route[1]
vis = route[2]
dm = deer_move(pos, vis)
for move in dm:
    vis.add(pos[0])
    routes.append([pos, total, vis])

results = []

shortest_paths = set()
shortest_paths.add((start[0], 0))

def find_routes(routes: list) -> list:
    res = []
    for route in routes:
        pos = route[0]
        total = route[1]
        vis = route[2]
        for path in shortest_paths.copy():
            if pos[0] in path:
                p = min(total, path[1])
                break
            else:
                p = total
                shortest_paths.add((pos[0], total))
        if p < total:
            continue
        if results and total > min(results):
            continue
        dm = deer_move(pos, vis)
        if end in vis:
            results.append(total)
            continue
        if dm:
            for move in dm:
                ny, nx = move
                y, x = pos[0]
                nd = ny - y, nx - x
                t = count_points(pos, nd, total)
                next_pos = (move, nd)
                v = vis.copy()
                v.add(move)
                item = [next_pos, t, v]
                if item not in res:
                    res.append(item)
    return res

while routes:
    routes = find_routes(routes)

if results:
    print(min(results))
