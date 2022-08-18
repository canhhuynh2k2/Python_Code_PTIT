P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    l = input().split()
    if l[0] == "0": break
    k, s = l[0], l[1]
    ans = ""
    for x in range(0, len(s)):
        ans += P[(P.find(s[x]) + int(k)) % 28]
    print(ans[-1::-1])
