def USCLN(a, b):
    while b != 0:
        x = a % b
        a = b
        b = x
    return a
n = int(input())
l = [int(x) for x in input().split()]
l.sort()
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if USCLN(l[i], l[j]) == 1: print(l[i], l[j])