f1 = open('DATA1.in')
f2 = open('DATA2.in')

a1 = list(set(f1.read().lower().split()))
a2 = list(set(f2.read().lower().split()))
a1.sort()
a2.sort()
cnt1 = {}
cnt2 = {}
for x in a1:
    cnt1[x] = 1
for x in a2:
    cnt2[x] = 1

for x in a1:
    if x not in cnt2.keys():
        print(x, end = ' ')
print()
for x in a2:
    if x not in cnt1.keys():
        print(x, end = ' ')
print()
