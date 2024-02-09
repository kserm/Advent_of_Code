data = {}
data_str = ''

with open('input.txt', 'r') as file:
    data_str = file.read()

with open('input.txt', 'r') as file:
    item = file.readline().split(':')
    key = item[0]
    value = item[1].strip().split()
    data[key] = value
    file.readline()
    for line in file.readlines():
        if line.startswith(('s', 'w', 'f', 't', 'h', 'l')):
            key = line.split(':')[0]
            data[key] = []
        elif line.startswith(('1','2','3','4','5','6','7','8','9','0')):
            data[key].append(line.split())

data_int = list(map(int, data['seeds']))
# print(data_int)
seed_ranges = []
for i in range(0, len(data_int), 2):
    seed_ranges.append(range(data_int[i], data_int[i]+data_int[i+1]))

# for seed in seed_ranges:
#     print(seed)

seeds = list(map(int, data_str.split('\n\n')[0].strip().split(':')[1].strip().split()))
# print('seeds: ', seeds)
maps = data_str.split('\n\n')[1:]
maps_list = [line.splitlines()[1:] for line in maps]
new_maps_list = []
for item in maps_list:
    tmp = []
    for i in item:
        tmp.append(list(map(int, i.split())))
    new_maps_list.append(tmp)

# for i in new_maps_list:
#     print(i)


# for seed in seed_ranges[:1]:
#     for s in seed:
#         print(s, end=' ')

dest_range_list = []
source_range_list = []
for item in new_maps_list:
    tmp_dst = []
    tmp_src = []
    for i in item:
        tmp_dst.append(range(i[0], i[0]+i[2]))
        tmp_src.append(range(i[1], i[1]+i[2]))
    dest_range_list.append(tmp_dst)
    source_range_list.append(tmp_src)

# for i in range(len(new_maps_list)):
#     print(len(new_maps_list[i]))
# #     print(len(source_range_list[i]))
# for item in new_maps_list:
#     for i in range(len(item)):
#         print('min - ', item[i][1])
#         print('max - ', item[i][1]+item[i][2])

res = []
for seed in seed_ranges[5:]:
    print(seed)
    # min_seed_val = min(seed)
    # max_seed_val = max(seed)
    for s in seed:
        val = s
        for i in range(len(new_maps_list)):
            item = new_maps_list[i]
            for r in range(len(item)):
                # rng_min = item[r][1]
                # rng_max = item[r][1] + item[r][2]
                # if rng_min<=val<=rng_max:
                if val in source_range_list[i][r]:
                    val = item[r][0] - item[r][1] + val
                    break
        res.append(val)
            
# print(res) 
print(min(res))


# min[:5] = 2254686
# min[5:] = 95285571