# 246436046

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.split())

card_ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def find_combination(inp_str: str) -> list:
    comb_dict = {}
    comb_dict_if_joker = {}
    res = []
    for c in inp_str:
        if comb_dict.get(c):
            comb_dict[c] += 1
        else:
            comb_dict[c] =1
    keys = comb_dict.keys()
    if 'J' in keys:
        if len(comb_dict) == 1:
            comb_dict_if_joker = comb_dict
        max_value = 1
        max_key = 'J'
        for key in keys:
            if key != 'J':
                if comb_dict[key] > max_value:
                    max_value = comb_dict[key]
                    max_key = key
                elif comb_dict[key] == max_value:
                    for key in keys:
                        if key != max_key and key != 'J':
                            max_key = card_ranks[min(card_ranks.index(max_key), card_ranks.index(key))]
        for key in keys:
            if key == max_key and key != 'J':
                comb_dict_if_joker[key] = comb_dict[key] + comb_dict['J']
            else:
                if key != 'J' and key != max_key:
                    comb_dict_if_joker[key] = comb_dict[key]
        comb_dict = comb_dict_if_joker
    keys = comb_dict.keys()
    comb_num = len(keys)
    max_val = 1
    max_key = 'J'
    pwr = 0
    for key in keys:
        if comb_dict[key] > max_val:
            max_val = comb_dict[key]
            max_key = key
    if max_key != 'J':
        p = len(card_ranks) - card_ranks.index(max_key)
        pwr += p*comb_dict[max_key]
    else:
        pwr = 5
    if comb_num == 1:
        res = [pwr, 6]
    elif comb_num == 2:
        if max_val == 4:
            res = [pwr, 5]
        else:
            res = [pwr, 4]
    elif comb_num == 3:
        if max_val == 3:
            res = [pwr, 3]
        else:
            res = [pwr, 2]
    elif comb_num == 4:
        res = [pwr, 1]
    else:
        res = [pwr, 0]
    return res


def cards_powers_list(cards: str) -> list:
    powers = []
    for card in cards:
        powers.append(len(list(card_ranks)) - card_ranks.index(card))
    return powers

res = [[],[],[],[],[],[],[]]
for item in data:
    res_indx = find_combination(list(item[0]))[1]
    comb_power = find_combination(list(item[0]))[0]
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


for item in new_res:
    for i in item:
        print(i)
print(total)