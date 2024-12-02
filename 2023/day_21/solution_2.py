from math import sqrt
data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

tst_str = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

# data = [list(i) for i in tst_str.strip().split('\n')]
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            start = [(y, x)]
            data[y][x] = '.'


# counter = 0
# for y in range(len(data)):
#     for x in range(len(data[y])):
#         if data[y][x] == '.':
#             counter += 1

DIRECTIONS = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
]

def move(position: tuple) -> list:
    res = []
    y, x = position
    for d in DIRECTIONS:
        a = y + d[0]
        b = x + d[1]
        if data[a][b] == '.':
            res.append((a, b))
    return res

steps = 6
# steps = 26501365

for i in range(steps):
    new_pos = []
    for item in start:
        positions = move(item)
        for p in positions:
            if p not in new_pos:
                new_pos.append(p)
    start = new_pos

# print(len(start))
print(3703 * 65 * 131)