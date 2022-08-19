t = int(input())
while t > 0:
    n = int(input())
    l = list([int(x) for x in input().split()])
    d = dict()
    ans = 0
    Max = 0
    l.sort()
    for x in l:
        if x not in d: d[x] = 1
        else: d[x] = d[x] + 1
        if d[x] > Max:
            Max = d[x]
            ans = x
    if Max > n // 2: print(ans)
    else: print("NO")
    t -= 1