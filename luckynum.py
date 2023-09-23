def lucky(l1):
    c=1
    d=2
    i=0
    while i<len(l1):
        l1.remove(l1[c])
        l1.remove(l1[d])
        c=c+2
        d=d+3
        i=i+1
    return l1
