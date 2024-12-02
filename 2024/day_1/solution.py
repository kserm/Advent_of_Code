import os

list_1 = []
list_2 = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        list_1.append(line.strip().split()[0])
        list_2.append(line.strip().split()[1])

def difnum(lst):
    return abs(int(lst[0]) - int(lst[1]))

diff_list = map(difnum, zip(sorted(list_1), sorted(list_2)))

print(sum(diff_list))