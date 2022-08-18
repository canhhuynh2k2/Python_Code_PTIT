T = int(input())
l = [1]*1000005
for x in range(2, 1000001):
    if l[x] == 1:
        for y in range(x*x, 1000001, x):
            l[y] = 0
while T > 0:
    n = int(input())
    d = {}
    for x in range(2, n):
        if str(x) != str(x)[-1::-1] and l[x] == 1 and l[int(str(x)[-1::-1])] == 1 and int(str(x)[-1::-1]) < n and x not in d:
            print(x, str(x)[-1::-1], end = " ")
            d[x] = 1
            d[int(str(x)[-1::-1])] = 1
    print()
    T = T - 1