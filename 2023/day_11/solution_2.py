from itertools import combinations
import numpy as np

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

np_data = np.array(data)
n = 1000000

galaxies = set()
empty_rows = set()
empty_cols = set()
rows = np_data.shape[0]
cols = np_data.shape[1]

for r in range(rows):
    row = np_data[r, :]
    if all([i == '.' for i in row]):
        empty_rows.add(r)

for c in range(cols):
    col = np_data[:, c]
    if all([i == '.' for i in col]):
        empty_cols.add(c)

empty_rows = sorted(list(empty_rows))
empty_cols = sorted(list(empty_cols))

for r in range(rows):
    for c in range(cols):
        if np_data[r,c] == '#':
            galaxies.add((r,c))

def find_offs(num: int, e_list: list) -> int:
    empty_spaces = []
    for i in e_list:
        if num > i:
            empty_spaces.append(i)
    t = len(empty_spaces)
    res = num + t*(n - 1)
    return res

galaxies_combinations = list(combinations(galaxies, 2))
total = 0
for g in galaxies_combinations:
    y_1, x_1 = g[0][0], g[0][1]
    y_2, x_2 = g[1][0], g[1][1]
    y_1 = find_offs(y_1, empty_rows)
    y_2 = find_offs(y_2, empty_rows)
    x_1 = find_offs(x_1, empty_cols)
    x_2 = find_offs(x_2, empty_cols)
    v = abs(y_1 - y_2)
    h = abs(x_1 - x_2)
    sum = v + h
    total += sum

print(total)
