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
    beams.add((start, 1))
    total = 0
    while i < max_y:
        tmp = beams.copy()
        for item in tmp:
            pos = item[0]
            score = item[1]
            y, x = pos
            np = y + 1, x
            for p in positions:
                if np in positions[p]:
                    if p == ".":
                        new_item = (np, score)
                        for beam in beams:
                            if np in beam:
                                new_item = (np, beam[1] + score)
                                beams.remove(beam)
                                break
                        beams.add(new_item)
                    elif p == "^":
                        np_1 = y + 1, x - 1
                        np_2 = y + 1, x + 1
                        new_item_1 = (np_1, score)
                        new_item_2 = (np_2, score)
                        for beam in beams:
                            if np_1 in beam:
                                new_item_1 = (np_1, beam[1] + score)
                                beams.remove(beam)
                                break
                        for beam in beams:
                            if np_2 in beam:
                                new_item_2 = (np_2, beam[1] + score)
                                beams.remove(beam)
                                break
                        beams.add(new_item_1)
                        beams.add(new_item_2)
        for t in tmp:
            beams.remove(t)
        i += 1
    for beam in beams:
        total += beam[1]
    print(total)
