n, x = [int(i) for i in input().split()]
F = [0] * 8000
a = [0]
for i in range(2, 8000):
    if F[i] == 0:
        for j in range(i * i, 8000, i):
            F[j] = 1
        a.append(i)
for j in range(0, n+1):
    x += a[j]
    print(x, end = " ")