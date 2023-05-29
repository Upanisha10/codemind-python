def amicable(n):
    l = []
    t = n
    while n>0:
        r=n%10
        l.append(r)
        n//=10
    cnt = 0
    for i in l:
        if i!=0 and t%i==0:
            cnt+=1
    if cnt == len(l):
        return 1
    else:
        return 0
a = int(input())
b = int(input())
for i in range(a,b+1):
    if amicable(i):
        print(i,end=" ")
            