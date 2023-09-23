def lps(s):
    l=[]
    c=1
    for i in range(len(s)):
        r=""
        r+=s[i]
        for j in range(c,len(s)):
            r+=s[j]
            if r==r[::-1]:
                l.append(r)
            c=c+1
    return l
