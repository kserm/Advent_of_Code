import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    res = []
    batteries = [line.strip() for line in file.readlines()]
    for battery in batteries:
        start = battery[:2]
        current_max = int(start)
        for i in range(2, len(battery)):
            number = battery[i]
            if (i <= (len(battery) - 2)):
                a = int(battery[i:i+2])
                if a > current_max:
                    current_max = a
                    start = str(a)
                    continue
            n = int(start[0] + number)
            if n > current_max:
                current_max = n
        res.append(current_max)
        print(current_max, battery)
    print(sum(res))

