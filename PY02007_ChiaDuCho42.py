t = 10
l = []
while t > 0:
    base = input().split()
    l.extend(base)
    t = t - len(base)
d = {}
cnt = 0
for x in l:
    if int(x) % 42 not in d:
        cnt += 1
        d[int(x) % 42] = 1
print(cnt)