def palindrome(n):
    rev = 0
    temp = n
    while n>0:
        r = n%10
        rev = rev*10+r
        n//=10
    if rev == temp:
        return 1
    else:
        return 0
a = int(input())
b = int(input())
for i in range(a,b+1):
    if palindrome(i):
        print(i,end=" ")