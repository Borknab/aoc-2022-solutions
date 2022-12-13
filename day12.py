class GridItem:
    def __init__(self, row, col, value, dist):
        self.row = row
        self.col = col
        self.value = value
        self.dist = dist

def is_valid(row, col, previous_value, grid, visited):
    if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and visited[row][col] == False:
        item = grid[row][col]

        if item.value == "a" and previous_value == "b": return True
        if previous_value == "E": 
            return item.value == "z"
        if item.value == "E": return False
        return ord(previous_value) - ord(item.value) <= 1

    return False

with open("day12.txt") as f:
    grid = []
    pointer = 0
    start_item = None
    for line in f:
        grid.append([])
        for i, c in enumerate(str.strip(line)):
            if c == "E":
                start_item = GridItem(pointer, i, c, 0)
                grid[pointer].append(start_item)
            else:
                grid[pointer].append(GridItem(pointer, i, c, 0))
        pointer += 1
    
    visited = [[False for c in line] for line in grid]
    visited[start_item.row][start_item.col] = True
    queue = [start_item]

    ans = 0
    debug = 0
    while (len(queue)) != 0:
        item = queue.pop(0)

        if item.value == "a":
           ans = item.dist
           break

        # moving up
        if is_valid(item.row - 1, item.col, item.value, grid, visited):
            next_item = grid[item.row - 1][item.col]
            queue.append(GridItem(item.row - 1, item.col, next_item.value, item.dist + 1))
            visited[item.row - 1][item.col] = True
 
        # moving down
        if is_valid(item.row + 1, item.col, item.value, grid, visited):
            next_item = grid[item.row + 1][item.col]
            queue.append(GridItem(item.row + 1, item.col, next_item.value, item.dist + 1))
            visited[item.row + 1][item.col] = True
 
        # moving left
        if is_valid(item.row, item.col - 1, item.value, grid, visited):
            next_item = grid[item.row][item.col - 1]
            queue.append(GridItem(item.row, item.col - 1, next_item.value, item.dist + 1))
            visited[item.row][item.col - 1] = True
 
        # moving right
        if is_valid(item.row, item.col + 1, item.value, grid, visited):
            next_item = grid[item.row][item.col + 1]
            queue.append(GridItem(item.row, item.col + 1, next_item.value, item.dist + 1))
            visited[item.row][item.col + 1] = True
        
    print(ans)