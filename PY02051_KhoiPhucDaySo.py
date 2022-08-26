n = int(input())
a = []
ans = [0] * n
for i in range(0, n):
    b = [int(x) for x in input().split()]
    a.append(b)
if n == 2:
    print(1, a[0][1] - 1)
else:
    ans[n-1] = (a[n-2][n-1] + a[n-3][n-1] - a[n-3][n-2]) // 2
    for i in range(0, n-1):
        ans[i] = a[i][n-1] - ans[n-1]
    for i in range(0, n):
        print(ans[i], end = ' ')