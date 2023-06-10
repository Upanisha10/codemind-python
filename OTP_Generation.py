s = input()
l=[]
for i in range(0,len(s)):
    if int(s[i])%2==0:
        continue
    else:
        sq = int(s[i])**2
        l.append(sq)
for i in l:
    print(i,end='')
        