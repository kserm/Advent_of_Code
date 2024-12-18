import os

walls = []
start = (0, 0)
end = (70, 70)
max_y = 70
max_x = 70

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        walls.append(tuple(int(x) for x in line.strip().split(",")))

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

def in_boundaries(position: tuple) -> bool:
    x, y = position
    if (0 <= x <= max_x) and (0 <= y <= max_y):
        return True
    return False

def get_moves(position: tuple, walls_list: list) -> list:
    res = []
    x, y = position
    moves = [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls_list) and in_boundaries(m):
            res.append(m)
    return res

def check_neighbors(position: tuple, path_tree: dict, walls_list: list) -> bool:
    neighbors = get_moves(position, walls_list)
    for n in neighbors:
        if n not in path_tree:
            return False
    return True

def get_shortest_path_tree(walls_list: list) -> tuple:
    visited = set()
    spt = {}
    spt[start] = [start, 0]

    v = 0
    while v < len(spt):
        v = 0
        for position in spt.copy():
            if position in visited:
                v += 1
            distance = spt[position][1]
            if position not in visited:
                moves = get_moves(position, walls_list)
                for move in moves:
                    new_d = distance + 1
                    if move in spt:
                        old_d = spt[move][1]
                        if new_d < old_d:
                            spt[move][0] = position
                            spt[move][1] = new_d
                    else:
                        spt[move] = [position, new_d]
            if check_neighbors(position, spt, walls_list):
                visited.add(position)
    if end in spt:
        return (True, spt)
    else:
        return (False, spt)

for i in range(len(walls)-1, 1024, -1):
    wl = set(walls[:i])
    x = get_shortest_path_tree(wl)
    if x[0]:
        print(walls[i])
        break
