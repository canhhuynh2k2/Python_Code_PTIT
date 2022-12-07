class ThoiGian:
    def __init__(self, ma, ten, giovao, giora):
        self.ma = ma
        self.ten = ten
        h1 = int(giovao[0:2])
        m1 = int(giovao[3:5])
        h2 = int(giora[0:2])
        m2 = int(giora[3:5])
        gio = 0
        phut = 0
        if h2 < h1:
            gio += 24 - h1 + h2
        else:
            gio = h2 - h1
        if m2 < m1:
            gio -= 1
            phut = 60 - m1 + m2
        else:
            phut = m2 - m1
        self.gio = gio
        self.phut = phut
    def __str__(self):
        return "{}  {} {} gio {} phut".format(self.ma, self.ten, self.gio, self.phut)
if __name__ == '__main__':
    lst = list()
    n = int(input())
    for i in range(n):
        lst.append(ThoiGian(input(), input(), input(), input()))
    lst.sort(key = lambda x : (-x.gio, -x.phut))
    for x in lst:
        print(x)