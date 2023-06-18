def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
def dc(n):
    cnt = 0
    while n>0:
        cnt+=1
        n//=10
    return cnt
n,x= map(int,input().split())
dig = n%(pow(10,x))
dig1 = n//(pow(10,dc(n)-x))
print(abs(dig-dig1))