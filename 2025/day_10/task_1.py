import os

dir_path = os.path.dirname(os.path.realpath(__file__))


with open(f"{dir_path}/input.txt", "r") as file:
    lines = file.readlines()
    masks = []
    buttons = []
    joltages = []
    for line in lines:
        m, *b, j = line.strip().split()
        masks.append(tuple(0 if c == "." else 1 for c in m.strip("[]")))
        tmp_b = []
        for item in b:
            tmp_b.append(tuple((int(i) for i in item.strip("()").split(","))))
        buttons.append(tmp_b)
        joltages.append(tuple(int(c) for c in j.strip("{}").split(",")))

    def find_button_presses(mask, button_options):
        start = [0 for _ in mask]
        visited = {tuple(start)}
        items = [[start, 0]]
        while items:
            state, score = items.pop(0)
            if state == list(mask):
                return score
            for button in button_options:
                new_state = state.copy()
                for idx in button:
                    new_state[idx] ^= 1

                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    items.append([new_state, score + 1])
        return None

    total = 0
    for i in range(len(masks)):
        r = find_button_presses(masks[i], buttons[i])
        total += r
    print(total)
