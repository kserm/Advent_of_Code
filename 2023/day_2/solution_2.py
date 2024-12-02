from pprint import pprint


max_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}
# red_max = 12
# green_max = 13
# blue_max = 14

data = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip())


power_sum = 0
for line in data:
    game_id = int(line.split(':')[0].split(' ')[1])
    games_list = line.split(':')[1].split(';')
    current_max = {}
    power = 1
    for game in games_list:
        for cubes in game.split(', '):
            cubes_amount = int(cubes.strip().split(' ')[0])
            cubes_color = cubes.strip().split(' ')[1]
            if current_max.get(cubes_color):
                if current_max[cubes_color] < cubes_amount:
                    current_max[cubes_color] = cubes_amount
            else:
                current_max[cubes_color] = cubes_amount
    for key, value in current_max.items():
        power *= value
    power_sum += power

print(power_sum)