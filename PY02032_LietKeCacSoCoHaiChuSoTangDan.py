s = input()
if len(s) % 2 == 1: s = s[:-1]
d = dict()
for i in range(0, len(s), 2):
    d[int(s[i:i+2])] = 1
for x in sorted(d.keys()):
    print(x, end = " ")