n = int(input())
l = list(map(int,input().split()))
t=0
for i in l:
    if i!=0 and i!=1:
        t=1
        break
if t==1:
    print("False")
else:
    print("True")