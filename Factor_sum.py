def fac(n):
    s = 0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
s = input()
arr = []
for i in s:
    if i != ',':
        arr.append(int(i))
l = []
for i in arr:
    if fac(i) in arr:
        l.append(i)
if len(l) == 0:
    print("-1")
else:
    a = sorted(l)
    for i in a:
        print(i,end=' ')