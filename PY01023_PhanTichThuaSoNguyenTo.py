from math import *
t = int(input())
while t > 0:
    s = int(input())
    print("1 ", end = "")
    for x in range(2, int(sqrt(s)) + 1):
        cnt = 0
        while s % x == 0:
            cnt += 1
            s //= x
        if cnt != 0: print("* {0}^{1} ".format(x, cnt), end = "")
    if s != 1: print("* {0}^{1} ".format(s, 1), end = "")
    print()
    t = t - 1