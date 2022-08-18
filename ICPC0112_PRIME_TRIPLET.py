T = int(input())
l = [1]*1000005
for x in range(2, 1000001):
    if l[x] == 1:
        for y in range(x*x, 1000001, x):
            l[y] = 0
while T > 0:
    n = int(input())
    cnt = 0
    for x in range(2, n-6):
        if l[x] == 1 and l[x+2] == 1 and l[x+6] == 1: cnt += 1
        elif l[x] == 1 and l[x+4] == 1 and l[x+6] == 1: cnt += 1
    print(cnt)
    T = T - 1