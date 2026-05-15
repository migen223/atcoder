from collections import deque
n,m=map(int,input().split())

top={}
tube=[]
color={}
for i in range(1,n+1):
    color[i]=[]
    top[i]=0

for i in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    for j in range(k):
        color[a[j]].append(i)
    tube.append(deque(a))
    top[a[0]]+=1

outs=deque([])
out=0
for t in top:
    if top[t]==2:
        out+=2
        outs.append(t)

#print(tube)
#print(color)

while outs:
    now=outs.popleft()
    #print(color[now])
    for ind in color[now]:
        tube[ind].popleft()
        if len(tube[ind])>0:
            top[tube[ind][0]]+=1
            if top[tube[ind][0]]==2:
                outs.append(tube[ind][0])
                out+=2

if out==2*n:
    print("Yes")
else:
    print("No")
