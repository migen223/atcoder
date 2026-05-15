from collections import deque
rt,ct,ra,ca=map(int,input().split())
n,m,l=map(int,input().split())
dy=[-1,1,0,0]
dx=[0,0,-1,1]
dir={"U":0,"D":1,"L":2,"R":3}

def count(rt,ct,dt,ra,ca,da,dl):
    if dt==da:
        if rt==ra and ct ==ca:
            return dl
        else:
            return 0
    dtx=dx[dir[dt]]
    dty=dy[dir[dt]]
    dax=dx[dir[da]]
    day=dy[dir[da]]
    if dty-day!=0 and dtx-dax!=0:
        if (rt-ra)%(day-dty)==0 and (ct-ca)%(dax-dtx)==0:
            if (rt-ra)//(day-dty)==(ct-ca)//(dax-dtx):
                x=(rt-ra)//(day-dty)
                if 1<=x<=dl:
                    return 1
    else:
        if dtx==dax==0:
            if ct==ca and (rt-ra)%(day-dty)==0:
                x=(rt-ra)//(day-dty)
                #print(x,rt,ra,ct,ca)
                if 1<=x<=dl:
                    return 1
        else:
            if rt==ra and (ct-ca)%(dax-dtx)==0:
                x=(ct-ca)//(dax-dtx)
                #print(x,rt,ra,ct,ca)
                if 1<=x<=dl:
                    return 1
    return 0
    
dal=deque([])
dtl=deque([])

for i in range(m):
    s,a=input().split()
    a=int(a)
    dtl.append([s,a])

for i in range(l):
    t,b=input().split()
    b=int(b)
    dal.append([t,b])

tak=[rt,ct]
aok=[ra,ca]
ans=0
while dtl and dal:
    da,xa=dal[0]
    dt,xt=dtl[0]
    dl=min(xt,xa)
    if xt>xa:
        dal.popleft()
        dtl[0][1]-=xa
    elif xa>xt:
        dtl.popleft()
        dal[0][1]-=xt
    else:
        dal.popleft()
        dtl.popleft()
    ans+=count(tak[0],tak[1],dt,aok[0],aok[1],da,dl)
    #print(count(tak[0],tak[1],dt,aok[0],aok[1],da,dl))
    tak[0]+=dy[dir[dt]]*dl
    tak[1]+=dx[dir[dt]]*dl
    aok[0]+=dy[dir[da]]*dl
    aok[1]+=dx[dir[da]]*dl
print(ans)


"""
td=deque([])
tp=deque([[rt,ct]])
tt=deque([0])
ad=deque([])
ap=deque([[ra,ca]])
at=deque([0])

for i in range(m):
    s,a=input().split()
    a=int(a)
    tp.append([tp[-1][0]+dy[dir[s]]*a,tp[-1][1]+dx[dir[s]]*a])
    td.append(s)
    tt.append(tt[-1]+a)
    

for i in range(l):
    t,b=input().split()
    b=int(b)
    ap.append([ap[-1][0]+dy[dir[t]]*b,ap[-1][1]+dx[dir[t]]*b])
    ad.append(s)
    at.append(at[-1]+b)

tp.popleft()
ap.popleft()
tt.popleft()
at.popleft()

ans=0
while tp:
    y,x=tp.popleft()
    nd=ad.popleft()
    t=tt.popleft()
    while ap and t>0:
        dt=at[0]-t
        if dt>=0:
            at[0]-=t

            if dt[0]==0:
                at.popleft()
                ay,ax=ap.popleft()
                d1=ad.popleft()
            else:
                ay,ax
"""