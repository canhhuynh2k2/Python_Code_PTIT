t = int(input())
while t > 0:
    n = int(input())
    for x in range(2, n, 2):
        s = str(x)
        if len(s) % 2 == 0 and s == s[-1::-1] and '1' not in s and '3' not in s and '5' not in s and '7' not in s and '9' not in s:
            print(x, end = " ")
    print()
    t -= 1