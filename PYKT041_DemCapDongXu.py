n = int(input())
l = list()
ans = 0
for i in range(0, n):
    d = input()
    x = d.count('C')
    l.append(d)
    ans += x * (x-1) // 2
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if l[j][i] == 'C':
            cnt += 1
    ans += cnt * (cnt - 1) // 2
print(ans)