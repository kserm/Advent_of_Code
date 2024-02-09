# 1479011877
# 973
data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append([int(i) for i in line.split()])

# tmp_data = data[0]

# tmp_list = []
# for i in range(len(tmp_data)-1):
#     a = tmp_data[i]
#     b = tmp_data[i+1]
#     tmp_list.append(b-a)
print(data[-4])

total = 0
for item in data:
    tmp_data = item
    flag = True
    res = []
    res.append(tmp_data[-1])
    print(tmp_data)
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
            res.append(tmp_list[-1])
            tmp_data = tmp_list
            print(tmp_data)

    print(res)
    semi_total = 0
    semi_total += sum(res)
    # for r in res[::-1]:
    #     semi_total += r
    print(semi_total)
    total += semi_total

print(total)