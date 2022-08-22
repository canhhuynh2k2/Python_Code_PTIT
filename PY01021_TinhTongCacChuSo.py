t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
while t > 0:
    s = input()
    a = list()
    sum = 0
    for i in range(0, len(s)):
        if s[i] in d:   sum += d[s[i]]
        else: a.append(s[i])
    a.sort()
    for i in a: print(i, end = "")
    print(sum)
    t -= 1