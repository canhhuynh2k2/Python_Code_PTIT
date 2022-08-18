t =int(input())
def solve(n):
    if len(n) == 1: return True
    if len(n) % 2 == 0 or n[0] == n[1]: return False
    for x in range(2, len(n), 2):
        if n[x] != n[0]: return False
    return True
while t > 0:
    if solve(input()): print("YES")
    else: print("NO")
    t -= 1