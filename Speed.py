t = int(input())
while t>0:
    n = int(input())
    arr= list(map(int,input().split()))
    cnt = 0
    for i in range(0,n-1):
        if arr[i+1] < arr[i]:
            cnt += 1
    print(cnt+1)
    t-=1
        
    