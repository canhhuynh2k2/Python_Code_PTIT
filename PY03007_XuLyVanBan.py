import re
s = ""
str = '[\w\s,:]+'
while True:
    try:
        s += input()
    except IOError:
        break
s = re.findall(str, s)
for y in s:
    x = y.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))