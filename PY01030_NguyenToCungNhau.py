def togePrime(n, m):
    while m != 0:
        x = n % m
        n = m
        m = x
    return n
n, k = [int(x) for x in input().split()]
cnt = 0
for x in range(10**(k-1), 10**k):
    if togePrime(x, n) == 1:
        print(x, end = " ")
        cnt += 1
        if cnt == 10:
            cnt = 0
            print()