data = {}

with open('input.txt') as file:
    for line in file.readlines():
        l = line.strip().split(' -> ')
        # print(l)
        if '%' in l[0]:
            data[l[0][1:]] = {'type': 'ff', 'state': 'off', 'dest': [i for i in l[1].split(', ')]}
        elif '&' in l[0]:
            data[l[0][1:]] = {'type': 'con', 'inputs': []}
            for i in l[1].split(', '):
                data[l[0][1:]]['inputs'].append([i, 'low'])
        else:
            data[l[0]] = {'type': 'broadcaster', 'dest': [i for i in l[1].split(', ')]}

# ls = set()
# rs = set()

# with open('input.txt') as file:
#     for line in file.readlines():
#         l = line.strip().split(' -> ')
#         if l[0] != 'broadcaster':
#             ls.add(l[0][1:])
#             for i in l[1].split(', '):
#                 rs.add(i)

# print(rs.difference(ls))

def process_node(node: str, signal: str) -> str:
    if data[node]['type'] == 'ff':
        state = data[node]['state']
        if state == 'off' and signal == 'low':
            data[node]['state'] = 'on'
            return 'high'
        elif state == 'on' and signal == 'low':
            data[node]['state'] = 'off'
            return 'low'
    # else:
    #     nodes = data[node]['inputs']

end = 'rx'

low = 0
high = 0


start = 'broadcaster'
low += 1
signal = 'low'
print(start, data[start])
for node in data[start]['dest']:
    low += 1
    signal = process_node(node, 'low')
    print(node, data[node])
    # while node:
    #     if data[node]['type'] == 'ff' and signal == 'low':
    #         for n in data[node]['dest']:
    #             print(n, data[n])
    #             node = n
    #     if data[node]['type'] == 'con':
    #         break
                
                

