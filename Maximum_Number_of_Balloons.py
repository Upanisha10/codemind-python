s = input()
b = 0
a = 0
l = 0
o = 0
n = 0
for i in range(0,len(s)):
    if s[i] == 'b':
        b+=1
    elif s[i] == 'a':
        a+=1
    elif s[i] == 'l':
        l+=1
    elif s[i] == 'o':
        o+=1
    elif s[i] == 'n':
        n+=1
l//=2
o//=2
print(min(b,a,l,o,n))