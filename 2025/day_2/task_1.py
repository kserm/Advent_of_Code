import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    res = []
    line = file.readlines()[0].strip()
    items = line.split(",")
    for item in items:
        a, b = item.split("-")
        for n in range(int(a), int(b) + 1):
            s = str(n)
            y = len(s) // 2
            if s[:y] == s[y:]:
                res.append(n)
    print(sum(res))
            

