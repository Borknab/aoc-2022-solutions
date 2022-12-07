class Entry:
    def __init__(self, children, name, parent, size):
        self.children = children
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self) -> str:
        return f"Dir '{self.name}': {self.size}, with children: {self.children} and parent {self.parent}"

def dfs(dir, ans):
    dir_size = dir.size
    if len(dir.children) == 0:
        ans.append(dir.size)
        return dir.size

    for child_name in dir.children:
        dir_size += dfs(dir.children[child_name], ans)
        
    ans.append(dir_size)
    return dir_size

with open('day7.txt') as f:
    home = Entry({}, "/", None, 0)
    max_dir_size = 70_000_000
    required_space = 30_000_000
    current_dir = home
    
    for line in f:
        line = str.strip(line)
        if line.startswith("$ cd"):
            current_dir_name = str.split(line, " ")[2]
            if current_dir_name == "/":
                continue
            if current_dir_name == "..":
                current_dir = current_dir.parent
            else:
                if current_dir_name not in current_dir.children:
                    new_entry = Entry({}, current_dir_name, current_dir, 0)
                    current_dir.children[current_dir_name] = new_entry
                else:
                    current_dir = current_dir.children[current_dir_name]
        elif line.startswith("$ ls"):
            continue
        else:
            if line.startswith("dir"):
                dir_name = str.split(line, " ")[1]
                new_entry = Entry({}, dir_name, current_dir, 0)
                current_dir.children[dir_name] = new_entry
            else:
                file_size = int(str.split(line, " ")[0])
                current_dir.size += file_size
 
    results = []
    dfs(home, results)

    max_size = max(results)
    space_available = max_dir_size - max_size
    space_to_free = required_space - space_available
    ans1 = sum(list(filter(lambda x: x <= 100000, results)))
    ans2 = min(list(filter(lambda x: x >= space_to_free, results)))

    print(ans1, ans2)