from math import *
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
n = int(input())
l = [int(x) for x in input().split()]
d = dict()
for i in l:
    if i not in d: d[i] = 1
    else: d[i] += 1
for i in l:
    if d[i] != 0 and isPrime(i):
        print(i, d[i])
        d[i] = 0