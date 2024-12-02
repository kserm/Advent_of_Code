# 36771
import numpy as np

data = []

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

def equal_except_one(a, b):
    diff_index = np.where(a != b)[0]
    return len(diff_index) == 1

total = 0
rd = {}
cd = {}
rd_s = {}
cd_s = {}
for item in data:
    tmp_data = [list(l) for l in item.split('\n')]
    np_data = np.array(tmp_data)

    rows = np_data.shape[0]
    cols = np_data.shape[1]

    for row in range(1, rows):
        missmatch = 0
        flag = False
        if row <= rows // 2:
            for i in range(row):
                a = np_data[row-i-1, :]
                b = np_data[row+i, :]
                if not np.array_equal(a, b):
                    if missmatch != 0:
                        flag = False
                        break
                    else:
                        if equal_except_one(a, b):
                            flag = True
                            missmatch += 1
                        else:
                            flag = False
                            break
                else:
                    flag = True
        else:
            for i in range(rows-row):
                a = np_data[row-i-1, :]
                b = np_data[row+i, :]
                if not np.array_equal(a, b):
                    if missmatch != 0:
                        flag = False
                        break
                    else:
                        if equal_except_one(a, b):
                            flag = True
                            missmatch += 1
                        else:
                            flag = False
                            break
                else:
                    flag = True
        if flag and missmatch == 0:
            rd[data.index(item)] = row
        elif flag and missmatch == 1:
            rd_s[data.index(item)] = row

    for col in range(1, cols):
        missmatch = 0
        flag = False
        if col <= cols // 2:
            for i in range(col):
                a = np_data[:, col-i-1]
                b = np_data[:, col+i]
                if not np.array_equal(a, b):
                    if missmatch != 0:
                        flag = False
                        break
                    else:
                        if equal_except_one(a, b):
                            flag = True
                            missmatch += 1
                        else:
                            flag = False
                            break
                else:
                    flag = True
        else:
            for i in range(cols-col):
                a = np_data[:, col-i-1]
                b = np_data[:, col+i]
                if not np.array_equal(a, b):
                    if missmatch != 0:
                        flag = False
                        break
                    else:
                        if equal_except_one(a, b):
                            flag = True
                            missmatch += 1
                        else:
                            flag = False
                            break
                else:
                    flag = True
        if flag and missmatch == 0:
            cd[data.index(item)] = col
        elif flag and missmatch == 1:
            cd_s[data.index(item)] = col

for k, v in rd_s.items():
    total += 100*v

for k, v in cd_s.items():
    total += v

print(total)
