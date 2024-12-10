import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        data.append([int(c) for c in line.strip()])

max_y = len(data) -1
max_x = len(data[0]) - 1

def check_next(position: tuple, dy: int, dx: int) -> bool:
    y, x = position
    height = data[y][x]
    ny, nx = y+dy, x+dx
    if (0 <= ny <= max_y) and (0 <= nx <= max_x):
        new_height = data[ny][nx]
        dh = new_height - height
        if (dh == 1):
            return True
    return False
    
total = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        pos = y, x
        if data[y][x] == 0:
            scores = 0
            routes = [[[], pos, True, set()]]
            routes[0][0].append(pos)
            for i in range(1, 10):
                for route in routes:
                    is_active = route[2]
                    if is_active == False:
                        continue
                    else:
                        route[2] = False
                        visited = route[0]
                        last = route[1]
                        heights = route[3]
                        if check_next(last, 1, 0):
                            new_pos = last[0] + 1, last[1]
                            ny, nx = new_pos
                            height = data[ny][nx]
                            new_visited = visited.copy()
                            if (new_pos not in new_visited) and (new_pos != last) and (new_pos not in heights):
                                if height == 9:
                                    heights.add(new_pos)
                                new_visited.append(new_pos)
                                routes.append([new_visited, new_pos, True, heights])
                        if check_next(last, -1, 0):
                            new_pos = last[0] - 1, last[1]
                            ny, nx = new_pos
                            height = data[ny][nx]
                            new_visited = visited.copy()
                            if (new_pos not in new_visited) and (new_pos != last) and (new_pos not in heights):
                                if height == 9:
                                    heights.add(new_pos)
                                new_visited.append(new_pos)
                                routes.append([new_visited, new_pos, True, heights])
                        if check_next(last, 0, 1):
                            new_pos = last[0], last[1] + 1
                            ny, nx = new_pos
                            height = data[ny][nx]
                            new_visited = visited.copy()
                            if (new_pos not in new_visited) and (new_pos != last) and (new_pos not in heights):
                                if height == 9:
                                    heights.add(new_pos)
                                new_visited.append(new_pos)
                                routes.append([new_visited, new_pos, True, heights])
                        if check_next(last, 0, -1):
                            new_pos = last[0], last[1] - 1
                            ny, nx = new_pos
                            height = data[ny][nx]
                            new_visited = visited.copy()
                            if (new_pos not in new_visited) and (new_pos != last) and (new_pos not in heights):
                                if height == 9:
                                    heights.add(new_pos)
                                new_visited.append(new_pos)
                                routes.append([new_visited, new_pos, True, heights])
            for route in routes:
                if len(route[0]) == 10:
                    scores += 1
            total += scores
print(total)
