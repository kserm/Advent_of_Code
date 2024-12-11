import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        data = line.strip().split()

for _ in range(25):
    new_data = []
    for n in data:
        if n == '0':
            new_data.append('1')
        elif (len(n) % 2) == 0:
            m = len(n) // 2
            a = int(n[:m])
            b = int(n[m:])
            new_data.append(str(a))
            new_data.append(str(b))
        elif (len(n) % 2) == 1:
            new_data.append(str(int(n)*2024))
    data = new_data.copy()

print(len(data))