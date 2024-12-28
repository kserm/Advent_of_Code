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

visited = set()
routes = []
first_route = [start[0], start[1], 0, [start[0]]]
routes.append(first_route)

while len(visited) < max_v:
    print(len(visited), max_v, len(routes))
    for i in range(len(routes)):
        route = routes[i]
        position = route[0]
        direction = route[1]
        total = route[2]
        backtrack = route[3]
        visited.add(position)
        if position == end:
            continue
        moves = deer_moves(position, backtrack)
        if moves:
            if len(moves) >= 2:
                y, x = position
                ny, nx = moves[0]
                nd = ny - y, nx - x
                t = count_points(direction, nd, total)
                bt = backtrack.copy()
                bt.append((ny, nx))
                routes[i] = [(ny, nx), nd, t, bt]
                for move in moves[1:]:
                    y, x = position
                    ny, nx = move
                    nd = ny - y, nx - x
                    t = count_points(direction, nd, total)
                    bt = backtrack.copy()
                    bt.append((ny, nx))
                    routes.append([(ny, nx), nd, t, bt])
            else:
                y, x = position
                ny, nx = moves[0]
                nd = ny - y, nx - x
                t = count_points(direction, nd, total)
                bt = backtrack.copy()
                bt.append((ny, nx))
                routes[i] = [(ny, nx), nd, t, bt]

min_total = 999999
for route in routes:
    if end in route[3]:
        min_total = min(route[2], min_total)
        # print(route)
        # print(40*"###")

print(min_total)
vp = set()

for route in routes:
    if route[2] == min_total:
        for pos in route[3]:
            vp.add(pos)

print(len(vp))
