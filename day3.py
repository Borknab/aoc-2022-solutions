def common_letter(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    for x in set1:
        if x in set2:
            return x

def common_letter_2(g1, g2, g3):
    set1 = set(g1)
    set2 = set(g2)
    set3 = set(g3)
    for x in set1:
        if x in set2 and x in set3:
            return x

def compute_cost(letter):
    return ord(letter) - 97 + 1 if str.islower(letter) else ord(letter) - 65 + 27

ans = 0
with open('day3.txt') as f:
    for line in f:
        m = len(line) // 2
        ans += compute_cost(common_letter(line[:m], line[m:]))

ans2 = 0
with open('day3.txt') as f:
    while True:
        g1 = f.readline()
        if not g1:
            break
        g2 = f.readline()
        g3 = f.readline()
        ans2 += compute_cost(common_letter_2(g1.strip(),g2.strip(),g3.strip()))

print(ans, ans2)