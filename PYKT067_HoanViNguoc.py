t = int(input())
n = 0
a = [0] * 20
b = [0] * 20
ans = []
def Try(i):
    for j in range(n, 0, -1):
        if b[j] == 0:
            b[j] = 1
            a[i] = j
            if i == n:
                s = ""
                for d in range(1, n+1):
                    s += str(a[d])
                ans.append(s)
            else: Try(i+1)
            b[j] = 0
while t > 0:
    n = int(input())
    ans.clear()
    Try(1)
    print(len(ans))
    for x in ans:
        print(x, end = " ")
    print()
    t -= 1