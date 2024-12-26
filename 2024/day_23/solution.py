import os

data = {}

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        a, b = line.strip().split("-")
        if a in data:
            data[a].append(b)
        else:
            data[a] = [b]
        if b in data:
            data[b].append(a)
        else:
            data[b] = [a]

connections = []

for a in data:
    for b in data[a]:
        for c in data[b]:
            if c in data[a]:
                nc = {a, b, c}
                if nc not in connections:
                    connections.append(nc)

total = 0
for connection in connections:
    for comp in connection:
        if comp.startswith("t"):
            total += 1
            break

print(total)
