n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
t = int(input())
cnt = 0
for i in range(0,n):
    if a[i]<=t and b[i]>=t:
        cnt+=1
print(cnt)