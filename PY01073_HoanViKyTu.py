b = [0] * 10
def solve(i, n, s, ss):
    for x in range(0, n):
        if b[x] == 0:
            b[x] = 1
            if i == n-1: print(ss + s[x])
            else: solve(i+1, n, s, ss + s[x])
            b[x] = 0
s = input()
solve(0, len(s), s, "")