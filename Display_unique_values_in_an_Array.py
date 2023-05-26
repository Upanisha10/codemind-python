n = int(input())
l = list(map(int,input().split()))
t = 0
for i in l:
    if l.count(i) == 1:
        t = 1
        print(i,end=" ")
if t==0:
    print("-1")
