t = int(input())
for T in range(1, t+1):
    s1 = list([ x for x in input()])
    s2 = list([ x for x in input()])
    print("Test {0}: ".format(T), end = "")
    if sorted(s1) == sorted(s2):    print("YES")
    else: print("NO")