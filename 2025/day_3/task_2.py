import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    res = []
    batteries = [line.strip() for line in file.readlines()]
    for battery in batteries:
        battery_list = list(map(int, battery))
        temp = []
        i = 0
        while True:
            temp.append(battery_list[i])
            indx = len(temp) - 1
            r = len(battery_list) + len(temp) - 12
            flag = True
            for j in range(i, r):
                if temp[indx] < battery_list[j]:
                    temp[indx] = battery_list[j]
                    i = j + 1
                    flag = False
            if flag:
                i += 1
            if r == len(battery_list):
                break
        res.append(int("".join(map(str, temp))))
    print(sum(res))
