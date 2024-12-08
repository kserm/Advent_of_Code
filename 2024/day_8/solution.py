import os

data = {}

dir_path = os.path.dirname(os.path.realpath(__file__))

max_y = 0
max_x = 0

with open(f'{dir_path}/input.txt', 'r') as file:
    lst = file.read().split('\n')
    max_y = len(lst)
    max_x = len(lst[0])
    for y in range(max_y):
        for x in range(len(lst[y])):
            if lst[y][x] != '.':
                if lst[y][x] in data:
                    data[lst[y][x]].append((y, x))
                else:
                    data[lst[y][x]] = [(y, x)]

antinodes = {}

for key, item in data.items():
    antinodes[key] = set()
    for i in range(len(item)):
        point = item[i]
        for j in range(len(item)):
            if i != j:
                another_point = item[j]
                dy = point[0] - another_point[0]
                dx = point[1] - another_point[1]
                antinode_1 = (point[0] + dy, point[1] + dx)
                antinode_2 = (another_point[0] - dy, another_point[1] - dx)
                if (0 <= antinode_1[0] < max_y) and (0 <= antinode_1[1] < max_x):
                    antinodes[key].add(antinode_1)
                if (0 <= antinode_2[0] < max_y) and (0 <= antinode_2[1] < max_x):
                    antinodes[key].add(antinode_2)

uniques = set()
for item in antinodes.values():
    for i in item:
        uniques.add(i)

print(len(uniques))
