data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

tst_str = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

# data = [list(l) for l in tst_str.strip().split('\n')]


directions = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
]

start = (0, 1)
end = (140, 139)

def move_is_allowed(cur: tuple, nxt: tuple) -> bool:
    y, x = nxt
    dy = nxt[0] - cur[0]
    dx = nxt[1] - cur[1]
    if y not in range(0, len(data)) or x not in range(0, len(data[0])):
        return False
    if data[y][x] == '#':
        return False
    elif data[y][x] == '>' and (dy, dx) == (0, -1):
        return False
    elif data[y][x] == 'v' and (dy, dx) == (-1, 0):
        return False
    elif data[y][x] == '<' and (dy, dx) == (0, 1):
        return False
    elif data[y][x] == '^' and (dy, dx) == (1, 0):
        return False
    return True


def move(pos: tuple, visited: set) -> list:
    res = []
    for d in directions:
        next_pos = (pos[0]+d[0], pos[1]+d[1])
        if move_is_allowed(pos, next_pos) and next_pos not in visited:
            res.append(next_pos)
    return res

res_routes = []
routes = []
routes.append([start, 0, set()])
routes[0][2].add(start)
while routes:
    i = 0
    for route in routes:
        cur_pos = route[0]
        steps = route[1]
        vis = route[2]
        next_pos = move(cur_pos, vis)
        if not next_pos:
            res_routes.append(route)
            routes.pop(i)
            break
        else:
            steps += 1
            if len(next_pos) == 1:
                vis.add(next_pos[0])
                next_route = [next_pos[0], steps, vis]
                routes[i] = next_route
            else:
                cur_vis = vis
                cur_vis.add(next_pos[0])
                next_route = [next_pos[0], steps, cur_vis]
                routes[i] = next_route
                for pos in next_pos[1:]:
                    next_route = [pos, steps, set()]
                    next_route[2].add(cur_pos)
                    next_route[2].add(pos)
                    routes.append(next_route)
        i += 1

max_steps = 0
for r in res_routes:
    steps = r[1]
    max_steps = max(max_steps, steps)

print(max_steps)