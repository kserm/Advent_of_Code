import numpy as np

data = []

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

total = 0
for item in data:
    tmp_data = [list(l) for l in item.split('\n')]
    np_data = np.array(tmp_data)

    rows = np_data.shape[0]
    cols = np_data.shape[1]

    row_sep = []
    output_r = 0
    for row in range(1, rows):
        flag = False
        if row <= rows // 2:
            for i in range(row):
                a = np_data[row-i-1, :]
                b = np_data[row+i, :]
                if not np.array_equal(a, b):
                    flag = False
                    break
                else:
                    flag = True
        else:
            for i in range(rows-row):
                a = np_data[row-i-1, :]
                b = np_data[row+i, :]
                if not np.array_equal(a, b):
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            output_r = row
    total += 100 * output_r
    # for row in range(1, rows):
    #     a = np_data[row-1, :]
    #     b = np_data[row, :]
    #     if np.array_equal(a, b):
    #         row_sep.append(row)

    output_c = 0
    col_sep = []
    for col in range(1, cols):
        flag = False
        if col <= cols // 2:
            for i in range(col):
                a = np_data[:, col-i-1]
                b = np_data[:, col+i]
                if not np.array_equal(a, b):
                    flag = False
                    break
                else:
                    flag = True
        else:
            for i in range(cols-col):
                a = np_data[:, col-i-1]
                b = np_data[:, col+i]
                if not np.array_equal(a, b):
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            output_c = col
    total += output_c
        # a = np_data[:, col-1]
        # b = np_data[:, col]
        # if np.array_equal(a, b):
        #     col_sep.append(col)
    # if col_sep:
    #     print(col_sep)

print(total)
