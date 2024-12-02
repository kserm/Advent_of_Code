data = []

with open('output.txt', 'r') as file:
    y = 0
    for line in file.readlines():
        for x in range(len(line)):
            if line[x] == '#':
                data.append((y,x))
        y += 1     

total = 0

def split_sequence(arr: list) -> bool:
    res = []
    j = 0
    res.append([])
    for i in range(1, len(arr)):
        dx = arr[i][1] - arr[i-1][1]
        if dx == 1:
            res[j].append(arr[i-1])
        else:
            res[j].append(arr[i-1])
            j += 1
            res.append([])
            res[j].append(arr[i])
            continue
    return res

# for y in range(288):
for y in range(35,36):
    line = [item for item in data if item[0]==y]
    print(split_sequence(line))

print(total)