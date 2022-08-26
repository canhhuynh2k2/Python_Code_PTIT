n = int(input())
a = []
d = dict()
while len(a) < n:
    b = [int(x) for x in input().split()]
    for x in b:
        d[x] = 1
    a.extend(b)
ok = 0
for i in range(1, a[n-1] + 1):
    if i not in d:
        ok = 1
        print(i)
if ok == 0: print("Excellent!")