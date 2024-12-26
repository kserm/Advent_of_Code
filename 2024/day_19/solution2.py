import os

towels = []
designs = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    chunks = file.read().strip().split("\n\n")
    towels = chunks[0].strip().split(", ")
    designs = chunks[1].strip().split("\n")

def find_designs(towels: list, target: str, parts=None, res=None, visited=None) -> list:
    if parts is None:
        parts = {}
        for t in towels:
            if target.startswith(t):
                if t not in parts:
                    parts[t] = [[t]]
    if res is None:
        res = []
    if visited is None:
        visited = set()
    if target in visited:
        return res
    for p in parts.copy():
        if p not in visited:
            visited.add(p)
            for item in parts[p]:
                part = "".join(item)
                left = target[len(part):]
                if part != target[:len(part)]:
                    parts[p].remove(item)
                    continue
                if part == target:
                    res.append(item)
                    continue
                for t in towels:
                    if left.startswith(t):
                        nk = part + t
                        ni = item + [t]
                        if nk not in parts:
                            parts[nk] = [ni]
                        else:
                            parts[nk].append(ni)
            find_designs(towels, target, parts, res, visited)
    return res

test_towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
test_designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]

# towels = test_towels
# designs = test_designs

# design = designs[2]
# print(find_designs(towels, design))

total = 0
i = 1
ii = len(designs)
for design in designs:
    print(f"{i} of {ii}")
    fd = find_designs(towels, design)
    total += len(fd)
    i += 1


print(total)
