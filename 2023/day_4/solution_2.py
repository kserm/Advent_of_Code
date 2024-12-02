data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())

cards_pile = {}

for i in range(len(data)):
    card = data[i].split(':')[0].strip()
    cards_pile[card] = 1

for i in range(len(data)):
    card = data[i].split(':')[0].strip()
    winning_numbers = data[i].split(':')[1].split('|')[0].strip().split(' ')
    winning_numbers = [num for num in winning_numbers if num]
    my_numbers = data[i].split(':')[1].split('|')[1].strip().split(' ')
    my_numbers = [num for num in my_numbers if num]
    matches = 0
    for number in my_numbers:
        if number in winning_numbers:
            matches += 1
    for j in range(matches):
            crd = data[i+j+1].split(':')[0].strip()
            cards_pile[crd] += cards_pile[card]

total_cards = 0
for card, number in cards_pile.items():
    total_cards += number

print(total_cards)
            
