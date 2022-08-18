t = int(input())
while t > 0:
    n = input()
    ok = 1
    for x in n:
        if x != "0" and x != "1" and x != "2":
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t -= 1