from math import *
s = int(input())
n = int(sqrt(s))
a = [0] * (n+2)
ans = 0
for i in range(1, n+1):
    a[i] = i
i = 2
while i * i <= n:
    if a[i] == i:
        j = i * i
        while j <= n:
            if a[j] == j:
                a[j] = i
            j += i
    i += 1
for k in range(2, n + 1):
    tmp1 = a[k]
    tmp2 = a[int(k/a[k])]
    if tmp1 * tmp2 == k and tmp2 != 1 and tmp1 != tmp2:
        ans += 1
    elif a[k] == k:
        if int(pow(k, 8)) <= s:
            ans += 1
print(ans)