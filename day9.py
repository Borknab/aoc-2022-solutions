def are_adjacent(p1, p2):
    return abs(p1[0] - p2[0]) in [0, 1] and abs(p1[1] - p2[1]) in [0, 1]

# 
# Part 1
# 

with open('day9.txt') as f:
    tail = [0, 0]
    head = [0, 0]
    visited = set()
    visited.add((0,0))

    for line in f:
        sp = str.split(str.strip(line), " ")
        dir, amount = sp[0], int(sp[1])
        for i in range(amount):
            if dir == "R": head[1] += 1
            if dir == "L": head[1] -= 1
            if dir == "U": head[0] += 1
            if dir == "D": head[0] -= 1

            # Case 1: overlap
            if tail == head: continue

            # Case 2: adjacent
            if are_adjacent(tail, head): continue

            # Case 3: adjacent to adjacent
            if head[0] == tail[0]:
                if dir == "R": tail[1] += 1
                elif dir == "L": tail[1] -= 1
            elif head[1] == tail[1]:
                if dir == "U": tail[0] += 1
                elif dir == "D": tail[0] -= 1
            else:
                # Move in direction of change
                if tail[0] < head[0] and tail[1] < head[1]:
                    tail[0] += 1
                    tail[1] += 1
                elif tail[0] > head[0] and tail[1] < head[1]:
                    tail[0] -= 1
                    tail[1] += 1
                elif tail[0] > head[0] and tail[1] > head[1]:
                    tail[0] -= 1
                    tail[1] -= 1
                elif tail[0] < head[0] and tail[1] > head[1]:
                    tail[0] += 1
                    tail[1] -= 1
            visited.add((tail[0], tail[1]))
            
    print(len(visited))

# 
# Part 2
# 

with open('day9.txt') as f:
    tail = [[0, 0] for i in range(9)]
    head = [0, 0]
    visited2 = set()
    visited2.add((0,0))

    for line in f:
        sp = str.split(str.strip(line), " ")
        dir, amount = sp[0], int(sp[1])
        for i in range(amount):
            if dir == "R": head[1] += 1
            if dir == "L": head[1] -= 1
            if dir == "U": head[0] += 1
            if dir == "D": head[0] -= 1

            new_head = head

            for t in tail:
                
                # Case 1: overlap
                if t == new_head: continue

                # Case 2: adjacent
                if are_adjacent(t, new_head): 
                    new_head = t
                    continue

                # Case 3: adjacent to adjacent
                if new_head[0] == t[0]:
                    if t[1] < new_head[1]: t[1] += 1
                    else: t[1] -= 1  
                elif new_head[1] == t[1]:
                    if t[0] < new_head[0]: t[0] += 1
                    else: t[0] -= 1  
                else:
                    # Move in direction of change
                    if t[0] < new_head[0] and t[1] < new_head[1]:
                        t[0] += 1
                        t[1] += 1
                    elif t[0] > new_head[0] and t[1] < new_head[1]:
                        t[0] -= 1
                        t[1] += 1
                    elif t[0] > new_head[0] and t[1] > new_head[1]:
                        t[0] -= 1
                        t[1] -= 1
                    elif t[0] < new_head[0] and t[1] > new_head[1]:
                        t[0] += 1
                        t[1] -= 1

                new_head = t

            visited2.add((tail[-1][0], tail[-1][1]))
            
    print(len(visited2))