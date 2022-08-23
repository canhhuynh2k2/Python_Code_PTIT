t = int(input())
while t > 0:
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = dict()
    dd = dict()
    for i in a:
        if i in d: d[i] += 1
        else: d[i] = 1
    for i in b:
        if i in dd: dd[i] += 1
        else: dd[i] = 1
    c.sort()
    ok = 0
    for i in c:
        if i in d and i in dd:
            if d[i] > 0 and dd[i] > 0:
                ok = 1
                print(i, end = ' ')
                d[i] -= 1
                dd[i] -= 1
    if ok == 0: print("NO", end = "")
    print()
    t -= 1