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
            

test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
seeds = list(map(int, data_str.split('\n\n')[0].strip().split(':')[1].strip().split()))
print('seeds: ', seeds)
maps = data_str.split('\n\n')[1:]
maps_list = [line.splitlines()[1:] for line in maps]
new_maps_list = []
for item in maps_list:
    tmp = []
    for i in item:
        tmp.append(list(map(int, i.split())))
    new_maps_list.append(tmp)

for i in new_maps_list:
    print(i)

res = []
for seed in seeds:
    val = seed
    for item in new_maps_list:
        dest_range_list = []
        source_range_list = []
        for i in item:
            dest_range_list.append(range(i[0], i[0]+i[2]))
            source_range_list.append(range(i[1], i[1]+i[2]))
        for r in range(len(item)):
            if val in source_range_list[r]:
                val = item[r][0] - item[r][1] + val
                break
    res.append(val)
            
# print(res) 
print(min(res)) 

