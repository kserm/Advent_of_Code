import numpy as np

data = []

tst_str = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

# data = [list(l) for l in tst_str.strip().split('\n')]

np_data = np.array(data)

rows = np_data.shape[0]
cols = np_data.shape[1]

line = np_data[:, 0]

def tilt_col(line):
    b = 0
    for i in range(len(line)):
        if i >= b:
            if line[i] == '.':
                for j in range(i+1, len(line)):
                    if line[j] == '#':
                        b = j + 1
                        break
                    if line[j] == 'O':
                        line[b] = 'O'
                        line[j] = '.'
                        b += 1
                        break
            else:
                b += 1

def tilt_table(table):
    cols = table.shape[1]
    for col in range(cols):
        tilt_col(table[:, col])

def cycle(table):
    for _ in range(4):
        tilt_table(table)
        # table = table.T
        table = np.rot90(table, k=-1)

tilt_table(np_data)

print(np_data)

def count_total(table):
    rows = table.shape[0]
    cols = table.shape[1]
    round_rocks = []
    for r in range(rows):
        for c in range(cols):
            if np_data[r,c] == 'O':
                round_rocks.append((r, c))
    total = 0
    rng = rows               
    for i in range(rng):
        m = rng - i
        count = 0
        for item in round_rocks:
            if item[0] == i:
                count += 1
        total += m * count

    return total
print(count_total(np_data))
print(20*' * ')
cycles = 1000
# cycles = 1000000000
for _ in range(cycles):
    print(_)
    cycle(np_data)
print(count_total(np_data))
