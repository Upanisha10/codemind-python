n = int(input())
arr = list(map(int,input().split()))
t = 0
for i in range(0,n):
    if i%2==0 and arr[i]%2!=0:
        t = 1
        break
if t==0:
    print("True")
else:
    print("False")
        