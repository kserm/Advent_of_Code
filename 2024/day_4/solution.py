import os

data = []

xmas = ["X", "M", "A", "S"]

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    for line in file.readlines():
        data.append([c if c in xmas else "." for c in line])

def find_xmas(lst: list[list]) -> int:
    res = 0
    max_indx_x = len(lst[0]) - 1
    max_indx_y = len(lst) - 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j <= max_indx_x - 3:
                if lst[i][j] == "X" and lst[i][j+1] == "M" and lst[i][j+2] == "A" and lst[i][j+3] == "S":
                    res += 1
            if j >= 3:
                if lst[i][j] == "X" and lst[i][j-1] == "M" and lst[i][j-2] == "A" and lst[i][j-3] == "S":
                    res += 1
            if i <= max_indx_y - 3:
                if lst[i][j] == "X" and lst[i+1][j] == "M" and lst[i+2][j] == "A" and lst[i+3][j] == "S":
                    res += 1
            if i >= 3:
                if lst[i][j] == "X" and lst[i-1][j] == "M" and lst[i-2][j] == "A" and lst[i-3][j] == "S":
                    res += 1
            if (i <= max_indx_y - 3) and (j <= max_indx_x - 3):
                if lst[i][j] == "X" and lst[i+1][j+1] == "M" and lst[i+2][j+2] == "A" and lst[i+3][j+3] == "S":
                    res += 1
            if (i >= 3) and (j <= max_indx_x - 3):
                if lst[i][j] == "X" and lst[i-1][j+1] == "M" and lst[i-2][j+2] == "A" and lst[i-3][j+3] == "S":
                    res += 1
            if (i <= max_indx_y - 3) and (j >= 3):
                if lst[i][j] == "X" and lst[i+1][j-1] == "M" and lst[i+2][j-2] == "A" and lst[i+3][j-3] == "S":
                    res += 1
            if (i >= 3) and (j >= 3):
                if lst[i][j] == "X" and lst[i-1][j-1] == "M" and lst[i-2][j-2] == "A" and lst[i-3][j-3] == "S":
                    res += 1
    return res
        
print(find_xmas(data))