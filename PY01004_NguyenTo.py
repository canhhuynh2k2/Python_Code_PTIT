from math import *

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
    if n == 1: return True
    return False
t = int(input())
while t > 0:
    n = int(input())
    ok = 1
    cnt = 1
    for x in range(2, n):
        if togePrime(x, n): cnt += 1
    if isPrime(cnt): print("YES")
    else: print("NO")
    t= t - 1