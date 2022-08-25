n = int(input())
a = list()
while len(a) < n:
    tmp = [int(x) for x in input().split()]
    a.extend(tmp)
b = list()
c = list()
for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)
b.sort()
c.sort(reverse = True)
i = 0
j = 0
for k in range(0, n):
    if a[k] % 2 == 0:
        a[k] = b[i]
        i += 1
    else:
        a[k] = c[j]
        j += 1
print(*a)