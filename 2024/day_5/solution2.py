import os

rules = {}

page_numbers = []
page_numbers_copy = []

page_numbers_to_update = []

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

page_numbers_copy = page_numbers[:]

def check_rules(number: int, rules_dict: dict, num_list: list) -> list:
    res = []
    il1 = []
    il2 = []
    indx = num_list.index(number)
    for i in range(len(num_list)):
        if res == False:
            break
        if i != indx:
            for item in rules_dict[number]:
                if i < indx:
                    if num_list[i] in item and number in item:
                        if item.index(number) == 0:
                            il1.append(i)
                if i > indx:
                    if num_list[i] in item and number in item:
                        if item.index(number) == 1:
                            il2.append(i)
    res.append(il1)
    res.append(il2)
    return res

def swap_positions(num1: int, num2: int, num_list: list):
    a, b = num_list.index(num1), num_list.index(num2)
    num_list[b], num_list[a] = num_list[a], num_list[b]

def update_numbers(rules_dict: dict, num_list: list) -> list:
    pages_index = page_numbers.index(num_list)
    for n in num_list:
        indxs = check_rules(n, rules_dict, num_list)
        if len(indxs[0]) >= len(indxs[1]):
            for i in range(len(indxs[1])):
                swap_positions(num_list[indxs[0][i]], num_list[indxs[1][i]], num_list)
            for i in range(len(indxs[1]), len(indxs[0])):
                indx = num_list.index(n)
                swap_positions(num_list[indxs[0][i]], num_list[indx], num_list)
        else:
            for i in range(len(indxs[0])):
                swap_positions(num_list[indxs[0][i]], num_list[indxs[1][i]], num_list)
            for i in range(len(indxs[0]), len(indxs[1])):
                indx = num_list.index(n)
                swap_positions(num_list[indxs[1][i]], num_list[indx], num_list)
    page_numbers[pages_index] = num_list

updated_pages = []
for i in range(len(page_numbers_copy)):
    for n in page_numbers_copy[i]:
        if check_rules(n, rules, page_numbers_copy[i]) != [[],[]]:
            updated_pages.append(page_numbers[i])
            break

# Oh, this is so stupid...
for item in page_numbers:
    update_numbers(rules, item)
    update_numbers(rules, item)
    update_numbers(rules, item)

total = 0

for item in updated_pages:
    indx = len(item) // 2
    total += item[indx]

print(total)