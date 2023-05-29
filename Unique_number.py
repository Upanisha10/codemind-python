n = int(input())
cnt = 0
l=[]
while n>0:
    r=n%10
    l.append(r)
    cnt+=1
    n//=10
s = list(set(l))
if len(s) == cnt:
    print("Unique Number")
else:
    print("Not Unique Number")