from math import *
t = int(input())
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True
def togePrime(n, m):
    while m != 0:
        x = n % m
        n = m
        m = x
    return n
while t > 0:
    a, b = [int(x) for x in input().split()]
    x = togePrime(a, b)
    if isPrime(sum([int(y) for y in str(x)])): print("YES")
    else: print("NO")
    t = t - 1