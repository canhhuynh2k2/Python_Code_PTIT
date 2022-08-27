def solve(n, p):
    x = 0
    while n > 0:
        n //= p
        x += n
    return x
t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()]
    print(solve(n, m))
    t -= 1