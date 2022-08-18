from math import *
P = "abcdefghijklmnopqrstuvwxyz"
t = int(input())
while t > 0:
    s1 = input()
    s2 = s1[-1::-1]
    ok = 1
    for i in range(1, len(s1)):
        if abs(P.find(s1[i]) - P.find(s1[i-1])) != abs(P.find(s2[i]) - P.find(s2[i-1])):
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t = t - 1