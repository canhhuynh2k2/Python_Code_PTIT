d = dict()
n, k = [int(x) for x in input().split()]
a = []
b = [0] * n
def Try(i):
    for j in range(b[i-1] + 1, n - k + i + 1):
        b[i] = j
        if i == k:
            for x in range(1, k+1):
                print(a[b[x] - 1], end = " ")
            print()
        else: Try(i+1)

l = input().split()
for i in range(0, n):
    if l[i] not in d:
        a.append(int(l[i]))
        d[l[i]] = 1
    else: n -= 1
a.sort()
Try(1)