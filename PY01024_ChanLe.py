from math import *
t = int(input())
while t > 0:
    sum = 0
    s = input()
    ok = 1
    for x in range(0, len(s) - 1):
        if abs(int(s[x]) - int(s[x+1])) != 2:
            ok = 0
            break
        sum += int(s[x])
    sum += int(s[-1])
    if ok == 1 and sum % 10 == 0:
        print("YES")
    else: print("NO")
    t = t - 1
