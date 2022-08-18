s = input()
cnt = 0
for x in s:
    if x.isupper():
        cnt += 1
if cnt > len(s) - cnt: print(s.upper())
else: print(s.lower())