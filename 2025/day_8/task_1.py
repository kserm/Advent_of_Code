import os
from itertools import combinations
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
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
    pairs = [(tuple(a), tuple(b)) for _, (a, b) in sorted_dists]

    parents = {}

    def make_set(x, parent):
        parent[x] = x

    def find(x, parent):
        if parent[x] != x:
            parent[x] = find(parent[x], parent)
        return parent[x]

    def union(x, y, parent):
        root_x = find(x, parent)
        root_y = find(y, parent)
        if root_x != root_y:
            parent[root_y] = root_x

    limit = 1000
    for a, b in pairs[:limit]:
        if a not in parents:
            make_set(a, parents)
        if b not in parents:
            make_set(b, parents)
        union(a, b, parents)

    groups = defaultdict(list)
    for point in parents:
        root = find(point, parents)
        groups[root].append(point)

    total = 1
    res = []
    for k, v in groups.items():
        res.append(len(v))
    res = sorted(res)
    for r in res[len(res) - 3 :]:
        total *= r
    print(total)
