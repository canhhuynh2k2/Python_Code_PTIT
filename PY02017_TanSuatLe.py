t = int(input())
while t > 0:
    n = int(input())
    a = list([int(x) for x in input().split()])
    d = dict()
    for x in a:
        if x not in d:
            d[x] = 1
        else: d[x] += 1
    for x in d.keys():
        if d[x] % 2 == 1:
            print(x)
            break
    t -= 1