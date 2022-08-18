t = int(input())
while t > 0:
    s = input()
    ok = 1
    for x in s[2::2]:
        if x != s[0]:
            ok = 0
            break
    for x in s[3::2]:
        if x != s[1]:
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t -= 1