n = int(input())
t = 0
for i in range(1,n//2+1):
    if n == i*(i+1):
        t = 1
        break
if t==0:
    print("NO")
else:
    print("YES")