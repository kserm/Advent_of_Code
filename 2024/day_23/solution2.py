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
    set_1 = set((a, *data[a]))
    for b in data[a]:
        set_2 = set((b, *data[b]))
        pre_conn = set_1.intersection(set_2)
        fconn = pre_conn.copy()
        for c in pre_conn:
            if (c != a) and (c != b):
                set_3 = set((c, *data[c]))
                insec = set_1.intersection(set_2, set_3)
                if len(insec) < len(pre_conn):
                    fconn.remove(c)
        if fconn not in connections:
            connections.append(fconn)

ml = 0
i = 0
for j in range(len(connections)):
    conn = connections[j]
    if len(conn) > ml:
        i = j
        ml = len(conn)

print(",".join(sorted(connections[i])))
