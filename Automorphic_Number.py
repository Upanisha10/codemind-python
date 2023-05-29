def dc(n):
    cnt = 0
    while n>0:
        cnt+=1
        n//=10
    return cnt
n = int(input())
sq = n**2
dig = sq%(10**dc(n))
if dig == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")