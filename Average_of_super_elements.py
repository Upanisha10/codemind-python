n = int(input())
arr = list(map(int,input().split()))
l = []
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
if len(l) == 0:
    print("-1")
else:
    s = sum(l)
    avg = s/len(l)
    print("{:.2f}".format(avg))