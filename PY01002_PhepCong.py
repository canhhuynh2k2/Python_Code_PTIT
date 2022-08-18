import re
s = input()
ss = re.findall("[0-9]+", s)
if int(ss[0]) + int(ss[1]) == int(ss[2]): print("YES")
else: print("NO")