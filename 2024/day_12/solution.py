import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        data.append(list(line.strip()))

test_str = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

test_data = []
for l in test_str.strip().split("\n"):
    test_data.append(list(l.strip()))

# data = test_data

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


def is_adjacent(position: tuple, positions: list) -> bool:
    y1, x1 = position
    for p in positions:
        y2, x2 = p
        if ((abs(y2-y1)==1) and (abs(x2-x1)==0)) or ((abs(y2-y1)==0) and (abs(x2-x1)==1)):
            return True
    return False


processed = set()
# TODO: optimize this
def find_adjacent(positions: list) -> list:
    res = []
    max_counts = len(positions) - 1
    for i in positions:
        if i in processed:
            continue
        flag = True
        counter = 0
        res.append([])
        res[-1].append(i)
        processed.add(i)
        while flag:
            if counter > 20*max_counts:
                flag = False
            for j in positions:
                if (is_adjacent(j, res[-1])) and (j not in processed):
                    res[-1].append(j)
                    processed.add(j)
                else:
                    counter += 1
    return res

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
            