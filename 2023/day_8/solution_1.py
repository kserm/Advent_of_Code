data = []

with open('input.txt', 'r') as file:
    directions = list(file.readline().strip())
    file.readline()
    for line in file.readlines():
        lst = line.split(' = ')
        lr = lst[1].strip('(').strip(')\n').split(', ')
        a, b = lr
        data.append((lst[0], (a, b)))

# print(list(directions[292]))
# # print(data)

i = 0
j = 0
steps = 0
node_to_search = 'AAA'
for i in data:
    if i[0] == node_to_search:
        j = data.index(i)
# while end != 2:
# while steps < 1000:
#     if steps == 500:
#         break
while True:
    if node_to_search == 'ZZZ':
        print(steps)
        break
    else:
        for i in range(len(directions)):
            if node_to_search == 'ZZZ':
                print(steps)
                break
            direction = directions[i]
            if direction == 'L':
                index = 0
            elif direction == 'R':
                index = 1
            node_to_search = data[j][1][index]
            # print(steps, j, node_to_search, i, direction)
            for item in data:
                if item[0] == node_to_search:
                    j = data.index(item)
            steps += 1
            if i == len(directions)-1:
                # print(i, node_to_search)
                i = 0
