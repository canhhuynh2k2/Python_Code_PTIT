n = input()
while len(n) > 1:
    s1 = n[0:len(n)//2]
    s2 = n[len(n)//2: len(n)]
    n = str(int(s1) + int(s2))
    print(n)