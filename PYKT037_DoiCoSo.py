t = int(input())
while t > 0:
    n, b = [int(x) for x in input().split()]
    l = list()
    while n != 0:
        l.append(n % b)
        n //= b
    for i in range(len(l) - 1, -1, -1):
        if l[i] > 9:
            print(str(chr(l[i] + 55)), end = '')
        else:
            print(l[i], end = '')
    print()
    t -= 1