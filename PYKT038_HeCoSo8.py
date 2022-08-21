s = input()
while len(s) % 3 != 0: s = "0" + s
for i in range(0, len(s), 3):
    print(int(s[i]) * 4 + int(s[i+1]) * 2 + int(s[i+2]) * 1, end = "")