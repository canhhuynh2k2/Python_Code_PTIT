import re
d = dict()
n = int(input())
lst = ""
for _ in range(n):
    lst += input() + ' '
s = re.findall('[a-zA-Z\s]+', lst)
for i in s:
    x = i.lower().split()
    for j in x:
        if j in d: d[j] += 1
        else: d[j] = 1
m = sorted(d.items(), key = lambda x: (-x[1], x[0]))
for i in m:
    print(i[0], i[1])

