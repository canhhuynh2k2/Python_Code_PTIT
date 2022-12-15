t = int(input())
while t > 0:
    n = int(input())
    l = list()
    l.append(99999999)
    l.extend([int(x) for x in input().split()])
    lst = [0]
    Max = []
    for i in range(1, len(l)):
        while l[i] >= l[lst[-1]]:
            lst.pop()
        Max.append(i - lst[-1])
        lst.append(i)
    print(*Max)
    t -= 1