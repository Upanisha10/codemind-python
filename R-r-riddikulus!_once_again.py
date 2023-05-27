n,m = map(int,input().split())
arr = list(map(int,input().split()))
while m>0:
    res = arr[0]
    arr.remove(arr[0])
    arr.append(res)
    m-=1
for i in arr:
    print(i,end=" ")
