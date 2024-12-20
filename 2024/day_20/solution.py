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

def scan_shortcuts(position: tuple) -> list:
    res = []
    y, x = position
    moves = [((y + dy, x + dx), (y + 2*dy, x + 2*dx)) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for move in moves:
        if move[0] in walls and move[1] in spt:
            d1 = spt[position][1]
            d2 = spt[move[1]][1]
            cheat = d2 - d1 - 2
            if cheat > 0:
                res.append(cheat)
    return res

total = {}
for pos in spt:
    shortcuts = scan_shortcuts(pos)
    for s in shortcuts:
        if s in total:
            total[s] += 1
        else:
            total[s] = 1

result = 0
for s in total:
    if s >= 100:
        result += total[s]

print(result)