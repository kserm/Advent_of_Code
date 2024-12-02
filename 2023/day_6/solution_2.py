time = []
record = []

with open('input.txt', 'r') as file:
    time = file.readline().split(':')[1].strip().split()
    record = file.readline().split(':')[1].strip().split()


t = int(''.join(time))
rec= int(''.join(record))
# print(t)
# print(rec)

res = []
case = []
for speed in range(t):
    dist = speed*(t-speed)
    if dist > rec:
        case.append(dist)
res.append(len(case))

print(res)
# total = 1
# for i in res:
#     total *= i

# print(total)