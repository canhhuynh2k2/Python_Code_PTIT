n = int(input())
a = list([int(x) for x in input().split()])
Min = 1000000000
ans = 0
for i in range(0, len(a)):
    sum = 0
    for j in range(0, len(a)):
        if i != j:  sum += abs(a[j] - a[i])
    if sum < Min:
        Min = sum
        ans = a[i]
print(Min, ans)
