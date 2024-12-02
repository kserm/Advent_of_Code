import os

reports = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        reports.append(list(map(int, line.split())))

def is_safe_incr(l: list) -> bool:
    res = True
    for i in range(1, len(l)):
        d = l[i] - l[i-1]
        if d < 1 or d > 3:
            res = False
            return res
    return res

def is_safe_decr(l: list) -> bool:
    res = True
    for i in range(1, len(l)):
        d = l[i-1] - l[i]
        if d < 1 or d > 3:
            res = False
            return res
    return res

total = 0

for r in reports:
    if is_safe_incr(r) or is_safe_decr(r):
        total += 1

print(total)