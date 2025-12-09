import os
from itertools import combinations

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    positions = []
    red_tiles = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for line in lines:
        x, y = tuple(int(i) for i in line.strip().split(","))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        red_tiles.append((x, y))
    max_x += 1
    max_y += 1

    def calc_area(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        a = abs(x2 - x1) + 1
        b = abs(y2 - y1) + 1
        return a * b

    max_area = 0

    rtc = combinations(red_tiles, 2)
    for c in rtc:
        p1, p2 = c
        area = calc_area(p1, p2)
        max_area = max(max_area, area)

    print(max_area)