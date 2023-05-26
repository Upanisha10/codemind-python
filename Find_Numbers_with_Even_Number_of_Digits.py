def dc( n):
    cnt = 0
    while n>0:
        n//=10
        cnt +=1 
    return cnt

n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if dc(i)%2==0:
        cnt += 1
print(cnt)