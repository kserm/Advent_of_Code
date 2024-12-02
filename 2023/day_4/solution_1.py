data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())

total = 0
for item in data:
    score = 0
    matches = []
    card = item.split(':')[0].strip()
    winning_numbers = item.split(':')[1].split('|')[0].strip().split(' ')
    my_numbers = item.split(':')[1].split('|')[1].strip().split(' ')
    for number in my_numbers:
        if number:
            if number in winning_numbers:
                matches.append(number)
    if len(matches) > 0:
        if len(matches) == 1:
            total += 1
        else:
            score = 1
            for i in range(len(matches)-1):
                score *= 2
            total += score

print(total)    
