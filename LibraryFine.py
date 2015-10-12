__author__ = 'rfischer'



d1, m1, y1 = [int(n) for n in raw_input().split(' ')]

d2, m2, y2 = [int(n) for n in raw_input().split(' ')]


if y2 < y1:
    print 10000
elif y1 == y2:
    if m2 < m1:
        print 500 * (m1 - m2)
    elif m1 == m2:
        if d2 < d1:
            print 15 * (d1 - d2)
        else:
            print 0
    else:
        print 0
else:
    print 0



#print d1, m1, y1