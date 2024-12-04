import os

data = []

mas = ["M", "A", "S"]

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        data.append([c if c in mas else "." for c in line])

def find_mas(lst: list[list]) -> int:
    res = 0
    for i in range(1, len(lst)-1):
        for j in range(1, len(lst[i])-1):
            if lst[i][j] == "A":
                if lst[i-1][j-1] == "M" and lst[i-1][j+1] == "M" and lst[i+1][j-1] == "S" and lst[i+1][j+1] == "S":
                    res += 1
                if lst[i-1][j-1] == "M" and lst[i-1][j+1] == "S" and lst[i+1][j-1] == "M" and lst[i+1][j+1] == "S":
                    res += 1
                if lst[i-1][j-1] == "S" and lst[i-1][j+1] == "S" and lst[i+1][j-1] == "M" and lst[i+1][j+1] == "M":
                    res += 1
                if lst[i-1][j-1] == "S" and lst[i-1][j+1] == "M" and lst[i+1][j-1] == "S" and lst[i+1][j+1] == "M":
                    res += 1
    return res
        
print(find_mas(data))