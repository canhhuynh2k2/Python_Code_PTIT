t = int(input())
while t > 0:
    p, q = [x for x in input().strip().split()]
    if int(p) > int(q): p, q = q, p
    try:
    	s = input().strip().split()
    	a, b = [x for x in s]
    except:
    	a = s[0]
    	b = input().strip()
    c = a
    d = b
    a = a.replace(p, q, a.count(p))
    b = b.replace(p, q, b.count(p))
    c = c.replace(q, p, c.count(q))
    d = d.replace(q, p, d.count(q))
    print(int(c) + int(d), int(a) + int(b))
    t = t - 1