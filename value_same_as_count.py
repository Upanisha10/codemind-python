n = int(input())
arr = list(map(int,input().split()))
l = []
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
print(len(l))