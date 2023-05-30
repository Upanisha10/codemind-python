s = input()
t = 0
l = []
for i in s:
    if i=='a'or i=='e' or i=='o' or i=='i' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        t = 1
        if i not in l:
            l.append(i)
for i in l:
    print(i,end=" ")
if t==0:
    print("-1")
