import os
from itertools import product

data = []

operators = ['+', '*', '||']

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        key = int(line.split(':')[0])
        values = line.split(':')[1].strip().split()
        data.append((key, values)) 

total = 0
for equation in data:
    key = equation[0]
    values = equation[1]
    repeat_times = len(values) - 1
    operators_comb = list(product(operators, repeat=repeat_times))

    for item in operators_comb:
        res = 0
        num1 = values[0]
        for i in range(len(item)):
            num2 = values[i+1]
            if item[i] == '+':
                res = int(num1)+int(num2)
            elif item[i] == '*':
                res = int(num1)*int(num2)
            elif item[i] == '||':
                res = str(num1)+num2
            num1 = res
        if str(res) == str(key):
            total += key
            break

print(total)
