t = int(input())
while(t > 0):
    b = int(input())
    s = (input())
    ss = 0
    n = len(s)
    l = []
    for i in range(n-1, -1, -1):
        if (s[i] == '1'):
            ss += 2**(n-i-1)
    while(ss >= b):
        l.append(ss % b)
        ss //= b
    if (ss != 0): l.append(ss)
    for x in range(len(l) - 1, -1, -1):
        if(l[x] >= 10): print(str(chr(l[x] + 55)), end = "")
        else: print(l[x], end = "")
    print()
    t = t - 1
