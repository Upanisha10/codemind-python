n = int(input())
arr = list(map(int,input().split()))
a = int(input())
s = 0
for i in range(0,a):
    s += arr[i]
print(s)