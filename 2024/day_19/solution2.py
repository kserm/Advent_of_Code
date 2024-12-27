import os

towels = []
designs = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    chunks = file.read().strip().split("\n\n")
    towels = chunks[0].strip().split(", ")
    designs = chunks[1].strip().split("\n")

def find_designs(towels: list, target: str) -> int:
    res = {}
    tl = len(target)
    res[tl] = 0
    for t in towels:
        if target.startswith(t):
            k = len(t)
            if k not in res:
                res[k] = 1
    if not res:
        return 0
    for i in range(1, tl):
        if i in res:
            for t in towels:
                if target[i:].startswith(t):
                    nk = i + len(t)
                    if nk in res:
                        res[nk] += res[i]
                    else:
                        res[nk] = res[i]
    return res[tl]

total = 0
for design in designs:
    fd = find_designs(towels, design)
    total += fd

print(total)
