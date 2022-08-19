s = input().strip().lower()
P = "abcdefghijklmnopqrstuvwxyz"
ok = 1
for x in range(0, len(s) - 3):
    if s[x] != '_' and P.find(s[x]) == -1:
        ok = 0
        break
if ok == 1 and s[-3:] == '.py': print("yes")
else: print("no")