def togePrime(n, m):
    while m != 0:
        x = n % m
        n = m
        m = x
    return n
t =int(input())
while t > 0:
    s = input()
    if togePrime(int(s), int(s[-1::-1])) == 1: print("YES")
    else: print("NO")
    t = t - 1