# Too lazy to write a cleaner code, had little time :P

def determine_score(op, me):
    if (op == 'A' and me == 'Y') or (op == 'B' and me == 'Z') or (op == 'C' and me == 'X'): return 6
    if (op == 'A' and me == 'X') or (op == 'B' and me == 'Y') or (op == 'C' and me == 'Z'): return 3
    return 0

def get_choice(op, strat):
    if (op == 'A' and strat == 'X'): return 'Z'
    if (op == 'A' and strat == 'Y'): return 'X'
    if (op == 'A' and strat == 'Z'): return 'Y'

    if (op == 'B' and strat == 'X'): return 'X'
    if (op == 'B' and strat == 'Y'): return 'Y'
    if (op == 'B' and strat == 'Z'): return 'Z'

    if (op == 'C' and strat == 'X'): return 'Y'
    if (op == 'C' and strat == 'Y'): return 'Z'
    if (op == 'C' and strat == 'Z'): return 'X'

def choice_factor(me):
    if (me == 'X'): return 1
    if (me == 'Y'): return 2
    return 3

def choice_factor_two(strat):
    if (strat == 'X'): return 0
    if (strat == 'Y'): return 3
    return 6

ans = 0
ans2 = 0

with open('day2.txt') as f:
    for line in f:
        ans += determine_score(line[0], line[2]) + choice_factor(line[2])
        ans2 += choice_factor_two(line[2]) + choice_factor(get_choice(line[0], line[2]))

print(ans)
print(ans2)

