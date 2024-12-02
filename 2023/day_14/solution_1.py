data = []

tst_str = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

# data = [list(l) for l in tst_str.strip().split('\n')]
# print(data)

cube_rocks_postitions = set()
round_rocks_positions = set()
free_positions = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '#':
            cube_rocks_postitions.add((y, x))
        elif data[y][x] == 'O':
            round_rocks_positions.add((y, x))
        elif data[y][x] == '.':
            free_positions.add((y, x))


new_round_rocks_positions = set()
for line in range(len(data)):
    # print([item for item in round_rocks_positions if item[0]==line])
    items_to_discard = []
    is_allowed_axis = set()
    for item in free_positions:
        if item[0] == line:
            is_allowed_axis.add(item[1])
    for item in round_rocks_positions:
        if item[0] == line:
            items_to_discard.append(item)
            new_round_rocks_positions.add(item)
    for item in items_to_discard:
        round_rocks_positions.discard(item)
    # print(is_allowed_axis)
    # print(is_allowed_axis)
    for i in range(line+1, len(data)):
        for j in range(len(data[i])):
            items_to_discard = []
            if j in is_allowed_axis:
                for item in cube_rocks_postitions:
                    if item == (i, j):
                        is_allowed_axis.discard(j)
                for item in round_rocks_positions:
                    if item == (i, j):
                        new_position = (line, j)
                        new_round_rocks_positions.add(new_position)
                        free_positions.add(item)
                        free_positions.discard(new_position)
                        items_to_discard.append(item)
                        # round_rocks_positions.discard(item)
                        is_allowed_axis.discard(j)
                # print(items_to_discard)
                for item in items_to_discard:
                    round_rocks_positions.discard(item)
    
    # print([item for item in new_round_rocks_positions if item[0]==line])

# print(sorted(new_round_rocks_positions))
total = 0
rng = len(data)                
for i in range(rng):
    m = rng - i
    count = 0
    for item in new_round_rocks_positions:
        if item[0] == i:
            count += 1
    # print(i+1, count, m)
    total += m * count

print(total)
    # print(is_allowed_axis)
                
        