t = int(input())
while t > 0:
    n = input()
    y = n[-1]
    for x in range(len(n) - 1, 0, -1):
        if int(y) >= 5:
            y = int(n[x-1]) + 1
        else:
            y = int(n[x-1])
    print( str(y) + "0" * (len(n) - 1))
    t = t - 1