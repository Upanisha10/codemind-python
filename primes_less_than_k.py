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
arr= list(map(int,input().split()))
k=int(input())
cnt=0
for i in arr:
    if prime(i) and i<=k:
        cnt+=1
print(cnt)