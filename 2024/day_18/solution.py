import os

walls = set()
start = (0, 0)
end = (70, 70)
max_y = 70
max_x = 70

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    i = 0
    for line in file.readlines():
        walls.add(tuple(int(x) for x in line.strip().split(",")))
        if i == 1024:
            break
        i += 1

def in_boundaries(position: tuple) -> bool:
    x, y = position
    if (0 <= x <= max_x) and (0 <= y <= max_y):
        return True
    return False

def get_moves(position: tuple) -> list:
    res = []
    x, y = position
    moves = [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls) and in_boundaries(m):
            res.append(m)
    return res

def draw_map():
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("E", end="")
            elif (x, y) in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()

# draw_map()

visited = set()

spt = {}
spt[start] = [start, 0]

def check_neighbors(position: tuple) -> bool:
    neighbors = get_moves(position)
    for n in neighbors:
        if n not in spt:
            return False
    return True

v = 0
while v < len(spt):
    v = 0
    for position in spt.copy():
        if position in visited:
            v += 1
        distance = spt[position][1]
        if position not in visited:
            moves = get_moves(position)
            for move in moves:
                new_d = distance + 1
                if move in spt:
                    old_d = spt[move][1]
                    if new_d < old_d:
                        spt[move][0] = position
                        spt[move][1] = new_d
                else:
                    spt[move] = [position, new_d]
        if check_neighbors(position):
            visited.add(position)

print(spt[end][1])