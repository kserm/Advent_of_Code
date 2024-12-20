import os

towels = []
designs = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    chunks = file.read().strip().split("\n\n")
    towels = chunks[0].strip().split(", ")
    designs = chunks[1].strip().split("\n")

def find_match(design: str) -> bool:
    matches = []
    for t in towels:
        d = design
        if d.startswith(t):
            d = d[len(t):]
            matches.append([d, t])
    while matches:
        tmp_m = []
        for m in range(len(matches)):
            m = matches.pop()
            des = m[0]
            res = m[1]
            if res == design:
                return True
            for t in towels:
                if des.startswith(t):
                    d = des[len(t):]
                    r = res + t
                    item = [d, r]
                    if item not in tmp_m:
                        tmp_m.append(item)
        matches = tmp_m
    if not matches:
        return False

total = 0
for design in designs:
    fm = find_match(design)
    if fm:
        total += 1

print(total)
