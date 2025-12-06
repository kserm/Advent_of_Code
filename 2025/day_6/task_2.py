import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    numbers = []
    actions = []
    line_lists = []
    for line in lines:
        if ("+" in line) or ("*" in line):
            actions = line.strip().split()
        else:
            numbers.append(list(line.strip("\n")))
    spaces = []
    for n in range(len(numbers)):
        spaces.append(set())
        for i in range(len(numbers[n])):
            if numbers[n][i] == " ":
                spaces[n].add(i)
    common_spaces = sorted(set.intersection(*spaces))

    new_numbers = []
    for n in range(len(numbers)):
        j = 0
        new_numbers.append([])
        for cs in common_spaces:
            tmp = []
            for i in range(j, cs):
                tmp.append(numbers[n][i])
            new_numbers[n].append(tmp)
            j = cs + 1
        new_numbers[n].append(numbers[n][common_spaces[-1] + 1 :])
    total = 0
    i = 0
    for i in range(len(new_numbers[0])):
        tmp = []
        for item in new_numbers:
            tmp.append(item[i])
        transp = list(map(list, zip(*tmp)))
        if actions[i] == "+":
            st = 0
            for t in transp:
                st += int("".join(t).strip())
            total += st
        elif actions[i] == "*":
            st = 1
            for t in transp:
                st *= int("".join(t).strip())
            total += st
    print(total)
