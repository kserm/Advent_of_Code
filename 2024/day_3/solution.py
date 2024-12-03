import os
import re

memory = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        memory.append(line)

matches = []

for line in memory:
    m = re.findall("mul\(\d+,\d+\)", line)
    matches.append(m)

total = 0

for item in matches:
    for s in item:
        numbers = s.lstrip("mul(").rstrip(")").split(",")
        total += int(numbers[0]) * int(numbers[1])

print(total)