import os

data = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    id = 0
    for line in file.readlines():
        position = map(int, line.strip().split()[0].strip("p=").split(","))
        velocity = map(int, line.strip().split()[1].strip("v=").split(","))
        data.append((id, *position, *velocity))
        id += 1

wide = 101
tall = 103
steps = 100
mid_x = wide // 2
mid_y = tall // 2

def count_robots_positions(st: int):
    robots_positions = set()
    for robot in data:
        pos = (robot[1], robot[2])
        vel = (robot[3], robot[4])
        x, y = pos[0], pos[1]
        dx, dy = vel[0], vel[1]
        nx = (x + (st*dx)) % wide
        ny = (y + (st*dy)) % tall
        robots_positions.add((nx,ny))
    return len(robots_positions), robots_positions

for s in range(10000):
    rp = count_robots_positions(s)
    if rp[0] == len(data):
        print(s)
        for y in range(tall):
            for x in range(wide):
                if (x, y) in rp[1]:
                    print("*", end="")
                else:
                    print(".", end="")
            print()
        break
