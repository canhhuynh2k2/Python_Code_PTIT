t = int(input())
l = [1]*15
for x in range(2, 10): l[x] = l[x-1] * x
while t > 0:
    n = input()
    if sum([l[int(x)] for x in n]) == int(n):   print("Yes")
    else: print("No")
    t = t - 1