n, m = [int(x) for x in input().split()]
a = list()
Min = 1e9
Max = -1e9
for i in range(0, n):
    b = [int(x) for x in input().split()]
    Mi = min([int(x) for x in b])
    Ma = max([int(x) for x in b])
    Min = min(Min, Mi)
    Max = max(Max, Ma)
    a.append(b)
ans = Max - Min
ok = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == ans:
            ok += 1
            if ok == 1: print(ans)
            print(f"Vi tri [{i}][{j}]")
if ok == 0: print("NOT FOUND")