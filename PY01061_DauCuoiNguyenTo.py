from math import *
t = int(input())
def isPrime(n):
    if n < 2: return false
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
while t > 0:
    n = input()
    if isPrime(int(n[0:3])) and isPrime(int(n[-3:])): print("YES")
    else: print("NO")
    t -= 1