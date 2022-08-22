F = [0] * 1005
F[0] = 1
F[1] = 1
for i in range(2, 1005):
    if F[i] == 0:
        for j in range(i * i, 1005, i):
            F[j] = 1
n = int(input())
a = list([int(x) for x in input().split()])
b = list()
for x in a:
    if F[x] == 0: b.append(x)
b.sort()
j = 0
for i in range(0, len(a)):
    if F[a[i]] == 0:
        a[i] = b[j]
        j += 1
print(*a)