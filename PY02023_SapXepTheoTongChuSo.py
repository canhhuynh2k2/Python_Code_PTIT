t = int(input())
while t > 0:
    n = int(input())
    l = [ x for x in input().split()]
    a = []
    for x in range(0, len(l)):
        s = sum([int(k) for k in l[x]])
        a.append((s, int(l[x])))
    a.sort()
    for x in a:
        print(x[1], end = " ")
    print()
    t -= 1