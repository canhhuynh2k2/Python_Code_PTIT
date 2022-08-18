t = int(input())
while t > 0:
    n = int(input())
    ok = 1
    for x in range(10, n, 2):
        if x == int(str(x)[-1::-1]):
            if len(str(x)) % 2 == 0 and "1" not in str(x) and "3" not in str(x) and "5" not in str(x) and "7" not in str(x) and "9" not in str(x):
                print(x, end = " ")
    print()
    t = t - 1