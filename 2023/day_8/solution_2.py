from math import lcm

data = {}

with open('input.txt', 'r') as file:
    directions = list(file.readline().strip())
    file.readline()
    for line in file.readlines():
        lst = line.split(' = ')
        lr = lst[1].strip('(').strip(')\n').split(', ')
        a, b = lr
        data[lst[0]] = a, b

instructions = [0 if i == 'L' else 1 for i in directions]
starting_nodes = []
end_nodes = []
for item in data.keys():
    if item.endswith('Z'):
        end_nodes.append(item)
    if item.endswith('A'):
        starting_nodes.append(item)

res = []
for n in starting_nodes:
    node_to_search = n
    steps = 0
    while node_to_search not in end_nodes:
        for i in range(len(instructions)):
            direction = instructions[i]
            if i == len(instructions) - 1:
                i = 0
            node = node_to_search
            node_to_search = data[node][direction]
            steps += 1
            # print(steps, node_to_search)
            if node_to_search in end_nodes:
                res.append(steps)
                break
print(lcm(*res))