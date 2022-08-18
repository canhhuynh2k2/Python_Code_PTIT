t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
while t > 0:
    n = input()
    sum = 0
    mul = 1
    for x in range(0, len(n)):
        if x % 2 == 0 and n[x] != '0': mul *= d[n[x]]
        elif x % 2 == 1: sum += d[n[x]]
    print(mul, sum)
    t -= 1