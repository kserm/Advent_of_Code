import numpy as np

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

tst_str = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
# data = [list(l) for l in tst_str.strip().split('\n')]

np_data = np.array(data)

visited = set()
start = (0, -1)
next_position = (0, 0)

rows = np_data.shape[0]
cols = np_data.shape[1]


def move_is_allowed(pos: tuple) -> bool:
    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        return True
    return False

def direction(current_position: tuple, next_position: tuple) -> tuple:
    y_diff = next_position[0] - current_position[0]
    x_diff = next_position[1] - current_position[1]
    sym = np_data[next_position]
    if sym == '\\' and x_diff == 1:
        return (1, 0)
    if sym == '\\' and x_diff == -1:
        return (-1, 0)
    elif sym == '/' and x_diff == 1:
        return (-1, 0)
    elif sym == '/' and x_diff == -1:
        return (1, 0)
    elif sym in ['-', '.'] and x_diff == 1:
        return (0, 1)
    elif sym in ['-', '.'] and x_diff == -1:
        return (0, -1)
    elif sym == '\\' and y_diff == 1:
        return (0, 1)
    elif sym == '\\' and y_diff == -1:
        return (0, -1)
    elif sym == '/' and y_diff == 1:
        return (0, -1)
    elif sym == '/' and y_diff == -1:
        return (0, 1)
    elif sym in ['|','.'] and y_diff == 1:
        return (1, 0)        
    elif sym in ['|','.'] and y_diff == -1:
        return (-1, 0)        


beams = []
beams.append([start, next_position, 0])
while beams:
    if not beams:
        break
    else:
        for b in range(len(beams)):
            repeats = beams[b][2]
            if repeats > 300:
                del beams[b]
                break
            cur_pos = beams[b][0]
            nxt_pos = beams[b][1]
            if move_is_allowed(nxt_pos):
                y_diff = nxt_pos[0] - cur_pos[0]
                x_diff = nxt_pos[1] - cur_pos[1]
                sym = np_data[nxt_pos]
                if sym == '|' and x_diff in [-1, 1]:
                    if nxt_pos in visited:
                        repeats += 1
                    else:
                        visited.add(nxt_pos)
                    cur_pos = (cur_pos[0] + y_diff, cur_pos[1] + x_diff)
                    nxt_up = (cur_pos[0] + 1, cur_pos[1])
                    nxt_down = (cur_pos[0] - 1, cur_pos[1])
                    if move_is_allowed(nxt_up):
                        beams[b] = [cur_pos, nxt_up, repeats]
                        if move_is_allowed(nxt_down):
                            beams.append([cur_pos, nxt_down, repeats])
                    else:
                        if move_is_allowed(nxt_down):
                            beams[b] = [cur_pos, nxt_down, repeats]
                elif sym == '-' and y_diff in [-1, 1]:
                    if nxt_pos in visited:
                        repeats += 1
                    else:
                        visited.add(nxt_pos)
                    cur_pos = (cur_pos[0] + y_diff, cur_pos[1] + x_diff)
                    nxt_left = (cur_pos[0], cur_pos[1] - 1)
                    nxt_right = (cur_pos[0], cur_pos[1] + 1)
                    if move_is_allowed(nxt_left):
                        beams[b] = [cur_pos, nxt_left, repeats]
                        if move_is_allowed(nxt_right):
                            beams.append([cur_pos, nxt_right, repeats])
                    else:
                        if move_is_allowed(nxt_right):
                            beams[b] = [cur_pos, nxt_right, repeats]
                else:
                    move = direction(cur_pos, nxt_pos)
                    cur_pos = nxt_pos
                    nxt_pos = (cur_pos[0] + move[0], cur_pos[1] + move[1])
                    if cur_pos in visited:
                        repeats += 1
                    else:
                        visited.add(cur_pos)
                    beams[b] = [cur_pos, nxt_pos, repeats]
            else:
                del beams[b]
                break

print(len(visited))
