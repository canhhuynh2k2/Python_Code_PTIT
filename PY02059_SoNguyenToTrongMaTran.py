from math import *
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
n, m = [int(x) for x in input().split()]
ans = -1
a = []
for i in range(0, n):
    b = [int(x) for x in input().split()]
    for j in range(0, len(b)):
        if b[j] > ans and isPrime(b[j]):
            ans = b[j]
    a.append(b)
if ans == -1: print("NOT FOUND")
else:
    print(ans)
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == ans:
                print("Vi tri [{0}][{1}]".format(i, j))