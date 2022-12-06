import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        return math.sqrt(pow((self.x - p.x), 2) + pow((self.y - p.y), 2))
class Triangle:
    def  __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __str__(self):
        c1 = self.p1.distance(self.p2)
        c2 = self.p3.distance(self.p2)
        c3 = self.p1.distance(self.p3)
        if c1 + c2 <= c3 or c1 + c3 <= c2 or c2 + c3 <= c1:
            return "INVALID"
        else:
            return "{:.3f}".format(c1 + c2 + c3)
if __name__ == "__main__":
    t = int(input())
    lst = list()
    for _ in range(t):
        while True:
            if len(lst) >= 6:
                break
            lst.extend([float(x) for x in input().split()])
        A = Triangle(Point(lst[0], lst[1]), Point(lst[2], lst[3]), Point(lst[4], lst[5]))
        print(A)
        x = lst[6:]
        lst = x