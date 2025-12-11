import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    connections = {}
    for line in lines:
        key, values = line.strip().split(": ")
        connections[key] = values.split()
    start = "you"
    end = "out"
    queue = [(start, set())]
    total = 0
    while queue:
        item = queue.pop()
        key, visited = item
        visited = visited.copy()
        visited.add(key)
        values = connections[key]
        if end in values:
            total += 1
        for value in values:
            if value != end and value not in visited:
                queue.append((value, visited))
    print(total)
