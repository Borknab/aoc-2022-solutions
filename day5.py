def parse_command(c):
    s = str.split(c, " ")
    return (int(s[1]), int(s[3]), int(s[5]))

with open('day5.txt') as f:
    lines_parsed = f.readlines()
    lines = list(map(lambda x: str.strip(x), lines_parsed))
    lines.reverse()
    commands = []
    pointer = 0
    current_line = lines[pointer]

    while len(current_line) != 0:
        commands.insert(0, parse_command(current_line))
        pointer += 1
        current_line = lines[pointer]
    pointer += 1
    stack_line = str.split(lines[pointer], "  ")
    stacks = [[] for s in stack_line]
    pointer += 1
    lines_parsed.reverse()
    item_lists = lines_parsed[pointer:]
    item_lists = list(map(lambda x: x[:-1], item_lists))

    for item_list in item_lists:
        stack_pointer = 0
        last_empty = -1
        for i in range(len(item_list)):
            c = item_list[i]
            if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90):
                stacks[stack_pointer].append(c)
                stack_pointer += 1
            elif i >= 2 and i - last_empty >= 3 and c == " " and item_list[i - 1] == " " and item_list[i - 2] == " ":
                stack_pointer += 1
                last_empty = i + 1

    for c in commands:
        amount, from_s, to_s = c
        from_s -= 1
        to_s -= 1
        items_to_move = stacks[from_s][-amount:]
        items_to_move
        stacks[to_s] += items_to_move
        for c in range(amount): stacks[from_s].pop()

    ans = ""
    for s in stacks: ans += s[-1]
    print(ans)
    
            
                
