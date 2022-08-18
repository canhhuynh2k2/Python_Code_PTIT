t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
l = [1]*1000005
l[0] = 0
l[1] = 0
for x in range(2, 501):
    if l[x] == 1:
        for y in range(x*x, 501, x):
            l[y] = 0
def solve(n):
    for x in range(0, len(n)):
        if l[x] == 1 and l[d[n[x]]] == 0: return False
        elif l[x] == 0 and l[d[n[x]]] == 1: return False
    return True
while t > 0:
    if solve(input()): print("YES")
    else: print("NO")
    t -= 1

