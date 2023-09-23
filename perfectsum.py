def perfectsum(n):
    c=0
    x=[i for i in range(1,n+1)]
    for i in range(len(x)):
        for j in range(len(x)):
            if pow(x[i],3)+pow(x[j],2) in x:
                c=c+1

    return c
