s = input()
if len(s) % 2 == 1: s = s[:-1]
d = dict()
for i in range(0, len(s), 2):
    if int(s[i:i+2]) not in d:
        d[int(s[i:i+2])] = 1
    else: d[int(s[i:i+2])] += 1
for i in range(0, len(s), 2):
    if int(s[i:i+2]) in d:
        print(int(s[i:i+2]), d[int(s[i:i+2])])
        d.pop(int(s[i:i+2]))