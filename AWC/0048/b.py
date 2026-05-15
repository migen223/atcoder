
n=int(input())
h=list(map(int,input().split()))
d=list(map(int,input().split()))
ans=0
v=[0]
while v:
    now=v.pop()
    
    cand=[]
    if h[now]!=0 and d[now]!=0:
        ans+=1
    if now==n-1:
        break
    for i in range(1,3):
        ne=now+i
        if 0<=ne<=n-1:
            if h[ne]==0 or d[ne]==0:
                cand.append((1,ne))
            else:
                cand.append((0,ne))
    cand.sort()
    #print(cand)
    v.append(cand[-1][1])
print(ans)
