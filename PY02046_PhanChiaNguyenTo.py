from math import *
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
n = int(input())
a = list(map(int, input().split()))
b = list()
d = dict()
for x in a:
    if x not in d:
        d[x] = 1
        b.append(x)
F = [0] * (len(b) + 1)
for i in range(0, len(b)):
    F[i+1] = F[i] + b[i]
ok = 0
for i in range(0, len(b)):
    if isPrime(F[i+1]) and isPrime(F[len(b)] - F[i+1]):
        print(i)
        ok = 1
        break
if ok == 0: print("NOT FOUND")