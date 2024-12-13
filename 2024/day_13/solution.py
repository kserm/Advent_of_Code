import os
import re

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    blocks = file.read().strip().split("\n\n")
    for block in blocks:
        numbers = re.findall(r"\d+", block)
        data.append([int(n) for n in numbers])

def solve(ax, ay, bx, by, px, py: int) -> list:
    y = (ax*py - ay*px) / (ax*by - ay*bx)
    x = (px - bx * y) / ax
    return [x, y]

tokens = 0

for item in data:
    pt = solve(*item)
    if (pt[0] == int(pt[0])) and (pt[1] == int(pt[1])):
        tokens += 3*int(pt[0]) + int(pt[1])

print(tokens)