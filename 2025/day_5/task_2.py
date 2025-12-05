import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    fresh = []
    items = file.read().split("\n\n")
    ranges = [list(map(int, i.split("-"))) for i in items[0].split("\n")]
    r = sorted(ranges)
    i = 0
    while i < len(r):
        a, b = r[i]
        flag = True
        for j in r[i + 1 :]:
            c, d = j
            if b >= c - 1:
                if b > d:
                    r.remove(j)
                    flag = False
                else:
                    r[i] = a, d
                    r.remove(j)
                    flag = False
        if flag:
            i += 1

    total = 0
    for item in r:
        a, b = item
        if a == b:
            print(True)
        total += b - a + 1
    print(total)
