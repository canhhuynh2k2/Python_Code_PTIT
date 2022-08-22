n = input()
cnt = 0
while len(n) > 1:
    x = 0
    for i in n: x += ord(i) - ord('0')
    n = str(x)
    cnt += 1
print(cnt)
