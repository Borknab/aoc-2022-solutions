with open("day14.txt") as f:
    rocks = set()
    max_y = float("-inf")

    for line in f:
        line = str.strip(line)
        coordinates = str.split(line, " -> ")
        pointer = 0
        
        while pointer < len(coordinates) - 1:
            sp1 = str.split(coordinates[pointer], ",")
            firstx, firsty = int(sp1[0]), int(sp1[1])
    
            sp1 = str.split(coordinates[pointer + 1], ",")
            secondx, secondy = int(sp1[0]), int(sp1[1])

            rocks.add((firstx, firsty))
            max_y = max(max_y, firsty)

            if (firstx < secondx or firstx > secondx) and firsty == secondy:
                if firstx < secondx:
                    while firstx < secondx:
                        firstx += 1
                        max_y = max(max_y, firsty)
                        rocks.add((firstx, firsty))
                if firstx > secondx:
                    while firstx > secondx:
                        firstx -= 1
                        max_y = max(max_y, firsty)
                        rocks.add((firstx, firsty))

            elif (firsty < secondy or firsty > secondy) and firstx == secondx:
                if firsty < secondy:
                    while firsty < secondy:
                        firsty += 1
                        max_y = max(max_y, firsty)
                        rocks.add((firstx, firsty))
                if firsty > secondy:
                    while firsty > secondy:
                        firsty -= 1
                        max_y = max(max_y, firsty)
                        rocks.add((firstx, firsty))          

            pointer += 1

    print(max_y)
    p = (500, 0)
    original_rocks_length = len(rocks)

    while True:
        p = (500, 0)

        while True:
            if p[1] > max_y + 2: break
            
            block_down = (p[0], p[1] + 1)
            if block_down not in rocks: 
                p = block_down
                continue

            block_left_down = (p[0] - 1, p[1] + 1)
            if block_left_down not in rocks: 
                p = block_left_down
                continue

            block_right_down = (p[0] + 1, p[1] + 1)
            if block_right_down not in rocks: 
                p = block_right_down
                continue

            break

        if (500, 0) in rocks: break

        rocks.add((p[0], p[1]))

    counter = 0
    for x in rocks:
        if x[1] > max_y + 1: counter += 1

    print(len(rocks) - original_rocks_length - counter)