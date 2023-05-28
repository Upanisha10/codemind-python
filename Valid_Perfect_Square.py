t = int(input())
while t>0:
    n = int(input())
    s = n**0.5
    if int(s) == s:
        print("True")
    else:
        print("False")
    t-=1