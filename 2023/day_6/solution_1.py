time = []
record = []

with open('input.txt', 'r') as file:
    time = list(map(int, file.readline().split(':')[1].strip().split()))
    record = list(map(int, file.readline().split(':')[1].strip().split()))

res = []
for i in range(len(time)):
    case = []
    t = time[i]
    for speed in range(t):
        dist = speed*(t-speed)
        if dist > record[i]:
            case.append(dist)
    res.append(len(case))

print(res)
total = 1
for i in res:
    total *= i

print(total)