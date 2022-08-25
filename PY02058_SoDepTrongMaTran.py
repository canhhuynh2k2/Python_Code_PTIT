n, m = [int(x) for x in input().split()]
Max = -1
Min = 1000000
a = []
for i in range(0, n):
    b = [int(x) for x in input().split()]
    Max = max(Max, max([x for x in b]))
    Min = min(Min, min([x for x in b]))
    a.append(b)
ans = Max - Min
ok = 0
for i in range(0, n):
    for j in range(0, m):
        if a[i][j] == ans:
            if ok == 0: print(ans)
            ok = 1
            print("Vi tri [{0}][{1}]".format(i, j))
if ok == 0: print("NOT FOUND")