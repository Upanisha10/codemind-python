n = int(input())
arr = list(map(int,input().split()))
s = 0
su = 0
for i in range(0,n//2):
    s+=arr[i]
print(s)
for j in range(n//2,n):
    su+=arr[j]
print(su)
