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

s_list = sorted(visited)
my_area = 0
# sum1 = 0
# sum2 = 0
for i in range(1, len(s_list)):
    y1, x1 = s_list[i]
    y0, x0 = s_list[i-1]
    # sum1 += y0*x1 - y1*x0
    my_area += y1*x0 - y0*x1

print(my_area)
print(len(visited)/2)
total = my_area - (len(visited)/2) + 1
# print(sum1/2)

rng = len(data)
# total = 0
# rng = 1
# for i in range(rng):
#     vl = []
#     for item in sorted(visited):
#         if item[0] == i:
#             vl.append(item)
#     c = 0
#     for j in range(1, len(vl)):
#         x1 = vl[j][1]
#         y1 = vl[j][0]
#         if data[y][x] != '-':
#             c += 1
#         x0 = vl[j-1][1]
#         dx = x1 - x0
#         if dx > 1 and ((c%2 == 0) and ((c+1)%2 == 1)):
#             total += dx - 1
    # print(i, total, vl)

print(total)

def interior_area(points: list) -> float:
    padded_points = [*points, points[0]]  # form pair with last and first
    # print(padded_points)
    return (
        sum(
            row1 * col2 - row2 * col1
            for (row1, col1), (row2, col2) in zip(padded_points, padded_points[1:])
        )
        / 2
    )

area = interior_area(sorted(visited))
print(abs(area))
      
num_interior_points = int(abs(area) - 0.5 * len(visited) + 1)
print(num_interior_points)
