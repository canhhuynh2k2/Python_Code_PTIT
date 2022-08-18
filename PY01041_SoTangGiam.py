t = int(input())
while t > 0:
    t -= 1
    n = input()
    i = -1
    if len(n) < 3:
        print("NO")
        continue
    for x in range(1, len(n)):
        if int(n[x]) <= int(n[x-1]):
            i = x
            break
    if i != -1:
        for x in range(i, len(n)):
            if int(n[x]) >= int(n[x-1]):
                i = -2
                break
    if i == -2: print("NO")
    else: print("YES")