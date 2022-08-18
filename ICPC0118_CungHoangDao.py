t = int(input())
data = {((21, 3), (19, 4)) : "Bach Duong", ((20, 4), (20, 5)) : "Kim Nguu",
        ((21, 5), (20, 6)) : "Song Tu", ((21, 6), (22, 7)) : "Cu Giai",
        ((23, 7), (22, 8)) : "Su Tu", ((23, 8), (22, 9)) : "Xu Nu",
        ((23, 9), (22, 10)) : "Thien Binh", ((23, 10), (22, 11)) : "Thien Yet",
        ((23, 11), (21, 12)) : "Nhan Ma", ((22, 12), (19, 1)) : "Ma Ket",
        ((20, 1), (18, 2)) : "Bao Binh", ((19, 2), (20, 3)) : "Song Ngu"}
while t > 0:
    d, m = [int(x) for x in input().split()]
    for x in data.keys():
        if (m == x[0][1] and d >= x[0][0]) or (m == x[1][1] and d <= x[1][0]):
            print(data[x])
            break
    t = t - 1