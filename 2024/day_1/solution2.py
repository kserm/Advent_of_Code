import os

list_1 = []
list_2 = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        list_1.append(line.strip().split()[0])
        list_2.append(line.strip().split()[1])

similarity_list = []
for i in list_1:
    x = 0
    for j in list_2:
        if i == j:
            x += 1
    similarity_list.append((i,x))

def mult_sim(t):
    return int(t[0])*int(t[1])

print(sum(map(mult_sim, similarity_list)))