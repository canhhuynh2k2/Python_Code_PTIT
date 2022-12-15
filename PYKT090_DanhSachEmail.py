a = {}
f = open('CONTACT.in')
while True:
    try:
        s = f.readline().strip().lower()
        if len(s) == 0:
            break
        a[s] = 1
    except:
        break

ls = list(a.keys())
ls.sort()
for x in ls:
    print(x)