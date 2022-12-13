from functools import cmp_to_key

def right_order(x, y):
    pointer = 0
    nested_decision = True

    while pointer < max(len(x), len(y)):
        m = min(len(x), len(y))
        if pointer == m:
            if len(x) == m and len(y) == m: return "cont"
            if len(x) == m: return True
            else: return False

        left = x[pointer]
        right = y[pointer]

        if isinstance(left, int) and isinstance(right, int):
            if left < right: return True
            if left > right: return False
            else: 
                pointer += 1
                continue
        else:
            if isinstance(left, int): left = [left]
            if isinstance(right, int): right = [right]
            nested_decision = right_order(left, right)
            if nested_decision != "cont": return nested_decision

        pointer += 1

    return nested_decision

def right_order_cmp(x, y):
    if x == y: return 0
    return -1 if right_order(x, y) else 1

with open('day13.txt') as f:
    number_lists = []
    number_lists_2 = []
    pointer = 0
    lines = f.readlines()
    while pointer < len(lines):
        number_lists.append([eval(lines[pointer]), eval(lines[pointer + 1])])
        number_lists_2.append(eval(lines[pointer]))
        number_lists_2.append(eval(lines[pointer + 1]))
        pointer += 3
    number_lists_2.append([[2]])
    number_lists_2.append([[6]])

    # Part 1
    right_orders = []
    for i, pair in enumerate(number_lists):
        if right_order(pair[0], pair[1]): right_orders.append(i + 1)
    print(sum(right_orders))

    # Part 2
    right_orders_2 = []
    number_lists_2 = sorted(number_lists_2, key=cmp_to_key(right_order_cmp))
    ans2 = 1
    for i, el in enumerate(number_lists_2):
        if el == [[2]] or el == [[6]]: ans2 *= (i + 1)
    print(ans2)