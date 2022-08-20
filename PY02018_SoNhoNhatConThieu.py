n = int(input())
d = dict()
for x in input().split():
    if int(x) not in d:
        d[int(x)] = 1
for i in range(1, n + 2):
    if i not in d:
        print(i)
        break