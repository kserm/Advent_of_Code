import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    res = []
    line = file.readlines()[0].strip()
    items = line.split(",")
    for item in items:
        a, b = item.split("-")
        for n in range(int(a), int(b) + 1):
            res1 = set()
            s = str(n)
            y = len(s) // 2
            for j in range(1, y+1):
                m = len(s) % j
                if m == 0:
                    flag = True
                    s1 = s[:j]
                    k = len(s) // j
                    for i in range(k):
                        i1= i*j
                        j1 = i1+j
                        s2 = s[i1:j1]
                        if s2 != s1:
                            flag = False
                            break
                    if flag:
                        res1.add(n)
            res.extend(res1)
    print(sum(res))
