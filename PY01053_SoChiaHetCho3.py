t = int(input())
d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
while t > 0:
    s = input()
    sum = 0
    for x in s:
       sum += d[x]
    if sum % 3 == 0: print("YES")
    else: print("NO")
    t -= 1