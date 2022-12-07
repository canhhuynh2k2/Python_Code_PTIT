from datetime import datetime
class HoaDon:
    def __init__(self, id, ten, sophong, ngaynhan, ngaytra, phatsinh):
        self.ma = "KH{:02d}".format(id)
        self.ten = ten
        date_format = "%d/%m/%Y"
        d0 = datetime.strptime(ngaynhan, date_format)
        d1 = datetime.strptime(ngaytra, date_format)
        delta = d1 - d0
        self.songay = delta.days + 1
        self.sophong = sophong
        if sophong[0] == '1':
            self.thanhtien = 25 * self.songay + phatsinh
        elif sophong[0] == '2':
            self.thanhtien = 34 * self.songay + phatsinh
        elif sophong[0] == '3':
            self.thanhtien = 50 * self.songay + phatsinh
        else:
            self.thanhtien = 80 * self.songay + phatsinh
    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.ten, self.sophong, self.songay, self.thanhtien)
if __name__ == "__main__":
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(HoaDon(i+1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
    lst.sort(key = lambda x : -x.thanhtien)
    for x in lst:
        print(x)
