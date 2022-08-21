t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    d = dict()
    for i in l:
        d[i] = 1
    print(l[-1] - l[0] + 1 - len(d))
    t -= 1