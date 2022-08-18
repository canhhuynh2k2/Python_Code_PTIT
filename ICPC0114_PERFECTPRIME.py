from math import *
t = int(input())
def isPrime(n):
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return 0
    return 1
while t > 0:
    n = input()
    ok = 1
    sum = 0
    for x in n:
        sum += int(x)
        if isPrime(int(x)) == 0:
            ok = 0
    if ok == 1 and isPrime(sum) == 1 and isPrime(int(n)) == 1 and isPrime(int(n[-1::-1])) == 1:
        print("Yes")
    else: print("No")
    t = t - 1