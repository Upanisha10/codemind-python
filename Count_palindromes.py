def pal(n):
    rev = 0
    temp = n
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev==temp
n=int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if pal(i):
        cnt+=1
print(cnt)