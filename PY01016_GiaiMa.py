t = int(input())
while t > 0:
    s = input()
    for x in range(0, len(s), 2):
        print(s[x] * int(s[x+1]), end = "")
    print()
    t = t - 1