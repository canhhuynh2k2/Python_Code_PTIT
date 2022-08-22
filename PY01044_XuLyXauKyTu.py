d = dict()
for x in input().lower().split(): d[x] = 1
for x in input().lower().split():
    if x in d: d[x] = 2
    else: d[x] = 1
c = sorted(d.items())
for x in c:
    print(x[0], end = " ")
print()
for x in c:
    if x[1] == 2: print(x[0], end = ' ')

