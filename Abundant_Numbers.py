def sum_fac(n):
    s = 0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    return s
n = int(input())
if sum_fac(n) > n:
    print("True")
else:
    print("False")