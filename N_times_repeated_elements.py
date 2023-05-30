n = int(input())
arr = list(map(int,input().split()))
k = int(input())
l = []
for i in arr:
    if arr.count(i) == k and i not in l:
        l.append(i)
if len(l) == 0:
    print("-1")
else:
    for i in l:
        print(i,end=" ")