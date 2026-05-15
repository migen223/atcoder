
n,l,r,t=map(int,input().split())

ans=-1
cand=[]
for i in range(n):
    p,s=map(int,input().split())
    if l<=p<=r and s>=t:
        cand.append((p,-s,i))

if len(cand)>0:
    cand.sort()

    print(cand[0][2]+1)
else:
    print(-1)
