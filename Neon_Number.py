n = int(input())
sq = n**2
l = []
while sq>0:
    r= sq%10
    l.append(r)
    sq//=10
if sum(l) == n:
    print("Neon Number")
else:
    print("Not Neon Number")
