import os

ABC = []
program = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/input.txt", "r") as file:
    lst = file.read().strip().split("\n\n")
    for i in lst[0].strip().split("\n"):
        ABC.append(int(i.split(":")[1].strip()))
    program = [int(c) for c in lst[1].split(":")[1].strip().split(",")]

A, B, C = ABC

def get_combo(num: int) -> int:
    if num in range(4):
        return num
    elif num == 4:
        return A
    elif num == 5:
        return B
    elif num == 6:
        return C
    return -1

result = []
i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i+1]
    if opcode == 0:
        A = A // 2**get_combo(operand)
        i += 2
    elif opcode == 1:
        B = B ^ operand
        i += 2
    elif opcode == 2:
        B = get_combo(operand) % 8
        i += 2
    elif opcode == 3:
        if A != 0:
            i = operand
        else:
            i += 2
    elif opcode == 4:
        B = B ^ C
        i += 2
    elif opcode == 5:
        out = get_combo(operand) % 8
        result.append(str(out))
        i += 2
    elif opcode == 6:
        B = A // 2**get_combo(operand)
        i += 2
    elif opcode == 7:
        C = A // 2**get_combo(operand)
        i += 2

print(",".join(result))

