from datetime import datetime
class CaThi:
    def __init__(self, ma, ngay, gio, maphong):
        self.ma = "C{:03d}".format(ma)
        self.ngay = ngay.strip()
        self.gio = gio.strip()
        self.maphong = maphong.strip()
        self.d = datetime(int(ngay[6:10]), int(ngay[3:5]), int(ngay[0:2]), int(gio[0:2]), int(gio[3:]))
    def __str__(self):
        return "{} {} {} {}".format(self.ma, self.ngay, self.gio, self.maphong)
if __name__ == "__main__":
    f = open("CATHI.in", "r")
    n = int(f.readline())
    lst = list()
    for i in range(n):
        lst.append(CaThi(i + 1, f.readline(), f.readline(), f.readline()))
    lst.sort(key = lambda x : (x.d, x.ma))
    for x in lst:
        print(x)