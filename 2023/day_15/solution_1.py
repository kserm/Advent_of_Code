data = []

with open('input.txt') as file:
    for line in file.readlines():
        data = line.strip().split(',')

def calc_hash(s: str) -> int:
    v = 0
    m = 17
    for c in s:
        code = ord(c)
        v += code
        v *= m
        v = v % 256
    return v

total = 0
for i in data:
    total += calc_hash(i)

print(total)