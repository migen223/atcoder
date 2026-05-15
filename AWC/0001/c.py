
n,k=map(int,input().split())
d=list(map(int,input().split()))

d.sort()
for i in range(k):
    d.pop()
print(sum(d))