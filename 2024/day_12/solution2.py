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

data = test_data

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

def split_list(l: list) -> list:
    res = []
    indxs = []
    for i in range(len(l)-1):
        a, b = l[i], l[i+1]
        if abs(b-a) > 1:
            indxs.append(i+1)
    if indxs:
        last = 0
        for j in indxs:
            last = j
            res.append(l[:last])
        res.append(l[last:])
        return res
    else:
        return [l]

def list_for_dict(l: list) -> list:
    res = []
    if len(l) == 1:
        res = [l[0], l[0]]
    else:
        res = [l[0], l[-1]]
    return res

def get_sides(a, b: int, l: list) -> dict:
    res = {}
    tmp = {}
    srt_l = sorted(l)
    for i in srt_l:
        if i[a] in res:
            res[i[a]].append(i[b])
        else:
            res[i[a]] = [i[b]]
    for k in res:
        if len(res[k]) == 1:
            tmp[k] = [[res[k][0], res[k][0]]]
        else:
            tmp_lst = split_list(res[k])
            if len(tmp_lst) == 1:
                if k in tmp:
                    tmp[k].append(list_for_dict(tmp_lst[0]))
                else:
                    tmp[k] = [list_for_dict(tmp_lst[0])]
            else:
                for item in tmp_lst:
                    if k in tmp:
                        tmp[k].append(list_for_dict(item))
                    else:
                        tmp[k] = [list_for_dict(item)]
    res = tmp
    return res

total = 0
for key, value in garden_plots.items():
    f = find_adjacent(value)
    for i in f:
        blocks = 0
        area = len(i)
        print(key, i)
        hor = get_sides(0, 1, i)
        vert = get_sides(1, 0, i)
        print(hor)
        for k, v in hor.items():
            for h in v:
                if (not check_up(key, k, h[0])) or (not check_up(key, k, h[1])):
                    blocks += 1
                    print(k, h, check_up(key, k, h[0]), check_up(key, k, h[1]), blocks)
                if (not check_down(key, k, h[0])) or (not check_down(key, k, h[1])):
                    blocks += 1
                    print(k, h, check_down(key, k, h[0]), check_down(key, k, h[1]), blocks)
        print(vert)
        for k, v in vert.items():
            for vrt in v:
                if (not check_left(key, vrt[0], k)) or (not check_left(key, vrt[1], k)):
                    blocks += 1
                    print(k, h, check_left(key, vrt[0], k), check_left(key, vrt[1], k), blocks)
                if (not check_right(key, vrt[0], k)) or (not check_right(key, vrt[1], k)):
                    blocks += 1
                    print(k, h, check_right(key, vrt[0], k), check_right(key, vrt[1], k), blocks)
        print(area, blocks)
        print(40*"###")
        total += area * blocks

print(total)          
            