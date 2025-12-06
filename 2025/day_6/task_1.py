import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    numbers = []
    actions = []
    line_lists = []
    for line in lines:
        line_lists.append(line.strip().split())
    for item in line_lists:
        if ("+" in item) or ("*" in item):
            actions.append(item)
        else:
            numbers.append([int(i) for i in item])
    total = 0
    for action in actions:
        i = 0
        for a in action:
            temp = 0
            if a == "+":
                temp = 0
                for n in range(len(numbers)):
                    temp += numbers[n][i]
            elif a == "*":
                temp = 1
                for n in range(len(numbers)):
                    temp *= numbers[n][i]
            total += temp
            i += 1
    print(total)
