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

# exampl: str = data[0]
# game_id = exampl.split(':')[0].split(' ')[1]
# games_list = exampl.split(':')[1].split(';')

# print(exampl.split(':'))
# print(game_id)
# print(games_list)

id_sum = 0
for line in data:
    game_id = int(line.split(':')[0].split(' ')[1])
    games_list = line.split(':')[1].split(';')
    flag = False
    for game in games_list:
        for cubes in game.split(', '):
            cubes_amount = int(cubes.strip().split(' ')[0])
            cubes_color = cubes.strip().split(' ')[1]
            if cubes_amount > max_dict[cubes_color]:
                flag = True
    if not flag:
        # print(game_id)
        id_sum += game_id

print(id_sum)
# for game in games_list:
#     for cube in game.split(', '):
#         print(cube.strip().split(' '))