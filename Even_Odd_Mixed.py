n = int(input())
e = 0
o = 0
l = []
while n>0:
    r = n%10
    l.append(r)
    n//=10
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
if e==len(l) and o==0:
    print("Even")
elif o==len(l) and e==0:
    print("Odd")
else:
    print("Mixed")
    