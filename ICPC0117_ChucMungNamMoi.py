n = int(input())
d = {}
cnt = 0
for i in range(0, n):
    s = input()
    if s not in d:
        cnt += 1
        d[s] = 1
print(cnt)