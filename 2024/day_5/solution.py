import os

rules = {}

page_numbers = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    sections = file.read().split('\n\n')
    pairs = sections[0].split('\n')
    for pair in pairs:
        numbers = list(map(int, pair.split('|')))
        for number in numbers:
            if number in rules:
                rules[number] += [numbers]
            else:
                rules[number] = [numbers]
    page_numbers = [list(map(int , s.strip().split(','))) for s in sections[1].split('\n')]

def check_rules(number: int, rules_dict: dict, num_list: list) -> bool:
    res = True
    indx = num_list.index(number)
    for i in range(len(num_list)):
        if res == False:
            break
        if i != indx:
            for item in rules_dict[number]:
                if i < indx:
                    if num_list[i] in item and number in item:
                        if item.index(number) == 0:
                            res = False
                            break
                if i > indx:
                    if num_list[i] in item and number in item:
                        if item.index(number) == 1:
                            res = False
                            break
    return res

total = 0
for item in page_numbers:
    flag = True
    for n in item:
        flag = check_rules(n, rules, item)
        if flag == False:
            break
    if flag == True:
        indx = len(item) // 2
        total += item[indx]

print(total)