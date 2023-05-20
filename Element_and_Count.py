n = int(input())
arr = list(map(int,input().split()))
l = []
c = []
for i in arr:
    if i not in l:
        l.append(i)
        c.append(arr.count(i))
for i in range(0,len(l)):
    print(l[i],c[i],end=" ")