def fac(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
t = int(input())
while t>0:
    n = int(input())
    print(fac(n))
    t-=1