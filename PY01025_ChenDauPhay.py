s = input()
ans = ""
cnt = 0
for x in range(len(s) - 1, -1, -1):
    cnt += 1
    ans = s[x] + ans
    if cnt == 3:
        ans = "," + ans
        cnt = 0
if ans[0] == ',': print(ans[1:])
else: print(ans)