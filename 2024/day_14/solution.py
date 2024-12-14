import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    id = 0
    for line in file.readlines():
        position = map(int, line.strip().split()[0].strip("p=").split(","))
        velocity = map(int, line.strip().split()[1].strip("v=").split(","))
        data.append((id, *position, *velocity))
        id += 1

wide = 101
tall = 103
steps = 100
mid_x = wide // 2
mid_y = tall // 2

robots = [0, 0, 0, 0]
for robot in data:
    pos = (robot[1], robot[2])
    vel = (robot[3], robot[4])
    x, y = pos[0], pos[1]
    dx, dy = vel[0], vel[1]
    nx = (x + (steps*dx)) % wide
    ny = (y + (steps*dy)) % tall
    if (0 <= nx < mid_x) and (0 <= ny < mid_y):
        robots[0] += 1
    elif (mid_x < nx < wide) and (0 <= ny < mid_y):
        robots[1] += 1
    elif (0 <= nx < mid_x) and (mid_y < ny < tall):
        robots[2] += 1
    elif (mid_x < nx < wide) and (mid_y < ny < tall):
        robots[3] += 1

total = 1
for r in robots:
    total *= r

print(total)