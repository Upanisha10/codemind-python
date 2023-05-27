n = int(input())
arr = list(map(int,input().split()))
cnt = 0
max_count = 0
for i in range(0,n):
    if arr[i] == 0:
        cnt = 0
    else:
        cnt += 1
        max_count = max(max_count,cnt)
print(max_count)