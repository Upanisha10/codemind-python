n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            print(j-i,end=" ")
            break
    else:
        print("0",end=" ")
