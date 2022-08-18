from math import *
t = int(input())
P = "abcdefghijklmnopqrstuvwxyz"
while t > 0:
    s = input()
    ss = s[-1::-1]
    ok = 1
    for i in range(0, len(s)):
        if abs(P.find(s[i]) - P.find(s[i-1])) != abs(P.find(ss[i]) - P.find(ss[i-1])):
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t -= 1