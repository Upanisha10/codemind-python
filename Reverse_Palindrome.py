def rev(n):
    rev = 0
    while n>0:
        r = n%10
        rev = rev*10+r
        n//=10
    return rev
def palindrome(n):
    if n == rev(n):
        return 1
    else:
        return 0
n = int(input())
res = n + rev(n)
while palindrome(res) != 1:
    res = res+rev(res)
print(res)