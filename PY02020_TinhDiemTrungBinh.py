n = int(input())
l = [float(x) for x in input().split()]
Min = min(l)
Max = max(l)
ans = 0
for i in l:
    if i == Min or i == Max: n -= 1
    else: ans += i
print("{:.2f}".format(ans / n))