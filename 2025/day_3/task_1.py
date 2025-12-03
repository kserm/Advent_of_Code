import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    res = []
    batteries = [line.strip() for line in file.readlines()]
    for battery in batteries:
        first, second = battery[:2]
        current_max = int(first + second)
        for i in range(1, len(battery)):
            n = int(battery[i])
            if (n > int(first)) and (i < len(battery) - 1):
                first = str(n)
                second = battery[i+1]
                current_max = int(first+second)
            elif n > int(second):
                second = str(n)
                current_max = int(first+second)
        res.append(current_max)

    print(sum(res))

