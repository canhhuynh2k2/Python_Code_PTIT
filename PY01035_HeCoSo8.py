s = input()
while len(s) % 3 != 0:
    s = "0" + s
for i in range(0, len(s), 3):
    print((ord(s[i]) - 48) * 4 + (ord(s[i+1]) - 48) * 2 + (ord(s[i+2]) - 48) * 1, end = "")