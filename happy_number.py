def sum(n):
    s = 0
    while n>0:
        r = n%10
        s +=(r**2)
        n//=10
    return s
def dc(n):
    cnt=0
    while n>0:
        n//=10
        cnt+=1
    return cnt
n = int(input())
res=sum(n)
while dc(res)>1:
    res = sum(res)
if res==1 or res==7:
    print("True")
else:
    print("False")
