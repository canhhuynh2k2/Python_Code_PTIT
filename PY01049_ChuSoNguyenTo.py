from math import *
t = int(input())
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
while t > 0:
    n = input()
    Prime = 0
    notPrime = 0
    for x in n:
        if x == '3' or x == '2' or x == '5' or x == '7': Prime += 1
        else: notPrime += 1
    if Prime > notPrime and isPrime(len(n)): print("YES")
    else: print("NO")
    t -= 1