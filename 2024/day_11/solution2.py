import os

data = {}

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        for n in line.strip().split():
            if n in data:
                data[n] += 1
            else:
                data[n] = 1

for _ in range(75):
    new_dict = {}
    for n in data:
        j = data[n]
        if n == '0':
            if '1' in new_dict:
                new_dict['1'] += j
            else:
                new_dict['1'] = j
        elif (len(n) % 2) == 0:
            m = len(n) // 2
            a = str(int(n[:m]))
            b = str(int(n[m:]))
            if a in new_dict:
                new_dict[a] += j
            else:
                new_dict[a] = j
            if b in new_dict:
                new_dict[b] += j
            else:
                new_dict[b] = j
        elif (len(n) % 2) == 1:
            a = str(int(n)*2024)
            if a in new_dict:
                new_dict[a] += j
            else:
                new_dict[a] = j
    data = new_dict

total = 0
for v in data.values():
    total += v

print(total)
