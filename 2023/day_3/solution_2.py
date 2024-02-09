import re
data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())

symbol_list = ['=', '*', '-', '+', '#', '&', '@', '%', '/', '$']

regex_template_dig = '(\d+)'
regex_template_sym = '([.]|\d|[*,=,-,+,#,&,@,%,/,$])'

digits_positions = []
symbols_positions = []
digits = []
y = 0
for item in data:
    digits = [(i.group(), i.start()) for i in re.finditer(r'\b\d+\b', item)]
    for digit in digits:
        digits_positions.append((int(digit[0]), digit[1], y))
    y += 1


y = 0
for item in data:
    symbols = [i for i in re.split(regex_template_sym, item) if i]
    for symbol in range(len(symbols)):
        if symbols[symbol] in symbol_list:
            symbols_positions.append((symbols[symbol], symbol, y))
    y += 1

res = 0
for sym in symbols_positions:
    if sym[0] == '*':
        num_list = []
        total = 1
        for digit in digits_positions:
            x_list = range(digit[1]-1, digit[1]+len(str(digit[0]))+1)
            y_list = range(digit[2]-1, digit[2]+2)
            if sym[1] in x_list and sym[2] in y_list:
                num_list.append(int(digit[0]))

        if len(num_list) > 1:
            for num in num_list:
                total *= num
            res += total

print(res)