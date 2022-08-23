n, m = [int(x) for x in input().split()]
a = list(map(int, input().split()))
d = dict()
for x in a:
    if x in d: d[x] += 1
    else: d[x] = 1
dd = sorted(d.values())
Max = 0
tmp = 1000000
if len(dd) == 0 or dd[0] == dd[len(dd) - 1]: print("NONE")
else:
    for i in range(len(dd) - 1, -1, -1):
        if dd[len(dd)-1] != dd[i]:
            Max = dd[i]
            break
    for x in a:
        if d[x] == Max and x < tmp:
            tmp = x
    print(tmp)