t = int(input())
while t > 0:
    s = input()
    s1 = s[0:2]
    s2 = s[len(s)-2:len(s)]
    if s1 == s2:
        print("YES")
    else:   print("NO")
    t = t - 1