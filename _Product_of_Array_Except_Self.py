def product(arr):
    p=1
    for i in arr:
        p*=i
    return p
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    print(product(arr)//i,end=" ")
    