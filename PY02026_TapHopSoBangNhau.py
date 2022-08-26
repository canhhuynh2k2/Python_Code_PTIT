n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
d1 = dict()
d2 = dict()
for x in a:
    if x not in d1: d1[x] = 1
for x  in b:
    if x not in d2: d2[x] = 1
di1 = sorted(d1.keys())
di2 = sorted(d2.keys())
if len(di1) == len(di2) and di1 == di2:
    print("YES")
else: print("NO")