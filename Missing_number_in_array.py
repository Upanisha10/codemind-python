t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int,input().split()))
    s = sum(arr)
    nsum = (n*(n+1))//2
    print(nsum-s)
    t-=1