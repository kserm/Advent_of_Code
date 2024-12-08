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

antinodes = set()

for key, item in data.items():
    for i in range(len(item)):
        point = item[i]
        for j in range(len(item)):
            if i != j:
                another_point = item[j]
                dy = point[0] - another_point[0]
                dx = point[1] - another_point[1]
                y, x = point[0], point[1]
                new_y, new_x = y + dy, x + dx
                while (0 <= new_y < max_y) and (0 <= new_x < max_x):
                    antinodes.add((new_y, new_x))
                    new_y, new_x = new_y + dy, new_x + dx
                y, x = another_point[0], another_point[1]
                new_y, new_x = y - dy, x - dx
                while (0 <= new_y < max_y) and (0 <= new_x < max_x):
                    antinodes.add((new_y, new_x))
                    new_y, new_x = new_y - dy, new_x - dx

for item in data.values():
    for i in item:
        antinodes.add(i)

print(len(antinodes))
