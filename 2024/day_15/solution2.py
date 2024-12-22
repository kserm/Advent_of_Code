import os

walls = set()
boxes_ls = []
boxes_rs = []
movements = []
start = (-1, -1)
max_y = 0
max_x = 0

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    data = file.read().strip().split("\n\n")
    y = 0
    for line in data[0].strip().split("\n"):
        x = 0
        for c in line.strip():
            if c == "#":
                walls.add((y, x))
                x += 1
                walls.add((y, x))
            elif c == "O":
                boxes_ls.append((y, x))
                x += 1
                boxes_rs.append((y, x))
            elif c == "@":
                start = y, x
                x += 1
            else:
                x += 1
            x += 1
        y += 1
    max_y, max_x = y, x
    for line in data[1].strip().split("\n"):
        for c in line.strip():
            if c == "^":
                movements.append((-1, 0))
            elif c == "v":
                movements.append((1, 0))
            elif c == ">":
                movements.append((0, 1))
            elif c == "<":
                movements.append((0, -1))

def draw_map(robot):
    for y in range(max_y):
        for x in range(max_x):
            if (y, x) in walls:
                print("#", end="")
            elif (y, x) in boxes_ls:
                print("[", end="")
            elif (y, x) in boxes_rs:
                print("]", end="")
            elif (y, x) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()

def get_adjacent_boxes(position: tuple, direction: tuple) -> list:
    indexes = []
    dy, dx = direction
    y, x = position
    ny, nx = y + dy, x + dx
    if dy in [-1, 1] and dx == 0:
        if (ny, nx) in boxes_ls:
            indexes.append(boxes_ls.index((ny, nx)))
        if (ny, nx) in boxes_rs:
            indexes.append(boxes_rs.index((ny, nx)))
        if indexes:
            to_check = indexes.copy()
            flag = True
            while to_check:
                i = to_check.pop(0)
                y1, x1 = boxes_ls[i]
                y2, x2 = boxes_rs[i]
                ny1, nx1 = y1 + dy, x1 + dx
                ny2, nx2 = y2 + dy, x2 + dx
                if (ny1, nx1) in boxes_ls:
                    j = boxes_ls.index((ny1, nx1))
                    if j not in indexes:
                        indexes.append(j)
                        to_check.append(j)
                if (ny1, nx1) in boxes_rs:
                    j = boxes_rs.index((ny1, nx1))
                    if j not in indexes:
                        indexes.append(j)
                        to_check.append(j)
                if (ny2, nx2) in boxes_ls:
                    j = boxes_ls.index((ny2, nx2))
                    if j not in indexes:
                        indexes.append(j)
                        to_check.append(j)
                if (ny2, nx2) in boxes_rs:
                    j = boxes_rs.index((ny2, nx2))
                    if j not in indexes:
                        indexes.append(j)
                        to_check.append(j)
    elif dy == 0 and dx == 1:
        flag = True
        while flag:
            if (ny, nx) in boxes_ls:
                indexes.append(boxes_ls.index((ny, nx)))
            else:
                flag = False
            ny, nx = ny, nx + 2*dx
    elif dy == 0 and dx == -1:
        flag = True
        while flag:
            if (ny, nx) in boxes_rs:
                indexes.append(boxes_rs.index((ny, nx)))
            else:
                flag = False
            ny, nx = ny, nx + 2*dx
    return indexes

def is_move_allowed(indexes: list, direction: tuple) -> bool:
    dy, dx = direction
    for i in indexes:
        y1, x1 = boxes_ls[i]
        y2, x2 = boxes_rs[i]
        ny1, nx1 = y1 + dy, x1 + dx
        ny2, nx2 = y2 + dy, x2 + dx
        if ((ny1, nx1) in walls) or ((ny2, nx2) in walls):
            return False
    return True

def move_boxes(indexes: list, direction: tuple):
    dy, dx = direction
    for i in indexes:
        y1, x1 = boxes_ls[i]
        y2, x2 = boxes_rs[i]
        npl = y1 + dy, x1 + dx
        npr = y2 + dy, x2 + dx
        boxes_ls[i] = npl
        boxes_rs[i] = npr

robot = start
for move in movements:
    ys, xs = robot
    dy, dx = move
    ny, nx = ys + dy, xs + dx
    if (ny, nx) in walls:
        continue
    indxs = get_adjacent_boxes(robot, move)
    if indxs:
        if is_move_allowed(indxs, move):
            move_boxes(indxs, move)
            robot = ny, nx
    else:
        robot = ny, nx

draw_map(robot)

total = 0
for box in boxes_ls:
    y, x = box
    total += (y * 100) + x

print(total)
