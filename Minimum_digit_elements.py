def dc(n):
    cnt = 0
    while n>0:
        n//=10
        cnt+=1
    return cnt
n = int(input())
arr = list(map(int,input().split()))
d = dc(min(arr))
cnt = 0
for i in arr:
    if dc(i) == d:
        cnt+=1
print(cnt)