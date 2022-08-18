import re
t = int(input())
while(t > 0):
    s = input()
    ss = re.findall("[0-9]+", s)
    print(max([int(x) for x in ss]))
    t = t - 1