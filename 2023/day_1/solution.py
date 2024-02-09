data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())


total = 0
digit_list = []
for item in data:
    for char in item:
        if char.isdigit():
            digit_list.append(char)
    if len(digit_list) >= 1:
        total += int(''.join([digit_list[0],digit_list[-1]]))
        digit_list = []

print(total)