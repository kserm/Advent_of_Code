import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        data.append([c for c in line.strip()])

cur_pos = (0, 0)
cur_dir = (-1, 0)
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            cur_pos = (y, x)

cursor = '^'

visited = set()
visited.add(cur_pos)

max_y = len(data) - 1
max_x = len(data[0]) - 1

def guard_move() -> bool:
    global cur_dir, cur_pos, cursor
    y, x = cur_pos
    dy, dx = cur_dir
    ny, nx = y+dy, x+dx
    if ((max_y < ny) or (ny < 0)) or ((max_x < nx) or (nx < 0)):
        return False
    if (data[ny][nx] == '#'):
        if cur_dir == (-1, 0):
            cur_dir = (0, 1)
        elif cur_dir == (0, 1):
            cur_dir = (1, 0)
        elif cur_dir == (1, 0):
            cur_dir = (0, -1)
        elif cur_dir == (0, -1):
            cur_dir = (-1, 0)
        return True
    else:
        if (0 <= y+dy <= max_y) and (0 <= x+dx <= max_x):
            cur_pos = (y+dy, x+dx)
            visited.add(cur_pos)
            return True
        

while guard_move():
    pass

print(len(visited))
    