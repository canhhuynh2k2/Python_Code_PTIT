n = int(input())
i = 1
d = dict()
s = input()
d[s] = 0
while i < n:
    ss = input()
    if ss == "":
        s = input()
        d[s] = 0
        i += 1
    else:
        d[s] += 1
    i += 1
for x in d.keys():
    print(x + ":", d[x])
