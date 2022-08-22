n = int(input())
a = list()
while True:
    inp = [int(x) for x in input().split()]
    a.extend(inp)
    if len(a) == n: break
s1 = list()
s2 = list()
for x in a:
    if x % 2 == 0: s1.append(x)
    else: s2.append(x)
s1.sort()
s2.sort(reverse = True)
j = 0
k = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = s1[j]
        j += 1
    else:
        a[i] = s2[k]
        k += 1
print(*a)