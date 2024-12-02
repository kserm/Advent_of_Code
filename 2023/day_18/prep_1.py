# Inner area: 48020794727661
# Perimeter:  148344825
# Total area: 48020868900074

data = []

with open('input.txt') as file:
    for line in file.readlines():
        data.append(line.split())

tst_str = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

# data = [l.split() for l in tst_str.strip().split('\n')]
# print(data)

coordinates = []
y = 0
x = 0
for item in data:
    direction = item[0]
    steps = int(item[1])
    if direction == 'L':
        for i in range(steps):
            coordinates.append((y, x))
            x -= 1
        # x -= steps
    elif direction == 'R':
        for i in range(steps):
            coordinates.append((y, x))
            x += 1
        # x += steps
    elif direction == 'U':
        for i in range(steps):
            coordinates.append((y, x))
            y -= 1
        # y -= steps
    elif direction == 'D':
        for i in range(steps):
            coordinates.append((y, x))
            y += 1
        # y += steps

y_min = 0
x_min = 0

for item in coordinates:
    y = item[0]
    x = item[1]
    y_min = min(y_min, y)
    x_min = min(x_min, x)

y_max = 0
x_max = 0
new_coordinates = []
for item in coordinates:
    new_y = item[0] - y_min
    new_x = item[1] - x_min
    y_max = max(y_max, new_y)
    x_max = max(x_max, new_x)
    new_coordinates.append((new_y, new_x))

# print(y_max, x_max)
list_for_str = []
for y in range(y_max+1):
    line = []
    for x in range(x_max+1):
        if (y, x) in new_coordinates:
            line.append('#')
        else:
            line.append('.')
    list_for_str.append(line)

data_str = '\n'.join([''.join(c) for c in list_for_str])

with open('output.txt', 'w') as file:
    file.write(data_str)
# print(y_min, x_min)
    # print(y, x)
    # print(item[0], int(item[1]))
# print(coordinates)
