ans = 0
ans2 = 0
with open('day4.txt') as f:
    for line in f:
        part1, part2 = str.split(line, ",")
        part1_sep, part2_sep = str.split(part1, "-"), str.split(part2, "-")
        start1, end1, start2, end2 = int(part1_sep[0]), int(part1_sep[1]), int(part2_sep[0]), int(part2_sep[1])
        if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1): ans += 1
        if (end1 >= start2 and start1 <= end2) or (end2 >= start1 and start2 <= end1): ans2 += 1
print(ans, ans2)