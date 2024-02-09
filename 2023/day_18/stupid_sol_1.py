data = []

with open('tst.txt', 'r') as file:
    y = 0
    for line in file.readlines():
        for x in range(len(line)):
            if line[x] == '#':
                data.append((y,x))
        y += 1

print(len(data))