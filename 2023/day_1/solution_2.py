from pprint import pprint

data = []

valid_digits = {'one': '1', 
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())

def find_dict(substr: str, inp_str: str) -> dict:
    res_dict = {}
    pos = 0
    while pos < len(inp_str):
        pos = inp_str.find(substr, pos)
        if pos == -1:
            return res_dict
        else:
            res_dict[pos] = substr
            pos += 1
    return res_dict

total = 0
digit_list = []
for i in range(len(data)):
    tmp_dict = {}
    for key, value in valid_digits.items():
        tmp_dict.update(find_dict(key, data[i]))
    for j in range(len(data[i])):
        if j in tmp_dict.keys():
            value = tmp_dict[j]
            digit_list.append(valid_digits[value])
        elif data[i][j].isdigit():
                digit_list.append(data[i][j])
    # print(digit_list)
    if len(digit_list) >= 1:
        total += int(''.join([digit_list[0],digit_list[-1]]))
        digit_list = []


print(total)