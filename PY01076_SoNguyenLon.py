t = int(input())
def USCLN(a, b):
    if b == 0: return a
    return USCLN(b, a % b)
while t > 0:
    print(USCLN(int(input()), int(input())))
    t -= 1