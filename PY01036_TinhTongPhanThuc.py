t = int(input())
while t > 0:
    n = int(input())
    if n % 2 == 1: print("{:.6f}".format(sum([1 / float(x) for x in range(1, n+1, 2)])))
    else: print("{:.6f}".format(sum([1 / float(x) for x in range(2, n+1, 2)])))
    t = t - 1