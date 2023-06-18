def reverse(n):
    rev = 0
    while n!=0:
        r = n%10
        rev = rev*10+r
        n//=10
    return rev
def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return 1
    else:
        return 0
n = int(input())
if prime(n) and prime(reverse(n)):
    print("circular prime")
elif prime(n) and prime(reverse(n)) == 0:
    print("prime but not a circular prime")
else:
    print("not prime")