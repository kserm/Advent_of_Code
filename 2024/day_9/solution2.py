import os

dir_path = os.path.dirname(os.path.realpath(__file__))

data_str = ''

with open(f'{dir_path}/input.txt', 'r') as file:
    data_str = file.read().strip()

data = list(data_str)

files = list(map(int, data[::2]))
free_spaces = list(map(int, data[1::2]))

blocks = []

blocks = list(zip(files, free_spaces, range(len(files))))
blocks.append((files[-1], 0, len(files)-1, True))

i = len(blocks) - 1
while i >= 0:
    flag = False
    for j in range(len(blocks)):
        if (blocks[i][0] <= blocks[j][1]) and (j < i):
            blocks[i-1] = (blocks[i-1][0], blocks[i-1][1]+blocks[i][0]+blocks[i][1], blocks[i-1][2])
            new_block = (blocks[i][0], blocks[j][1] - blocks[i][0], blocks[i][2])
            blocks.insert(j+1, new_block)
            blocks.pop(i+1)
            blocks[j] = (blocks[j][0], 0, blocks[j][2])
            flag = True
            break
    if not flag:
        i -= 1

blocks_list = []

for item in blocks:
    for i in range(item[0]):
        blocks_list.append(item[2])
    for i in range(item[1]):
        blocks_list.append('.')

checksum = 0
for i in range(len(blocks_list)):
    if blocks_list[i] != '.':
        checksum += i * blocks_list[i]

print(checksum)
