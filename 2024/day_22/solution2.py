import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        data.append(int(line.strip()))

def calc_secr_num(sn: int) -> int:
    mult = sn * 64
    sn = sn ^ mult
    sn = sn % 16777216
    d = int(sn / 32)
    sn = sn ^ d
    sn = sn % 16777216
    m = sn * 2048
    sn = sn ^ m
    sn = sn % 16777216
    return sn

totals = {}
for num in data:
    to_skip = set()
    seq = []
    i = 0
    lld = int(str(num)[-1])
    for _ in range(2000):
        num = calc_secr_num(num)
        cld = int(str(num)[-1])
        dif = cld - lld
        lld = cld
        seq.append(dif)
        if len(seq) == 4:
            s = tuple(seq)
            if s in totals:
                if s not in to_skip:
                    totals[s] += cld
                    to_skip.add(s)
            else:
                totals[s] = cld
                to_skip.add(s)
            seq.pop(0)

print(max(totals.values()))
