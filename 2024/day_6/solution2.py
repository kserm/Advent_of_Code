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

start = cur_pos
start_dir = cur_dir

max_y = len(data) - 1
max_x = len(data[0]) - 1

loops = 0

def guard_move(visited: set) -> bool:
    global cur_dir, cur_pos, loops
    y, x = cur_pos
    dy, dx = cur_dir
    ny, nx = y+dy, x+dx
    if ((max_y < ny) or (ny < 0)) or ((max_x < nx) or (nx < 0)):
        return False
    if (data[ny][nx] == '#') or (data[ny][nx] == 'O'):
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
        if ((ny >= 0) and (ny <= max_y)) and ((nx >= 0) and (nx <= max_x)):
            cur_pos = (ny, nx)
            entry = cur_pos, cur_dir
            if entry in visited:
                loops += 1
                return False
            else:
                visited.add(entry)
                return True

for y in range(max_y+1):
    for x in range(max_x+1):
        vis = set()
        stored_value = data[y][x]
        if stored_value == '.':
            data[y][x] = 'O'
            while guard_move(vis):
                pass
        data[y][x] = stored_value
        cur_pos = start
        cur_dir = start_dir

print(loops)            
    