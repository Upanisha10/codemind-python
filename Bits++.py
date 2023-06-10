n = int(input())
x = 0
for i in range(1,n+1):
    s = input()
    for i in range(0,len(s)):
        if s[i] == '+' and s[i+1] == '+':
            x+=1
            break
        elif s[i] == '-' and s[i+1] == '-':
            x-=1
            break
print(x)