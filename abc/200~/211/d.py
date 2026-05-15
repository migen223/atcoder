from collections import deque,Counter
n,m=map(int,input().split())
graph=[[] for i in range(n+1)] 
p=10**9+7
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

"""
visit=[-1]*(n+1)
visit[n]=0
visitable=deque([[n,0]])

while visitable:
    now=visitable.popleft()
    pos=now[0]
    depth=now[1]
    for i in range(len(graph[pos])):
        if visit[graph[pos][i]]==-1:
            visitable.append([graph[pos][i],depth+1])
            visit[graph[pos][i]]=depth+1
z"""

dp=[[10**9,0] for i in range(n+1)]  
dp[1]=[0,1]    #深さ,経路数

visit2=[-1]*(n+1)
visit2[1]=0
visitable=deque([[1,0]])
while visitable:
    now=visitable.popleft()
    pos=now[0]
    depth=now[1]
    for i in range(len(graph[pos])):
        if visit2[graph[pos][i]]==-1:
            visitable.append([graph[pos][i],depth+1])
            visit2[graph[pos][i]]=depth+1
            dp[graph[pos][i]]=[depth+1,dp[pos][1]]
        else:
            if dp[graph[pos][i]][0]==depth+1:
                dp[graph[pos][i]][1]+=dp[pos][1]
                dp[graph[pos][i]][1]%=p
    #print(dp)

if visit2[n]==-1:
    print(0)
else:
    print(dp[n][1])
#print(visit)
#print(visit2)



