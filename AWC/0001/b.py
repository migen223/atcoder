
n,l,r=map(int,input().split())
p=list(map(int,input().split()))


ans=-1
cand=[]
for i in range(n):
    if l<=p[i]<=r:
        cand.append((p[i],-i))
if len(cand)>0:

    cand.sort()
    print(-cand[-1][1]+1)
else:
    print(-1)