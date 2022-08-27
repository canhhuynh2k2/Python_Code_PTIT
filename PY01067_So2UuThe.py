import queue
t = int(input())
while t > 0:
    n = int(input())
    q = queue.Queue()
    q.put("1")
    q.put("2")
    d = 0
    while q.qsize():
        a = q.get()
        b = a.count("2")
        if b > len(a) - b:
            print(a, end = " ")
            d += 1
            if d == n:
                break
        q.put(a + "0")
        q.put(a + '1')
        q.put(a + '2')
    print()
    t -= 1