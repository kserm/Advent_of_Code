import os
from collections import deque

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        data.append(list(line.strip()))

max_y = len(data) - 1
max_x = len(data[0]) - 1

def out_of_bounds(y, x: int) -> bool:
    if (y < 0) or (y > max_y) or (x < 0) or (x > max_x):
        return True
    return False

def check_up(current_plant: str, y, x: int) -> bool:
    ny, nx = y-1, x
    if out_of_bounds(ny, nx):
        return False
    if data[ny][nx] == current_plant:
        return True
    return False

def check_down(current_plant: str, y, x: int) -> bool:
    ny, nx = y+1, x
    if out_of_bounds(ny, nx):
        return False
    if data[ny][nx] == current_plant:
        return True
    return False

def check_left(current_plant: str, y, x: int) -> bool:
    ny, nx = y, x-1
    if out_of_bounds(ny, nx):
        return False
    if data[ny][nx] == current_plant:
        return True
    return False

def check_right(current_plant: str, y, x: int) -> bool:
    ny, nx = y, x+1
    if out_of_bounds(ny, nx):
        return False
    if data[ny][nx] == current_plant:
        return True
    return False

def is_in_group(positions: list[list], y, x: int) -> int:
    index = -1
    for i in range(len(positions)):
        position_list = positions[i]
        for position in position_list:
            a, b = position
            if ((abs(a-y)==1) and ((b-x)==0)) or (((a-y)==0) and (abs(b-x)==1)):
                index = i
                break
    return index

garden_plots = {}
for y in range(max_y+1):
    for x in range(max_x+1):
        plot = data[y][x]
        if plot not in garden_plots:
            garden_plots[plot] = [(y, x)]
        else:
            garden_plots[plot].append((y, x))

def is_adjacent(coord1, coord2: tuple) -> bool:
    y1, x1 = coord1
    y2, x2 = coord2
    return (abs(y1 - y2) == 1 and x1 == x2) or (y1 == y2 and abs(x1 - x2) == 1)

def find_adjacent(positions):
    positions_set = set(positions)
    groups = []

    while positions_set:
        current_group = []
        queue = deque([positions_set.pop()])

        while queue:
            coord = queue.popleft()
            current_group.append(coord)

            neighbors = [(coord[0] + dy, coord[1] + dx) for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
            for neighbor in neighbors:
                if neighbor in positions_set:
                    queue.append(neighbor)
                    positions_set.remove(neighbor)
        groups.append(sorted(current_group))
    return groups

total = 0
for key, value in garden_plots.items():
    f = find_adjacent(value)
    for i in f:
        per = 0
        area = len(i)
        for j in i:
            y, x = j
            name = data[y][x]
            if not check_up(name, y, x):
                per += 1
            if not check_down(name, y, x):
                per += 1
            if not check_left(name, y, x):
                per += 1
            if not check_right(name, y, x):
                per += 1
        total += area * per

print(total)          
            