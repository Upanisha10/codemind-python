def sum_fac(n):
    s = 0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    return s
a = int(input())
b = int(input())
if a==sum_fac(b) and b==sum_fac(a):
    print("Amicable")
else:
    print("Not Amicable")