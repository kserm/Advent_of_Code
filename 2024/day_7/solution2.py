import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        key = int(line.split(':')[0])
        values = line.split(':')[1].strip().split()
        data.append((key, values)) 

def recursive_check(goal: int, numbers: list, index: int = 1, current_result: int = None) -> int:
    if current_result == None:
        current_result = numbers[0]
    if index == len(numbers):
        return goal if current_result == goal else 0
    next_number = numbers[index]
    addition = recursive_check(goal, numbers, index+1, current_result+next_number)
    if addition:
        return addition
    multiplication = recursive_check(goal, numbers, index+1, current_result*next_number)
    if multiplication:
        return multiplication
    concatinated = int(f"{current_result}{next_number}")
    concatination = recursive_check(goal, numbers, index+1, concatinated)
    if concatination:
        return concatination
    return 0

total = 0
for item in data:
    key = item[0]
    values = [int(v) for v in item[1]]
    total += recursive_check(key, values)

print(total)