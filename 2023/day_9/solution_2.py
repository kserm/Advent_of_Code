data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append([int(i) for i in line.split()])



total = 0
for item in data:
    tmp_data = item
    flag = True
    res = []
    prev = []
    res.append(tmp_data[0])
    while flag:
        zeros = 0
        for el in tmp_data:
            if el == 0:
                zeros += 1
        if zeros == len(tmp_data):
            flag = False
        tmp_list = []
        for i in range(len(tmp_data)-1):
            if not flag:
                break
            a = tmp_data[i]
            b = tmp_data[i+1]
            tmp_list.append(b-a)
        if tmp_list:
            res.append(tmp_list[0])
            tmp_data = tmp_list
    prev.append(res[-1])
    for i in res[-2::-1]:
        prev.append(i - prev[-1])
    total += prev[-1]

print(total)