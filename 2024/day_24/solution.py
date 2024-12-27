import os

data = {}
operations = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    chunks = file.read().strip().split("\n\n")
    for line in chunks[0].strip().split("\n"):
        k, v = line.strip().split(": ")
        data[k] = int(v)
    for line in chunks[1].strip().split("\n"):
        a, b, c, _, d = line.strip().split(" ")
        o = (a, b, c, d)
        operations.append(o)

max_p = len(operations)
processed = set()
while len(processed) < max_p:
    for operation in operations:
        if operation not in processed:
            a, b, c, d = operation
            if (a in data) and (c in data):
                res = None
                if b == "AND":
                    res = data[a] & data[c]
                elif b == "OR":
                    res = data[a] | data[c]
                elif b == "XOR":
                    res = data[a] ^ data[c]
                data[d] = int(res)
                processed.add(operation)
            else:
                continue

result = []
for k in sorted(data):
    if k.startswith("z"):
        result.append(data[k])

rr = [str(i) for i in reversed(result)]

print(int("".join(rr), 2))
