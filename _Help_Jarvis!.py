t = int(input())
while t>0:
    n = int(input())
    l=[]
    while n>0:
        r = n%10
        l.append(r)
        n//=10
    m = max(l)
    m1 = min(l)
    temp = 0
    for i in range(m1,m+1):
        if i not in l:
            temp = 1
            break
    if temp==0:
        print("YES")
    else:
        print("NO")
    t-=1
