while True:
    n = int(input())
    if n == 0: break
    a = list()
    for i in range(0, n):
        a.append(int(input()))
    Max = max([x for x in a])
    Min = min([x for x in a])
    if Max == Min: print("BANG NHAU")
    else: print(Min, Max)
