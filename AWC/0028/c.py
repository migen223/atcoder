
n=int(input())
p=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=0
c=[]
for i in range(n):
    ans+=a[i]-b[i]
    c.append(p[i]-b[i]-(a[i]-b[i]))

c.sort()
ans+=c[-1]
print(ans)