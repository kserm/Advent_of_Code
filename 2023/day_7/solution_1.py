data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.split())

card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def find_combination(inp_list: list) -> int:
    types_dict = {}
    res = 0
    for i in inp_list:
        if types_dict.get(i):
            types_dict[i] += 1
        else:
            types_dict[i] = 1
    keys = list(types_dict.keys())
    if len(keys) == 1:
        res = 6
    elif len(keys) == 2:
        for key in keys:
            if types_dict[key] == 4:
                res = 5
                break
            else:
                res = 4
    elif len(keys) == 3:
        for key in keys:
            if types_dict[key] == 3:
                res = 3
                break
            else:
                res = 2
    elif len(keys) == 4:
        res = 1
    else:
        res = 0
    return res

def cards_powers_list(cards: str) -> list:
    powers = []
    for card in cards:
        powers.append(len(list(card_ranks)) - card_ranks.index(card))
    return powers

res = [[],[],[],[],[],[],[]]
for item in data:
    res_indx = find_combination(list(item[0]))
    card_power = cards_powers_list(list(item[0]))
    res[res_indx].append([card_power, item])

new_res = []
for i in range(len(res)):
    cur_gr = res[i]
    tmp_lst = []
    for j in cur_gr:
        tmp_lst.append(j)
    new_res.append(sorted(tmp_lst))

output = []
for item in new_res:
    for i in item:
        output.append(i[1])

total = 0
for i in range(len(output)):
    m = i + 1
    num = int(output[i][1])
    total += num * m

print(total)