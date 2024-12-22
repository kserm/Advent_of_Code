import os
from itertools import product

numpad = {}
dirpad = {}
codes = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    for line in file.readlines():
        codes.append(list(line.strip()))

numpad["A"] = ["0", "3"]
numpad["0"] = ["A", "2"]
numpad["1"] = ["2", "4"]
numpad["2"] = ["0", "1", "3", "5"]
numpad["3"] = ["A", "2", "6"]
numpad["4"] = ["1", "5", "7"]
numpad["5"] = ["2", "4", "6", "8"]
numpad["6"] = ["3", "5", "9"]
numpad["7"] = ["4", "8"]
numpad["8"] = ["5", "7", "9"]
numpad["9"] = ["6", "8"]

dirpad["A"] = ["^", ">"]
dirpad["^"] = ["A", "v"]
dirpad[">"] = ["A", "v"]
dirpad["v"] = ["^", "<", ">"]
dirpad["<"] = ["v"]

def find_shortest_path(spt: dict, current: str, target: str, path=None, res=None) -> list:
    if path is None:
        path = []
    if res is None:
        res = []
    path.append(current)
    if target in spt[current]:
        item = path + [target]
        res.append(item)
        if res:
            ml = min(len(r) for r in res)
            for item in res:
                if len(item) > ml:
                    res.remove(item)
        return res
    for node in spt[current]:
        if node not in path:
            find_shortest_path(spt, node, target, path[:], res)
    if res:
        ml = min(len(r) for r in res)
        for item in res:
            if len(item) > ml:
                res.remove(item)
    return res

np_map = {}
np_map["A"] = (("0", "<"), ("3", "^"))
np_map["0"] = (("A", ">"), ("2", "^"))
np_map["1"] = (("4", "^"), ("2", ">"))
np_map["2"] = (("0", "v"), ("1", "<"), ("3", ">"), ("5", "^"))
np_map["3"] = (("A", "v"), ("2", "<"), ("6", "^"))
np_map["4"] = (("1", "v"), ("5", ">"), ("7", "^"))
np_map["5"] = (("2", "v"), ("4", "<"), ("6", ">"), ("8", "^"))
np_map["6"] = (("3", "v"), ("5", "<"), ("9", "^"))
np_map["7"] = (("4", "v"), ("8", ">"))
np_map["8"] = (("5", "v"), ("7", "<"), ("9", ">"))
np_map["9"] = (("6", "v"), ("8", "<"))

dp_map = {}
dp_map["A"] = (("^", "<"), (">", "v"))
dp_map["^"] = (("A", ">"), ("v", "v"))
dp_map[">"] = (("A", "^"), ("v", "<"))
dp_map["v"] = (("^", "^"), ("<", "<"), (">", ">"))
dp_map["<"] = (("v", ">"), )

def process_nums(num_list: list) -> list:
    cur = "A"
    result = []
    for n in num_list:
        fsp = find_shortest_path(numpad, cur, n)
        sliced_list = [lst[1:] for lst in fsp]
        result.append(sliced_list)
        cur = n
    return result

def process_dirs(dirs: str) -> list:
    dir_list = list(dirs)
    cur = "A"
    result = []
    for d in dir_list:
        if cur != d:
            fsp = find_shortest_path(dirpad, cur, d)
            sliced_list = [lst[1:] for lst in fsp]
            result.append(sliced_list)
        else:
            result.append([["X"]])
        cur = d
    return result

def nums_to_dir(combinations: list) -> list:
    result = []
    for combination in combinations:
        dir_res = []
        s = "A"
        for comb in combination:
            for c in comb:
                for m in np_map[s]:
                    if c in m:
                        dir_res.append(m[1])
                s = c
            dir_res.append("A")
        item = "".join(dir_res)
        result.append(item)
    return result

def dirs_to_dir(combinations: list) -> list:
    result = []
    for combination in combinations:
        res = ""
        cur = "A"
        for comb in combination:
            for c in comb:
                for m in dp_map[cur]:
                    if c == m[0]:
                        res += m[1]
                        break
                if c != "X":
                    cur = c
            res += "A"
        result.append(res)
    return result

total = 0
for code in codes:
    visited = set()
    ml = 9999
    number_list = []
    for ch in code:
        if ch.isdigit():
            number_list.append(ch)
    number = int("".join(number_list))
    np = process_nums(code)
    np_combs = list(product(*np))
    ntp = nums_to_dir(np_combs)
    for item in ntp:
        pd = process_dirs(item)
        pd_combs = list(product(*pd))
        dtp = dirs_to_dir(pd_combs)
        for item2 in dtp:
            pd2 = process_dirs(item2)
            pd_combs2 = list(product(*pd2))
            dtp2 = dirs_to_dir(pd_combs2)
            for item3 in dtp2:
                lv3 = len(item3)
                if lv3 > ml:
                    continue
                ml = min(lv3, ml)
    total += ml * number

print(total)
