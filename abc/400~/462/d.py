from collections import deque
n,d=map(int,input().split())

def C(n):
    return n*(n-1)//2
        
cand=[]
event=[]
end=[]
for i in range(n):
    s,t=map(int,input().split())
    cand.append((s,t))
    #event.append((s,0,i))
    event.append((t,2,i))
    end.append(t)
    if s+d<=t:
        event.append((s+d,1,i))
event.sort()
dq=deque(event)
flag=[0]*n
overd=0

ans=0
for i in range(max(end)+1):
    ban=[]
    while dq and dq[0][0]==i:
        t,e,p=dq.popleft()
        if e==1:
            flag[p]=1
            overd+=1
        elif e==2:
            if flag[p]==1:
                ban.append(p)
    ans+=C(overd)
    for b in ban:
        overd-=1
        flag[b]=0
    
    #print(ans,i)
print(ans)

"""
    event.append((s,i,0))
    event.append((t,i,1))

event.sort()

act=set([event[0][1]])
time=event[0][0]
ans=0
for  i in range(1,len(event)):
    t,p,io=event[i]
    #print(t,p,io,act,time)
    if t-time>=d and len(act)>=2:
        ans+=((t-time)-d+1)*C(len(act))
    if io==1:
        act.discard(p)
    else:
        act.add(p)
    
    #print(ans)
    time=t
print(ans)


"""