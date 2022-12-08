def visible_from_any_direction(i, j, value, lines):
    # constant i, start j from 0
    visible_from_left = True
    for j2 in range(0, j):
        if lines[i][j2] >= value:
            visible_from_left = False
    # constant j, start i from 0
    visible_from_top = True
    for i2 in range(0, i):
        if lines[i2][j] >= value:
            visible_from_top = False

    # constant i, start j from m - 1
    visible_from_right = True
    for j2 in range(len(lines[0]) - 1, j, -1):
        if lines[i][j2] >= value:
            visible_from_right = False

    # constant j, start i from n - 1
    visible_from_bottom = True
    for i2 in range(len(lines) - 1, i, -1):
        if lines[i2][j] >= value:
            visible_from_bottom = False

    return visible_from_left or visible_from_top or visible_from_right or visible_from_bottom

def calculate_scenic_score(i, j, value, lines):
    # constant i, start j2 from j - 1 and go to 0
    score_left = 0
    for j2 in range(j - 1, -1, -1):
        if lines[i][j2] < value:
            score_left += 1
        else:
            score_left += 1
            break

    # constant j, start i2 from i - 1 and go to 0
    score_top = 0
    for i2 in range(i - 1, -1, -1):
        if lines[i2][j] < value:
            score_top += 1
        else:
            score_top += 1
            break

    # constant i, start j2 from j + 1 and go to m
    score_right = 0
    for j2 in range(j + 1, len(lines[0])):
        if lines[i][j2] < value:
            score_right += 1
        else:
            score_right += 1
            break

    # constant j, start i2 from i + 1 and go to n
    score_bottom = 0
    for i2 in range(i + 1, len(lines)):
        if lines[i2][j] < value:
            score_bottom += 1
        else:
            score_bottom += 1
            break

    return score_left * score_top * score_right * score_bottom

with open('day8.txt') as f:
    lines = [[c for c in str.strip(line)] for line in f.readlines()]
    ans = 0
    n, m = len(lines), len(lines[0])
    max_score = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1 or visible_from_any_direction(i, j, lines[i][j], lines):
                ans += 1
            if i != 0 and j != 0 and i != n - 1 and j != m - 1:  
                max_score = max(max_score, calculate_scenic_score(i, j, lines[i][j], lines))
    print(ans, max_score)