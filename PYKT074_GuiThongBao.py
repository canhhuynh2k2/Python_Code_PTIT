t = int(input())
while t > 0:
    s = input()
    if len(s) <= 100: print(s)
    else:
        if s[100] == ' ': print(s[0:100])
        else:
            i = 99
            while i >= 0 and s[i] != ' ': i -= 1
            print(s[0:i+1])
    t -= 1