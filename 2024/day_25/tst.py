with open(r"D:\Projects\Python\Advent_of_Code\2024\day_25\input.txt") as f:
    s = f.read().strip()

g = [list(r) for r in s.split("\n")]
n,m = len(g),len(g[0])

keys = []
locks = []

ans = 0

# line by line input
for l in s.split("\n\n"):
    ll = l.split("\n")
    islock = False
    if ll[0].startswith("###"):
        islock = True
    g = [list(r) for r in ll]
    hts = [sum(1 for i in range(len(g)) if g[i][j] == "#") - 1 for j in range(len(g[0]))]
    if islock:
        locks.append(tuple(hts))
    else:
        keys.append(tuple(hts))


for k in keys:
    for l in locks:
        good = True
        for ki,li in zip(k,l):
            if ki + li > 5:
                good = False
                break
        if good:
            ans += 1
    

print(ans)