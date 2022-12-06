def unique_letters(letters): return len(set(letters)) == len(letters)

ans = 0
with open('day6.txt') as f:
    letters_seen = set()
    line = f.readline()
    for i in range(3, len(line)):
        if unique_letters([line[i], line[i - 1], line[i - 2], line[i - 3]]):
            ans = i + 1
            break
    for i in range(13, len(line)):
        if unique_letters(line[(i - 13):(i + 1)]):
            ans = i + 1
            break
print(ans)