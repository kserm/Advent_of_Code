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

total = 0
for num in data:
    for _ in range(2000):
        num = calc_secr_num(num)
    total += num

print(total)
