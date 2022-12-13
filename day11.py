import collections

# 
# Only contains solution to Part 2, can be easilly fixed to solve Part 1 though
# 

class Operation:
    def __init__(self, op, element):
        self.op = op
        self.element = element

class Test:
    def __init__(self, var, to_monkey_true, to_monkey_false):
        self.var = var
        self.to_monkey_true = to_monkey_true
        self.to_monkey_false = to_monkey_false
    
    def __repr__(self) -> str:
        return f"Throw to {to_monkey_true} if true else {to_monkey_false}"

class Monke:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test

    def __repr__(self) -> str:
        return f"Monke with items: {self.items}"

with open("day11.txt") as f:
    lines = [str.strip(line) for line in f.readlines()]
    pointer = 1
    monkeys = []

    while pointer < len(lines):
        items = [int(x) for x in str.split(str.replace(lines[pointer], "Starting items:", ""), ", ")]
        pointer += 1

        op_parsed = str.split(str.strip(str.split(lines[pointer], "new = ")[1]), " ")
        element = op_parsed[2] if op_parsed[2] == "old" else int(op_parsed[2])
        operation = Operation(op_parsed[1], element)
        pointer += 1

        test_var = int(str.split(lines[pointer], "Test: divisible by ")[1])
        pointer += 1
        to_monkey_true = int(str.split(lines[pointer], "If true: throw to monkey ")[1])
        pointer += 1
        to_monkey_false = int(str.split(lines[pointer], "If false: throw to monkey ")[1])
        pointer += 3
        test = Test(test_var, to_monkey_true, to_monkey_false)

        items = [{2: x % 2, 3: x % 3, 5: x % 5, 7: x % 7, 11: x % 11, 13: x % 13, 17: x % 17, 19: x % 19} for x in items]
        monkeys.append(Monke(items, operation, test))

    monke_inspections = collections.defaultdict(int)
    monke_representations = {}

    for k in range(10_000):
        print(k)
        for i, monke in enumerate(monkeys):
            while monke.items != []:
                item = monke.items.pop(0)
                monke_inspections[i] += 1
                if monke.operation.op == "+":
                    if monke.operation.element == "old":
                        for k in item:
                            item[k] = item[k] + item[k]
                    else:
                        for k in item:
                            item[k] = item[k] + monke.operation.element
                if monke.operation.op == "*":
                    if monke.operation.element == "old":
                        for k in item:
                            item[k] = item[k] * item[k]
                    else:
                        for k in item:
                            item[k] = item[k] * monke.operation.element

                for k in item:
                    item[k] = item[k] % k

                worry_level = item[monke.test.var]
                throw_decision = worry_level == 0

                if throw_decision:
                    monkeys[monke.test.to_monkey_true].items.append(item)
                else:
                    monkeys[monke.test.to_monkey_false].items.append(item)

                
    
    monke_inspections = list(sorted([monke_inspections[k] for k in monke_inspections]))

    print(monke_inspections[-1] * monke_inspections[-2])

