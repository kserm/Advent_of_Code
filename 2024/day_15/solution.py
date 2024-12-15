import os

walls = set()
boxes = []
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
            elif c == "O":
                boxes.append((y, x))
            elif c == "@":
                start = y, x
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

def find_nearest_wall(pos: tuple, direction: tuple) -> tuple:
    inc_y, inc_x = direction
    y, x = pos
    while True:
        y += inc_y
        x += inc_x
        if (y, x) in walls:
            return y, x

def is_box_adjacent(position: tuple, direction: tuple) -> bool:
    y, x = position
    dy, dx = direction
    next_pos = y + dy, x +dx
    if next_pos in boxes:
        return True
    return False

def is_move_allowed(position: tuple, direction: tuple) -> bool:
    y, x = position
    dy, dx = direction
    ny, nx = y + dy, x + dx
    if (ny, nx) not in walls:
        return True
    return False

def move_boxes(position: tuple, direction: tuple) -> bool:
    boxes_to_move = []
    indx = boxes.index(position)
    is_allowed = is_move_allowed(position, direction)
    if not is_allowed:
        return False
    boxes_to_move.append([indx, position])
    while is_box_adjacent(position, direction) and is_allowed:
        y, x = position
        dy, dx = direction
        next_pos = y + dy, x + dx
        is_allowed = is_move_allowed(next_pos, direction)
        indx = boxes.index(next_pos)
        boxes_to_move.append([indx, next_pos])
        position = next_pos
    if is_allowed:
        for item in boxes_to_move:
            i = item[0]
            y, x = item[1]
            dy, dx = direction
            new_pos = y + dy, x + dx
            boxes[i] = new_pos
        return True

robot = start
for move in movements:
    ys, xs = robot
    dy, dx = move
    ny, nx = ys + dy, xs + dx
    if (ny, nx) in walls:
        pass
    elif (ny, nx) in boxes:
        mb = move_boxes((ny, nx), move)
        if mb:
            robot = (ny, nx)
    else:
        robot = (ny, nx)

# for y in range(max_y):
#     for x in range(max_x):
#         if (y, x) in walls:
#             print("#", end="")
#         elif (y, x) in boxes:
#             print("O", end="")
#         else:
#             print(".", end="")
#     print()

total = 0
for box in boxes:
    y, x = box
    total += (y * 100) + x

print(total)

