n, m = [int(x) for x in input().split()]
a = []
for i in range(0, n):
    b = [int(x) for x in input().split()]
    if n < m:
        for j in range(1, m - n + 1):
            b.pop(j)
    a.append(b)
if n > m:
    for j in range(0, n - m):
        a.pop(j)
for i in range(0, min(n, m)):
    print(*a[i])
