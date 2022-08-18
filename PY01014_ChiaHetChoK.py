a, K, N = [int(x) for x in input().split()]
b = K - (a % K)
if b == 0: b += K
if a + b > N:
    print(-1)
else:
    while a + b <= N:
        print(b, end = " ")
        b = b + K
