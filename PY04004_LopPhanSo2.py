class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    def gcd(self, a, b):
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
    def add(self, a):
        tmp1 = self.__tu * a.getMau() + a.getTu() * self.__mau
        tmp2 = self.__mau * a.getMau()
        tmp = self.gcd(tmp1, tmp2)
        tmp1 /= tmp
        tmp2 /= tmp
        return PhanSo(tmp1, tmp2)

    def getTu(self):
        return self.__tu
    def getMau(self):
        return self.__mau
    def __str__(self):
        return "{}/{}".format(int(self.__tu), int(self.__mau))
if __name__ == "__main__":
    a, b, c, d = [int(x) for x in input().split()]
    A = PhanSo(a, b)
    B = PhanSo(c, d)
    print(A.add(B))