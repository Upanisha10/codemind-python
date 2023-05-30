def rev(n):
    rev  = 0
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    print(rev(i),end=" ")