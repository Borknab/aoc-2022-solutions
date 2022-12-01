# not really necessary, intentionally wanted to remember the library,
# will probably be relevant to the future exercises :)

import heapq

calories = [[]]
current_elf = 0

with open('day1.txt') as f:
    for line in f:
        if line != "\n":
            calories[current_elf].append(int(line))
        else:
            current_elf += 1
            calories.append([])

sums = list(map(lambda x: sum(x), calories))
ans1 = max(sums)

sums = list(map(lambda x: x * -1, sums))
heapq.heapify(sums)
ans2 = sums[0] + sums[1] + sums[2]

print(ans1)
print(ans2 * -1)