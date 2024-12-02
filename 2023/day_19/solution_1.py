with open('input.txt') as file:
    data = file.read().split('\n\n')
    workflows = [l for l in data[0].strip().split('\n')]
    wf_dict = {}
    for item in workflows:
        key = item.split('{')[0]
        val = item.split('{')[1][:-1].split(',')
        wf_dict[key] = val
    parts = [p.strip('{').strip('}').split(',') for p in data[1].strip().split('\n')]


accepted = []

def split_rule(st: str, ch: chr) -> tuple:
    if ch in st:
        label = st.split(ch)[0]
        value = int(st.split(ch)[1].split(':')[0])
        rule = st.split(ch)[1].split(':')[1]
        return (label, value, rule)

def parse_wf(parts: list):
    p_dict = {p.split('=')[0]: int(p.split('=')[1]) for p in parts}
    start = wf_dict['in']
    rule = None
    for item in start:
        if '>' in item:
            l, v, r = split_rule(item, '>')
            if p_dict[l] > v:
                # print(item, p_dict, r)
                rule = r
                break
        elif '<' in item:
            l, v, r = split_rule(item, '<')
            if p_dict[l] < v:
                # print(item, p_dict, r)
                rule = r
                break
        else:
            # print(item, p_dict, r)
            rule = item
            # break
    # print(wf_dict[rule])
        # break
    while rule != 'A' or 'R':
        for item in wf_dict[rule]:
            if '>' in item:
                l, v, r = split_rule(item, '>')
                if p_dict[l] > v:
                    # print(item, p_dict, r)
                    rule = r
                    break
            elif '<' in item:
                l, v, r = split_rule(item, '<')
                if p_dict[l] < v:
                    # print(item, p_dict, r)
                    rule = r
                    break
            else:
                # print(item, p_dict, r)
                rule = item
                # break
        if rule == 'R':
            break
        elif rule == 'A':
            accepted.append(p_dict)
            break
        # print(rule)
        # break
                

    
    

# print(wf_dict['in'])
for part in parts:
    parse_wf(part)

# print(accepted)
total = 0
for item in accepted:
    total += sum(item.values())

print(total)