n,r = map(int,input().split())
for i in range(1,r+1):
    if i%2==0:
        continue
    print(str(n)+" "+"x"+" " +str(i)+" " +"=" +" "+str(n*i))