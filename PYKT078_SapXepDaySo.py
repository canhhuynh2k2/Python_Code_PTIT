t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()]
    l = list(map(int, input().split()))
    i = -1
    Max = -1000000005
    for j in range(0, n):
        if l[j] > Max:
            Max = l[j]
            i = j
    l.insert(i, m)
    a = []
    i = 0
    while i <= n:
        if l[i] < 0:
            a.append(l[i])
            l.pop(i)
            n -= 1
        else: i += 1
    a.extend(l)
    print(*a)
    t -= 1