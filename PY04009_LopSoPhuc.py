class SoPhuc:
    def __init__(self, phanthuc, phanao):
        self.phanthuc = phanthuc
        self.phanao = phanao
    def C(A, B):
        thuc = A.phanthuc + B.phanthuc
        ao = A.phanao + B.phanao
        return SoPhuc(thuc * A.phanthuc - ao * A.phanao, thuc * A.phanao + A.phanthuc * ao)
    def D(A, B):
        thuc = A.phanthuc + B.phanthuc
        ao = A.phanao + B.phanao
        return SoPhuc(thuc * thuc - ao * ao, thuc * ao + thuc * ao)
    def __str__(self):
        if self.phanao < 0:
            return "{} {} {}i".format(self.phanthuc, "-", -self.phanao)
        else:
            return "{} {} {}i".format(self.phanthuc, "+", self.phanao)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d = [int(x) for x in input().split()]
        A = SoPhuc(a, b)
        B = SoPhuc(c, d)
        print("{}, {}".format(SoPhuc.C(A, B), SoPhuc.D(A, B)))