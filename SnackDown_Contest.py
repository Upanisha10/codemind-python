t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l = []
    for i in a:
        if i not in l:
            l.append(i)
    for i in b:
        if i not in l:
            l.append(i)
    temp = 0
    for i in range(1,n+1):
        if i not in l:
            temp = 1
            break
    if temp==1:
        print("NO")
    else:
        print("YES")
    t -= 1
    