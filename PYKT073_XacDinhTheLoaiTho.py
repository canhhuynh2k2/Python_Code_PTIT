n = int(input())
tmp = -1
ans = []
cnt = 0
while n > 0:
     l = len(input().split())
     if tmp == -1:
          tmp = l
          if tmp == 6:
               ans.append(1)
          else:
               cnt = 1
     else:
          if l == 7: cnt += 1
          if cnt == 4:
               ans.append(2)
               cnt = 0
          if l == 7 and tmp ==  6:
               tmp = 7
               cnt = 1
          elif l == 6 and tmp == 7:
               ans.append(1)
               tmp = 6
     n -= 1
print(len(ans))
for x in ans:
     print(x)