n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
avg = s//n
cnt = 0
for i in arr:
    if i<=avg:
        cnt+=1
print(cnt)