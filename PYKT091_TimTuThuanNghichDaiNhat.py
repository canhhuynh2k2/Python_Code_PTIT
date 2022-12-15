f = open('VANBAN.in')
cnt = {}
tt = {}
pos = 0
def check(s):
    l, r = (0, len(s) - 1)
    while l <= r:
        if(s[l] != s[r]) :
            return False
        l += 1
        r -= 1
    return True
while True:
    try:
        s = f.readline().strip().upper().split()
        if len(s) == 0:
            break
        for x in s:
            if check(x) == False:
                continue
            if x not in tt.keys():
                tt[x] = pos
                pos += 1
            if x not in cnt.keys():
                cnt[x] = 1
            else :
                cnt[x] += 1
    except:
        break

a = []
for key, value in cnt.items():
    a.append((key, value, tt[key]))
a.sort(key= lambda x: (-len(x[0]), x[2]))
if len(a) > 0:
    l = len(a[0][0])
    for x in a:
        if len(x[0]) == l:
            print(x[0], x[1])