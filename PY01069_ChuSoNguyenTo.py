import queue
n = int(input())
q = queue.Queue()
q.put("2")
q.put('3')
q.put('5')
q.put('7')
while q.qsize():
    a = q.get()
    if a.count('2') > 0 and a.count('3') > 0 and a.count('5') > 0 and a.count('7') > 0 and ord(a[-1]) % 2 != 0:
        print(a)
    if len(a) < n:
        q.put(a + "2")
        q.put(a + "3")
        q.put(a + "5")
        q.put(a + "7")