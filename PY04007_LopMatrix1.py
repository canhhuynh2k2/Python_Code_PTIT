class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        ans = []
        for i in range(len(self.matrix)):
            c = []
            for j in range(len(self.matrix)):
                d = 0
                for k in range(len(self.matrix[j])):
                    d += self.matrix[i][k] * self.matrix[j][k]
                c.append(d)
            ans.append(c)
        res = str("")
        for i in ans:
            for j in i:
                res += str(j) + " "
            res += '\n'
        return res
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        a = []
        for i in range(n):
            a.append([int(x) for x in input().split()])
        m = Matrix(a)
        print(m)