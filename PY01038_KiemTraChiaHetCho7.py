t = int(input())
while t > 0:
    n = int(input())
    if n % 7 == 0:
        print(n)
        t = t - 1
        continue
    for x in range(0, 1000):
        n += int(str(n)[-1::-1])
        if n % 7 == 0:
            print(n)
            break
    t = t - 1