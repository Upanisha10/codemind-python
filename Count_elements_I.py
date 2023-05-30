n,m  = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
for i in a:
    if i in b and i not in l:
        l.append(i)
print(len(l))