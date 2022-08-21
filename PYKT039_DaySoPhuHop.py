t = int(input())
while t > 0:
    n = int(input())
    a = list([int(x) for x in input().split()])
    b = list([int(x) for x in input().split()])
    a.sort()
    b.sort()
    ok = 1
    for i in range(0, n):
        if a[i] > b[i]:
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t -= 1