def sam(n):
    s = 0
    while n>0:
        r = n%10
        s += r
        n//=10
    return s
def dc(n):
    cnt = 0
    while n>0:
        n//=10
        cnt+=1
    return cnt
n = int(input())
res = sam(n)
while dc(res)>1:
    res = sam(res)
print(res)