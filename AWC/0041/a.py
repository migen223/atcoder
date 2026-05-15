
n,m=map(int,input().split())

pl=[]
for i in range(n):
    c,k=map(int,input().split())
    pl.append([c,k])

ans=0
for i in range(m):
    p=int(input())-1
    if pl[p][1]>=1:
        ans+=pl[p][0]
        pl[p][1]-=1

print(ans)

