n,m=map(int,input().split())
top=[]
for _ in range(n+1):
    top.append([])

for _ in range(m):
    a,b=map(int,input().split())
    top[a].append(b)
    top[b].append(a)
ans=0
#print(top)
for i in range(n+1):
    top[i].sort()
    if len(top[i])>1:
        if top[i][0]<i and top[i][1]>i:
            ans+=1
    elif len(top[i])==1:
        #print(top[i][0],i)
        if top[i][0]<i:
            ans+=1
print(ans)
