import os
from itertools import combinations

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input1.txt", "r") as file:
    lines = file.readlines()
    coordinates = []
    for line in lines:
        coordinates.append([int(n) for n in line.strip().split(",")])

    dist = []
    comb = combinations(coordinates, 2)
    for c in comb:
        x, y, z = c[0]
        nx, ny, nz = c[1]
        dx = nx - x
        dy = ny - y
        dz = nz - z
        d = (dx * dx) + (dy * dy) + (dz * dz)
        dist.append((d, c))
    sorted_dists = sorted(dist)
    for d in sorted_dists[:10]:
        print(d)
