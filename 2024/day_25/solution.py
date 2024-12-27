import os

locks = []
keys = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    chunks = file.read().strip().split("\n\n")
    for chunk in chunks:
        tmp = []
        lst = chunk.strip().split("\n")
        if "#####" in lst[0]:
            for x in range(len(lst[0])):
                y = 0
                for i in range(1, len(lst)-1):
                    if lst[i][x] == "#":
                        y += 1
                    else:
                        break
                tmp.append(y)
            locks.append(tmp)
        elif "#####" in lst[-1]:
            for x in range(len(lst[0])):
                y = 0
                for i in range(len(lst)-2, 0, -1):
                    if lst[i][x] == "#":
                        y += 1
                    else:
                        break
                tmp.append(y)
            keys.append(tmp)

total = 0
for lock in locks:
    for key in keys:
        flag = True
        for item in zip(key, lock):
            if sum(item) > 5:
                flag = False
                break
        if flag:
            total += 1

print(total)
