def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return 1
    else:
        return 0
n = int(input())
for i in range(1,n//2+1):
    if n%i==0:
        if prime(i) and prime(n//i):
            print(i,n//i)
            break
else:
    print("-1")
    