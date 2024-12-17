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

def proccess_program(a, b, c: int, pr: list) -> list:
    def get_combo(num: int) -> int:
        if num in range(4):
            return num
        elif num == 4:
            return a
        elif num == 5:
            return b
        elif num == 6:
            return c
        return -1
    result = []
    i = 0
    
    while i < len(pr):
        opcode = pr[i]
        operand = pr[i+1]
        if opcode == 0:
            a = a // 2**get_combo(operand)
            i += 2
        elif opcode == 1:
            b = b ^ operand
            i += 2
        elif opcode == 2:
            b = get_combo(operand) % 8
            i += 2
        elif opcode == 3:
            if a != 0:
                i = operand
            else:
                i += 2
        elif opcode == 4:
            b = b ^ c
            i += 2
        elif opcode == 5:
            out = get_combo(operand) % 8
            result.append(out)
            if len(result) == len(program):
                if result[-1] == program[-1]:
                    print(a)
            i += 2
        elif opcode == 6:
            b = a // 2**get_combo(operand)
            i += 2
        elif opcode == 7:
            c = a // 2**get_combo(operand)
            i += 2
    return result
