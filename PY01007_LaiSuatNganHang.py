t = int(input())
while t > 0:
    n, x, m = [float(x) for x in input().split()]
    cnt = 1
    x /= 100
    while n * x + n < m:
        cnt += 1
        n = n * x + n
    print(cnt)
    t = t - 1