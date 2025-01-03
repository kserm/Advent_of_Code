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
            # if program[:len(result)] != result:
            #     break
            i += 2
        elif opcode == 6:
            b = a // 2**get_combo(operand)
            i += 2
        elif opcode == 7:
            c = a // 2**get_combo(operand)
            i += 2
    return result

# Program: 2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0
# 1. B = A % 8              Always [0..7]
# 2. B = B ^ 3              Always [0..7]
# 3. C = A // 2**B          [0, 3]
# 4. A = A // 8             [0, [1..7],  ]
# 5. B = B ^ B              always B = 0
# 6. B = B ^ C              [0, 3]
# 7. res = B % 8            [0, 3, 5, 5, 4, 4, 5, 1, 3, 0, 5, 7, 3, 1, 4, 2]
# 8. Go to 1. or exit

end = 8 ** 16
A = 1

while A < end:
    o = proccess_program(A, 0, 0, program)
    if o == program:
        print("Initial A: ", A)
        break
    if o == program[-len(o):]:
        A = A << 3
    A += 1
