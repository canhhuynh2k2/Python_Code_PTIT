n = int(input())
a = []
for i in range(0, n):
    b = [int(x) for x in input().split()]
    a.append(b)
k = int(input())
s1 = 0
s2 = 0
for i in range(0, len(a)):
    s1 += sum([x for x in a[i][:i]])
    s2 += sum([x for x in a[i][i+1:]])
if abs(s1 - s2) <= k: print("YES")
else: print("NO")
print(abs(s1 - s2))