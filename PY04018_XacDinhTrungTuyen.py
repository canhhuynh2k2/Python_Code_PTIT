class GiangVien:
    def __init__(self, id, ten, maXT, diemTin, diemCM):
        self.ma = "GV{:02d}".format(id)
        self.ten = ten
        if maXT[0] == 'A':
            self.monthi = "TOAN"
        elif maXT[0] == 'B':
            self.monthi = "LY"
        else:
            self.monthi = "HOA"
        diem = diemTin * 2 + diemCM
        if maXT[1] == '1':
            diem += 2.0
        elif maXT[1] == '2':
            diem += 1.5
        elif maXT[1] == '3':
            diem += 1.0
        self.diemthi = diem
        if diem >= 18.0:
            self.kqua = "TRUNG TUYEN"
        else:
            self.kqua = "LOAI"
    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.ma, self.ten, self.monthi, self.diemthi, self.kqua)
if __name__ == "__main__":
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(GiangVien(i + 1, input(), input(), float(input()), float(input())))
    lst.sort(key = lambda x : (-x.diemthi))
    for x in lst:
        print(x)