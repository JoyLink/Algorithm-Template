def countCircleColorings(p, c):
    x=[0,c]
    for i in range(1,p):
        s=x[0]
        x[0]=x[0]*(c-2)+x[1]*(c-1)
        x[1]=s
    return x[0]


