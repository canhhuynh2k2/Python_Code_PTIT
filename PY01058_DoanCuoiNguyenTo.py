from math import *
t = int(input())
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
while t > 0:
    if isPrime(int(input()[-4:])): print("YES")
    else: print("NO")
    t -= 1