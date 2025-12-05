import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    fresh = set()
    items = file.read().split("\n\n")
    ranges = [list(map(int, i.split("-"))) for i in items[0].split("\n")]
    ids = [int(i) for i in items[1].split("\n")]
    for id in ids:
        if id in fresh:
            continue
        for r in ranges:
            if id in range(r[0], r[1] + 1):
                fresh.add(id)
    print(len(fresh))
