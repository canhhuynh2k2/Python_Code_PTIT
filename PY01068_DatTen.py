a = [0]*25
n, k = [int(x) for x in input().split()]
h = 0
s = [x for x in input().split()]
res = []
d = dict()
def Try(i):
    for j in range(a[i-1] + 1, h-k+i+1):
        a[i] = j
        if i == k:
            for d in range(1, k+1):
                print(res[a[d]-1], end = " ")
            print()
        else: Try(i+1)
for x in s:
    if x not in d:
        d[x] = 1
        res.append(x)
        h += 1
res.sort()
Try(1)
