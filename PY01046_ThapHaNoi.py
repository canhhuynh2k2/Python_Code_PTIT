def towerHaNoi(n, start, finish, temp):
    if n == 1:
        print(start, "->", finish)
        return
    towerHaNoi(n-1, start, temp, finish)
    print(start, "->", finish)
    towerHaNoi(n-1, temp, finish, start)
n = int(input())
towerHaNoi(n, 'A', 'C', 'B')