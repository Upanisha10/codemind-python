def prime(n):
    t = 0
    for i in range(2,n//2+1):
        if n%i==0:
            t = 1
            break
    if t==0:
        return 1
    else:
        return 0
a = int(input())
b = int(input())
for i in range(a,b+1):
    if i==1:
        continue
    if prime(i):
        print(i)
    