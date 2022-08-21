n = int(input())
l = list()
while n > 0:
    name = input()
    C, T = [int(x) for x in input().split()]
    l.append((C, T, name))
    n -= 1
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if l[i][0] < l[j][0]:
            l[i], l[j] = l[j], l[i]
        elif l[i][0] == l[j][0]:
            if l[i][1] > l[j][1]:
                l[i], l[j] = l[j], l[i]
            elif l[i][1] == l[j][1]:
                if l[i][2] > l[j][2]:
                    l[i], l[j] = l[j], l[i]
for x in l:
    print(x[2], x[0], x[1])