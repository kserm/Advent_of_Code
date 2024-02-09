data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        item = line.strip().split('~')
        xyz = [i.split(',') for i in item]
        x, y, z = map(int, xyz[0])
        x1, y1, z1 = map(int, xyz[1])
        if z == z1:
            z = (z, )
        else:
            z = (z, z1)
        if x == x1:
            x = (x, )
        else:
            x = (x, x1)
        if y == y1:
            y = (y, )
        else:
            y = (y, y1)
        data.append([z, x, y])

j = 1
for i in sorted(data)[:50]:
    print(j, i)
    j += 1