t = int(input())
while t > 0:
    n = int(input())
    d = dict()
    while n > 0:
        x = int(input())
        if x not in d: d[x] = 1
        else: d[x] += 1
        n -= 1
    Max = max([x for x in d.values()])
    ans = 10005
    for i, j in d.items():
        if j == Max:    ans = min(ans, i)
    print(ans)
    t -= 1