import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.read()
    regions = []
    presents = {}
    for item in lines.split("\n\n"):
        if "x" in item:
            ln = item.strip().split("\n")
            for i in ln:
                ks, vs = i.split(": ")
                kl = [int(i) for i in ks.split("x")]
                vl = [int(i) for i in vs.split()]
                k = kl[0] * kl[1]
                regions.append([k, vl])
        else:
            id, form = item.split(":\n")
            presents[int(id)] = form.count("#")
    res = 0
    for region in regions:
        area, pres_seq = region
        total = 0
        for id in range(len(pres_seq)):
            pn = pres_seq[id]
            ps = presents[id]
            total += pn * ps
        if total <= area:
            res += 1
    print(res)