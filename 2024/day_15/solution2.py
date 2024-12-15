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

def is_box_adjacent(position: tuple, direction: tuple) -> bool:
    pass

def is_move_allowed(position: tuple, direction: tuple) -> bool:
    pass

def move_boxes(position: tuple, direction: tuple) -> bool:
    pass

draw_map(start)

total = 0

print(total)

