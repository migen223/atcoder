n,m=map(int,input().split())
a=list(map(int,input().split()))
cand=[0]*n
now=[-1,0]#人,票数

for i in range(m):
    cand[a[i]-1]+=1
    #print(cand,a[i])
    if now[1]<=cand[a[i]-1]:
        if now[1]==cand[a[i]-1]:
            now[0]=min(now[0],a[i]-1)
        else:
            now[0]=a[i]-1
        now[1]=cand[a[i]-1]
    print(now[0]+1)