import sys
n=int(input())


que1=[]
que2=[]
que=[]
for i in range(n):
    t,x=map(int,input().split())
    que.append((t,x))
    if t==1:
        que1.append(x)
    else:
        que2.append(x)
ans=[0]*(n)
imos=[0]*(n+1)
po={}
for i in set(que2):
    po[i]=[]


for i in range(n):
    t,x=que[i]
    if t==1:
        if x in po:
            po[x].append(i)
    elif t==2:
        if len(po[x])==0:
            print(-1)
            sys.exit()
        else:
            time=po[x].pop()
            imos[time]+=1
            ans[time]=1
            imos[i+1]-=1

k=0
ansl=[]
for i in range(1,n):
    imos[i]+=imos[i-1]
for i in range(n):
    if que[i][0]==1:
        ansl.append(ans[i])

print(max(imos))
print(*ansl)
        

"""
need=Counter(que2)
have={}
use={}
for i in need:
    have[i]=0
    use[i]=0

ans=[]
kmin=10**32
k=0
for i in range(n):
    t,x=que[i]
    if t==1 :
        if x in need:
            if have[x]<=need[x]:
                have[x]+=1
                k+=1

                ans.append(1)
            else:
                ans.append(0)
        else:
            ans.append(0)
    else:

        
    
"""