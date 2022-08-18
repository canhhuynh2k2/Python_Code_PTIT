t = int(input())
while t > 0:
    n = input()
    x = n.count("4")
    y = n.count("7")
    if x + y == len(n):
        print("YES")
    else: print("NO")
    t = t - 1