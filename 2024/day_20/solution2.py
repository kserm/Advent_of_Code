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
    d1 = spt[pos1][1]
    d2 = spt[pos2][1]
    delta_d = d2 - d1
    y1, x1 = pos1
    y2, x2 = pos2
    cheat = abs(x2- x1) + abs(y2 - y1)
    return delta_d - cheat 

total = {}
for pos1 in spt:
    for pos2 in spt:
        if pos1 != pos2:
            y1, x1 = pos1
            y2, x2 = pos2
            md = (abs(x2 - x1) + abs(y2 - y1))
            if md <= 20:
                cc = calc_cheat(pos1, pos2)
                if cc in total:
                    total[cc] += 1
                else:
                    total[cc] = 1

result = 0
for s in sorted(total):
    if s >= 100:
        result += total[s]

print(result)
