n,m = map(int,input().split())
a  = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
for i in a:
    if i not in b:
        l.append(i)
for i in b:
    if i not in a:
        l.append(i)
s = list(set(l))
print(len(s))