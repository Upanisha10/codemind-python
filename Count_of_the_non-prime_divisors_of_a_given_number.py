def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return 0
    else:
        return 1
n = int(input())
cnt = 0
for i in range(1,n+1):
    if n%i==0 and prime(i):
        cnt+=1
print(cnt)