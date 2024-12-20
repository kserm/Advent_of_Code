import os

walls = set()
start = (-1, -1)
end = (-1, -1)
max_y = -1
max_x = -1

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    y = 0
    for line in file.readlines():
        x = 0
        for c in line.strip():
            if c == "#":
                walls.add((y, x))
            elif c == "S":
                start = (y, x)
            elif c == "E":
                end = (y, x)
            x += 1
        y += 1
    max_y, max_x = y, x

max_v = max_x*max_y - len(walls)

def get_moves(position: tuple) -> list:
    res = []
    y, x = position
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls):
            res.append(m)
    return res

visited = set()

spt = {}
spt[start] = (start, 0)

def check_neighbors(position: tuple) -> bool:
    neighbors = get_moves(position)
    for n in neighbors:
        if n not in spt:
            return False
    return True

while len(visited) < max_v:
    for position in spt.copy():
        if position in visited:
            continue
        else:
            distance = spt[position][1]
            moves = get_moves(position)
            for move in moves:
                new_d = distance + 1
                np = (position, new_d)
                if move in spt:
                    old_d = spt[move][1]
                    if new_d < old_d:
                        spt[move] = np
                else:
                    spt[move] = np
        if check_neighbors(position):
            visited.add(position)

def calc_cheat(pos1, pos2: tuple) -> int:
    if (pos1 in spt) and (pos2 in spt):
        d1 = spt[pos1][1]
        d2 = spt[pos2][1]
        delta_d = d2 - d1
        y1, x1 = pos1
        y2, x2 = pos2
        cheat = abs((abs(y1) - abs(y2)) + (abs(x1) - abs(x2)))
        if cheat < delta_d:
            return delta_d - cheat
    return None

def in_boundaries(pos: tuple) -> bool:
    y, x = pos
    if (0 <= y <= max_y - 1) and (0 <= x <= max_x - 1):
        return True
    return False

def scan_area(pos: tuple, rng: int) -> list:
    preres = []
    for i in range(rng):
        mx = i
        my = rng - mx - 1
        for y in range(my + 1):
            for x in range(mx + 1):
                if (y, x) not in preres:
                    preres.append((y, x))
                if (y, -x) not in preres:
                    preres.append((y, -x))
                if (-y, x) not in preres:
                    preres.append((-y, x))
                if (-y, -x) not in preres:
                    preres.append((-y, -x))
    y1, x1 = pos
    res = []
    for p in preres:
        y2, x2 = p
        np = y2 + y1, x2 + x1
        if in_boundaries(np) and np != pos and np not in walls:
            res.append(np)
    return res

def scan_shortcuts(position: tuple) -> list:
    res = []
    sa = scan_area(position, 20)
    for pos in sa:
        cc = calc_cheat(position, pos)
        if cc:
            res.append(cc)
    return res

# pos = (7, 7)
# sa = scan_area(pos, 20)

# for y in range(max_y):
#     for x in range(max_x):
#         if (y, x) in walls:
#             print("#", end="")
#         elif (y, x) in sa:
#             print("O", end="")
#         else:
#             print(".", end="")
#     print()

total = {}
for pos in spt:
    ss = scan_shortcuts(pos)
    for s in ss:
        if s in total:
            total[s] += 1
        else:
            total[s] = 1

result = 0
for s in total:
    if s >= 100:
        result += total[s]

print(result)