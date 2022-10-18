import re
n = int(input())
lst = list()
for _ in range(n):
    s = input()
    l = re.findall('[0-9]+', s)
    lst.extend(l)
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst.sort()
for x in lst:
    print(x)