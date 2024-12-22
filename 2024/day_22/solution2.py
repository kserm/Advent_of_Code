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

test_data = [1, 2, 3, 2024]

# data = test_data

ref_seq = [-2, 1, -1, 3]


unique_sequens = set()
for num in data:
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
            unique_sequens.add(s)
            seq.pop(0)

a = len(unique_sequens)

def get_total(numbers: list, refseq: list) -> int:
    total = 0
    for num in numbers:
        seq = []
        i = 0
        lld = int(str(num)[-1])
        for _ in range(2000):
            num = calc_secr_num(num)
            cld = int(str(num)[-1])
            dif = cld - lld
            lld = cld
            if dif == refseq[i]:
                seq.append(dif)
                i += 1
            else:
                if seq:
                    seq.append(dif)
                    i += 1
            if len(seq) == 4:
                if seq == ref_seq:
                    total += cld
                    break
                else:
                    seq = []
                    i = 0
    return total

totals = {}
i = 1
for rs in unique_sequens:
    print(f"Processing {i} of {a}")
    total = get_total(data, rs)
    if total in totals:
        totals[total].append(rs)
    else:
        totals[total] = [rs]
    i += 1

for k in sorted(totals):
    print(k)
# print(get_total(data, ref_seq))
