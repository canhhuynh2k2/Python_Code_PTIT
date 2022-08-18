from math import *
t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True
def solve(n):
    for x in range(0, len(n)):
        if x % 2 == 0 and d[n[x]] % 2 == 1: return False
        elif x % 2 == 1 and d[n[x]] % 2 == 0: return False
    return True
while t > 0:
    s = input()
    sum = 0
    for x in s:
       sum += d[x]
    if solve(s) and isPrime(sum): print("YES")
    else: print("NO")
    t -= 1