n = int(input())
l = [int(i) for i in input().split()]
i = 1
while(i < n):
    if((l[i] + l[i-1]) % 2 == 0):
        l.pop(i-1)
        l.pop(i-1)
        n -= 2
        if(i > 1):
            i = i - 1
    else: i = i + 1
print(len(l))
