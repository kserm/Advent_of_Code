# (6875, 471)
data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

n = (-1, 0)
s = (1, 0)
w = (0, -1)
e = (0, 1)
directions = (n, s, w, e)
tiles = {
    '|': (n, s),
    '-': (w, e),
    'L': (n, e),
    'J': (w, n),
    '7': (w, s),
    'F': (s, e),
}

coord_mapings = {}

S = (0, 0)
for y in range(len(data)):
    for x in range(len(data[y])):
        c = data[y][x]
        if c in tiles.keys():
            # print(c, x, y)
            coord_mapings[(y, x)] = tiles[c]
        elif c == 'S':
            S = (y, x)

def check_move_is_allowed(coord, move: tuple) -> bool:
    y, x = coord
    ym, xm = move
    # print(coord, move, coord_mapings[(y+ym, x+xm)])
    tile = data[y+ym][x+xm]
    if tile in tiles.keys():
        for d in coord_mapings[(y+ym, x+xm)]:
            possible_from = (y+ym+d[0], x+xm+d[1])
            # print(d, tile, possible_from)
            if possible_from == coord:
                return True
    return False

start = []
for d in directions:
    if check_move_is_allowed(S, d):
        start.append((S[0]+d[0], S[1]+d[1]))

visited = set()
visited.add(S)
while True:
    if start:
        res = []
        for item in start:
            if start:
                visited.add(item)
                pd = coord_mapings[item]
                for d in pd:
                    if check_move_is_allowed(item, d):
                        new_item = item[0]+d[0], item[1]+d[1]
                        if new_item not in visited:
                            res.append(new_item)
                start = res
    else:
        break

print(len(visited) // 2)

# output_data = [[] for i in range(len(data))]
# for y in range(len(data)):
#     for x in range(len(data[y])):
#         if (y, x) in visited:
#             output_data[y].append('X')
#         else:
#             output_data[y].append(data[y][x])
        # lb = len(data[y])
        # rb = 0
        # for item in visited:
        #     v_y, v_x = item
        #     if v_y == y:
        #         lb = min(lb, v_x)
        #         rb = max(rb, v_x)
        # if (y, x) in visited:
        #     output_data[y].append('X')
        # elif x < lb or x > rb:
        #     output_data[y].append('#')
        # else:
        #     output_data[y].append(data[y][x])

# output_str = ''
# for i in output_data:
#     output_str += ''.join(i) + '\n'

# with open('output.txt', 'w') as file:
#     file.write(output_str)

# counter = 0
# for item in output_data:
#     for c in item:
#         if c != 'X' or c != '#':
#             counter += 1

# print(counter)
