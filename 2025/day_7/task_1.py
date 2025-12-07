import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    positions = {}
    beams = set()
    y, x = 0, 0
    max_y = 0
    max_x = 0
    for line in lines:
        max_y = len(lines)
        max_y = len(line)
        for c in line:
            if positions.get(c):
                positions[c].append((y, x))
            else:
                positions[c] = [(y, x)]
            x += 1
        y += 1
        x = 0
    start = positions["S"][0]
    i = 0
    beams.add(start)
    splits = set()
    while i < max_y:
        tmp = beams.copy()
        for beam in tmp:
            beams.remove(beam)
            y, x = beam
            np = y + 1, x
            for item in positions:
                if np in positions[item]:
                    if item == ".":
                        beams.add(np)
                    elif item == "^":
                        splits.add(np)
                        np_1 = y + 1, x - 1
                        np_2 = y + 1, x + 1
                        beams.add(np_1)
                        beams.add(np_2)
        i += 1
    print(len(splits))
