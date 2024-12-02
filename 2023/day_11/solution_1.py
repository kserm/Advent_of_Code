from itertools import combinations

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(list(line.strip()))

mdata = []
for l in range(len(data)):
    if all([x == '.' for x in data[l]]):
        mdata.append(data[l])
        mdata.append(data[l])
    else:
        mdata.append(data[l])

hs = set()
ds = set()
for r in range(len(mdata)):
    for c in range(len(mdata[r])):
        if mdata[r][c] == '#':
            hs.add(c)
        else:
            ds.add(c)

indxs = sorted(ds.difference(hs))

mdata2 = [[] for x in range(len(mdata))]

for r in range(len(mdata)):
    for c in range(len(mdata[r])):
        if c in indxs:
            mdata2[r].append(mdata[r][c])
            mdata2[r].append(mdata[r][c])
        else:
            mdata2[r].append(mdata[r][c])

galaxies = set()

for r in range(len(mdata2)):
    for c in range(len(mdata2[r])):
        if mdata2[r][c] == '#':
            galaxies.add((r,c))

galaxies_combinations = list(combinations(galaxies, 2))
total = 0
for g in galaxies_combinations:
    v = abs(g[0][0] - g[1][0])
    h = abs(g[0][1] - g[1][1])
    sum = v + h
    total += sum

print(total)
