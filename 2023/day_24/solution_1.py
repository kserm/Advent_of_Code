from itertools import combinations

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        values = [i.split(', ') for i in line.strip().split(' @ ')]
        positions = list(map(int, values[0]))
        velocities = list(map(int, values[1]))
        data.append((positions, velocities))

tst_str = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

# data = [tuple(list(map(int, i.split(', '))) for i in line.split(' @ ')) for line in tst_str.strip().split('\n')]

# min_b = 7
# max_b = 27
min_b = 200000000000000
max_b = 400000000000000

data_comb = combinations(data, 2)

def find_intersection(p1, v1, p2, v2):
    px1, py1 = p1
    vx1, vy1 = v1
    px2, py2 = p2
    vx2, vy2 = v2

    if vx1 == 0 and vx2 == 0:
        return None

    if vx1 == 0:
        x = px1
        y = py2 + vy2 / vx2 * (x - px2)
    elif vx2 == 0:
        x = px2
        y = py1 + vy1 / vx1 * (x - px1)
    else:
        m1 = vy1 / vx1
        m2 = vy2 / vx2
        b1 = py1 - m1 * px1
        b2 = py2 - m2 * px2

        if m1 == m2:
            return None

        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1

    intersection = (x, y)

    if (
        min_b <= intersection[0] <= max_b
        and min_b <= intersection[1] <= max_b
        and (vx1 * (intersection[0] - px1) > 0)
        and (vx2 * (intersection[0] - px2) > 0)
    ):
        return intersection
    else:
        return None

total = 0
for item in data_comb:
    A, B = item
    p1 = A[0][:2]
    v1 = A[1][:2]
    p2 = B[0][:2]
    v2 = B[1][:2]
    if find_intersection(p1, v1, p2, v2):
        total += 1

print(total)
