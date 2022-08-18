t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
while t > 0:
    n = input()
    sum = 0
    mul = 1
    cnt = 0
    for x in range(0, len(n)):
        if x % 2 == 0: sum += d[n[x]]
        else:
            if n[x] == '0': cnt += 1
            else: mul *= d[n[x]]
    if cnt == len(n) // 2: print("{0} {1}".format(sum, 0))
    else: print("{0} {1}".format(sum, mul))
    t -= 1