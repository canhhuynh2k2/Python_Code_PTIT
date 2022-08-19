from math import *
while True:
    a, b, c, d = [int(x) for x in input().split()]
    if a == b == c == d == 0: break
    cnt = 0
    while True:
        if a == b == c == d:
            print(cnt)
            break
        e = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - e)
        cnt += 1