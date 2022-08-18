t = int(input())
while t > 0:
    n, d = [int(x) for x in input().split()]
    a = list([int(x) for x in input().split()])
    for i in range(d, n): print(a[i], end = " ")
    for i in range(0, d): print(a[i], end = " ")
    print()
    t = t - 1