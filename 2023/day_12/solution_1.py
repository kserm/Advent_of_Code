# 7173

import re
from itertools import combinations

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        # syms = []
        nums = list(map(int, line.strip().split()[1].split(',')))
        # for n in nums:
        # syms = line.strip().split()[0].strip('.').split('.')
        syms = line.strip().split()[0]
            
        data.append([syms, nums])

# print(data[0])
output = 0
for rec in data[1:2]:
    st = rec[0]
    nums = rec[1]
    # st = data[0][0]
    # nums = data[0][1]
    print(st, nums)

    x = 0
    new_lst = []
    for i in st:
        new_lst.append(x)
        x += 1
    lst_comb = list(combinations(new_lst, len(nums)))
    # print(lst_comb)

    res = []
    i = 0
    for n in nums:
        res.append([])
        for p in range(len(st)):
            if p < len(st) - n + 1:
                ts = st[p:]
                if n > 2:
                    pattern = '#(?:[#?]{'+str(n-2)+'})#'
                    if re.match(pattern, ts):
                        res[i].append(p)
                    else:
                        templ = '[?#]{'+f'{n}'+'}'
                        if re.match(templ, ts):
                            # print(re.match(templ, ts))
                            res[i].append(p)
                    # if p+n < len(st) and st[p+n] != '#':
                    #     res[i].append(p)
        i += 1
    print(res)


    total = []
    for item in lst_comb:
        matching_indexes = set()
        for r in res:
            for indx in r:
                if indx in item and indx not in matching_indexes:
                    # print(indx)
                    matching_indexes.add(indx)
                    break
        if len(item) == len(matching_indexes):
            l = []
            nmi = 0
            prob_match = sorted(matching_indexes)
            for i in range(len(prob_match)):
                el = prob_match[i]
                if el >= nmi:
                    l.append(el)
                nmi = el + nums[i] + 1
            if len(l) == len(prob_match):
                total.append(l)
    print(total)
    output += len(total)

print(output)

