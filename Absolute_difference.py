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
arr = list(map(int,input().split()))
s=1
su=1
for i in arr:
    if prime(i):
        s *= i
    else:
        su *= i
print(abs(s-su))