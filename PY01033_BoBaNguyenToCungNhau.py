def togePrime(n, m):
    while m != 0:
        x = n % m
        n = m
        m = x
    return n
L, R = [int(x) for x in input().split()]
for i in range(L, R+1):
    for j in range(i+1, R+1):
        if togePrime(i, j) == 1:
            for k in range(j+1, R+1):
                if togePrime(i, k) == 1 and togePrime(j, k) == 1:
                    print("({0}, {1}, {2})".format(i, j, k))