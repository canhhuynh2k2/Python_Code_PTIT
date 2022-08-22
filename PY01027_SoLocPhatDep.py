s = input()
if s.count('6') + s.count('8') == len(s):
    if s == '86' or s == '88' or s.count('888') > 0: print("NO")
    else: print("YES")
else: print("NO")
