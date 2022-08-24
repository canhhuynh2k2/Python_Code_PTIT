t = int(input())
while t > 0:
    s = input()
    s = s + '.'
    ok = 1
    x = ""
    cnt = 0
    for i in s:
        if ord(i) >= 48 and ord(i) <= 57:
            x += i
        elif i == '.':
            if x == '' or (int(x) < 0 or int(x) > 255):
                ok = 0
                break
            x = ""
            cnt += 1
        else:
            ok = 0
            break
    if ok == 1 and cnt == 4: print("YES")
    else: print("NO")
    t -= 1