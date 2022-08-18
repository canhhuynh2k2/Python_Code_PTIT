t = int(input())
while t > 0:
    s = input()
    s = s + "#"
    tmp = s[0]
    cnt = 0
    for x in s:
        if tmp == x: cnt += 1
        else:
            print(str(cnt) + tmp, end = "")
            tmp = x
            cnt = 1
    t = t - 1
    print()