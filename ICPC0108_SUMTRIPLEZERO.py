t = int(input())
while t > 0:
    n = int(input())
    a = sorted(list(map(int,input().split())))
    cnt = 0
    for i in range(0, n-2):
        l = i + 1
        r = n - 1
        while l < r:
            if a[i] + a[l] + a[r] > 0: r -= 1
            elif a[i] + a[l] + a[r] < 0: l += 1
            else:
                cnt += 1
                l += 1
    print(cnt)
    t -= 1
