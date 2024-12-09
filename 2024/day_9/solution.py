import os

dir_path = os.path.dirname(os.path.realpath(__file__))

data_str = ''

with open(f'{dir_path}/input.txt', 'r') as file:
    data_str = file.read().strip()

data = list(data_str)

files = list(map(int, data[::2]))
free_spaces = list(map(int, data[1::2]))

blocks = []

for i in range(len(files)-1):
    for j in range(files[i]):
        blocks.append(i)
    for j in range(free_spaces[i]):
        blocks.append('.')
for j in range(files[-1]):
    blocks.append(len(files)-1)

for i in range(len(blocks)):
    if blocks[i] == '.':
        for j in range(len(blocks)-1, 0, -1):
            if blocks[j] != '.' and i < j:
                blocks[i], blocks[j] = blocks[j], blocks[i]
                break

while blocks[-1] == '.':
    blocks.pop()

checksum = 0
for i in range(len(blocks)):
    checksum += i * blocks[i]

print(checksum)
