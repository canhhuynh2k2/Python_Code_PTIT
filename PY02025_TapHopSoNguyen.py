n, m = [int(x) for x in input().split()]
a = list([int(x) for x in input().split()])
b = list([int(x) for x in input().split()])
d = dict()
for i in a:
    d[i] = 1
for i in b:
    if i in d:
        if d[i] == 1: d[i] = 2
    else: d[i] = 3
dd = sorted(d.keys())
for i in dd:
    if d[i] == 2: print(i, end = " ")
print()
for i in dd:
    if d[i] == 1: print(i, end = " ")
print()
for i in dd:
    if d[i] == 3: print(i, end = " ")
