data = []

with open('input.txt') as file:
    for line in file.readlines():
        data = line.strip().split(',')

boxes = {}

def calc_hash(s: str) -> int:
    v = 0
    m = 17
    for c in s:
        code = ord(c)
        v += code
        v *= m
        v = v % 256
    return v

total = 0
for i in data:
    if '=' in i:
        lens_to_add = i.split('=')
        box_number = calc_hash(lens_to_add[0])
        if boxes.get(box_number):
            index = -1
            for lens in boxes[box_number]:
                if lens[0] == lens_to_add[0]:
                    index = boxes[box_number].index(lens)
                    break
                else:
                    continue
            if index != -1:
                boxes[box_number][index] = lens_to_add
            else:
                boxes[box_number].append(lens_to_add)
        else:
            boxes[box_number] = [lens_to_add]
    elif '-' in i:
        lens_to_del = i.split('-')
        box_number = calc_hash(lens_to_del[0])
        if boxes.get(box_number):
            for lens in boxes[box_number]:
                if lens[0] == lens_to_del[0]:
                    index = boxes[box_number].index(lens)
                    del boxes[box_number][index]

for item in sorted(boxes.items()):
    if item[1]:
        a = 1 + item[0]
        for i in range(len(item[1])):
            b = i + 1
            c = int(item[1][i][1])
            total += a * b * c
print(total)

