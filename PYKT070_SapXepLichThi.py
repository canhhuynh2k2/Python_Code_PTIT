import datetime
monthi = open("MONTHI.in")
cathi = open("CATHI.in")
lichthi = open("LICHTHI.in")

class lt:
    def __init__(self, mct, ngaythi, giothi, phongthi, name, nhom, sl):
        self.mct = mct
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.phongthi = phongthi
        self.name = name
        self.nhom = nhom
        self.sl = sl
        self.times = datetime.datetime.strptime(ngaythi + ' ' + giothi, '%d/%m/%Y %H:%M')
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.ngaythi, self.giothi, self.phongthi, self.name, self.nhom, self.sl)
class ct:
    def __init__(self, ngaythi, giothi, phongthi):
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.phongthi = phongthi
class mh:
    def __init__(self, name, hinhthuc):
        self.name = name
        self.hinhthuc = hinhthuc


mmh = {}
mct = {}
id_cathi = 1

smh = int(monthi.readline())
for i in range(smh):
    x = monthi.readline().strip()
    p = mh(monthi.readline().strip(), monthi.readline().strip())
    mmh[x] = p

sct = int(cathi.readline())
for i in range(sct):
    p = ct(cathi.readline().strip(), cathi.readline().strip(), cathi.readline().strip())
    mct[f'C{str(id_cathi).zfill(3)}'] = p
    id_cathi += 1

slt = int(lichthi.readline())

a = []
for i in range(slt):
    ls = lichthi.readline().split()
    Cathi = mct[ls[0]]
    Monhoc = mmh[ls[1]]
    a.append(lt(ls[0], Cathi.ngaythi, Cathi.giothi, Cathi.phongthi, Monhoc.name, ls[2], ls[3]))

a.sort(key= lambda x: (x.times, x.mct))

for x in a:
    print(x)