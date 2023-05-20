n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(0,n):
    s = s*2+arr[i]
print(s)