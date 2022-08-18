n = int(input())
l = input().split()
cnt = 0
for x in range(0, len(l) - 1):
    if l[x] != l[x+1]: cnt += 1
print(cnt)