t = int(input())
while t > 0:
    n = input()
    ok = 1
    for i in range(0, len(n) - 1):
        if n[i] > n[i+1]:
            ok = 0
            break
    if ok == 1: print("YES")
    else: print("NO")
    t = t - 1