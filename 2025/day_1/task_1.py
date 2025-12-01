import os

dir_path = os.path.dirname(os.path.realpath(__file__))


rotations = {}

def calculate(a, b, c: str):
    if c == "R":
        res = (a + b) % 100
    elif c == "L":
        res = (a - b) % 100
    return res

def process(s, inp: str):
    action = inp[0]
    num = int(inp[1:])
    result = calculate(s, num, action)
    return result

total = 0
current = 50
with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        line_formatted = line.strip()
        current = process(current, line_formatted)
        # print(line_formatted, "   ", current)
        if current == 0:
            total += 1


print(total)
