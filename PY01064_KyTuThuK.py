t = int(input())
while t > 0:
    n, k = [int(x) for x in input().split()]
    a = []
    for i in range(1, n + 1):
        a.append(pow(2, i-1))
    for i in range(n-1, -1, -1):
        if a[i] == k:
            print(chr(i + 65))
        elif a[i] < k:
            k -= a[i]
    t -= 1