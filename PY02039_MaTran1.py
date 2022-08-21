from math import *
n = int(input())
a = []
s1 = 0
s2 = 0
for i in range(0, n):
    b = [int(x) for x in input().split()]
    s1 += sum([x for x in b[i+1:]])
    s2 += sum([x for x in b[0:i]])
k = int(input())
if abs(s1 - s2) <= k: print("YES")
else: print("NO")
print(abs(s1 - s2))