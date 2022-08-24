s = input()
k = int(input())
if len(s) % 2 == 1: s = s[:-1]
d = dict()
ok = 0
for i in range(0, len(s), 2):
    if int(s[i:i+2]) not in d:
        d[int(s[i:i+2])] = 1
    else:
        d[int(s[i:i+2])] += 1
for x in sorted(d.keys()):
    if x in d and d[x] >= k:
        print(x, d[x])
        d.pop(x)
        ok = 1
if ok == 0: print("NOT FOUND")