import os

dir_path = os.path.dirname(os.path.realpath(__file__))


rotations = {}
total = 0

def calculate(a, b, c: str):
    global total
    if c == "R":
        res = (a + b) % 100
        res2 = (a + b) // 100
    elif c == "L":
        res = (a - b) % 100
        res2 = (a - b) // 100
    if res == 0 and res2 > 0:
        total += 1
        total += abs(res2) - 1
    else:
        total += abs(res2)
    return res


current = 50
with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        line_formatted = line.strip()
        action = line_formatted[0]
        num = int(line_formatted[1:])
        current = calculate(current, num, action)

print(total)
