from math import *
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
n, m = [int(x) for x in input().split()]
a = []
for i in range(0, n):
    a.append([1 if isPrime(int(x)) else 0 for x in input().split()])
for x in a:
    print(*x)