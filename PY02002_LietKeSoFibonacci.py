F = [0] * 93
F[1] = 1
for i in range(2, 93):
    F[i] = F[i-1] + F[i-2]
t = int(input())
while t > 0:
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        print(F[i], end = " ")
    print()
    t -= 1