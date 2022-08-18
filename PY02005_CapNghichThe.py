n = int(input())
l = input().split()
cnt = 0
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if int(l[i]) > int(l[j]): cnt += 1
print(cnt)