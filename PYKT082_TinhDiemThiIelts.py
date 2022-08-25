s = {(39, 40) : 9.0, (37, 38) : 8.5, (35, 36): 8.0, (33, 34):7.5, (30, 32):7.0,
     (27, 29):6.5, (23, 26):6.0, (20, 22):5.5, (16, 19):5.0, (13, 15):4.5, (10, 12):4.0,
     (7, 9) : 3.5, (5, 6):3.0, (3, 4):2.5}
t = int(input())
while t > 0:
    ss = [x for x in input().split()]
    a = int(ss[0])
    b = int(ss[1])
    ans = 0.0
    for x in s.keys():
        if a >= x[0] and a <= x[1]:
            ans += s[x]
        if b >= x[0] and b <= x[1]:
            ans += s[x]
    ans += float(ss[2]) + float(ss[3])
    ans /= 4
    if int(str(ans)[2:4]) < 25: print(str(int(ans)) + ".0")
    elif int(str(ans)[2:4]) >= 25 and int(str(ans)[2:4]) < 75: print(str(int(ans)) + ".5")
    else: print(str(int(ans) + 1) + ".0")
    t -= 1