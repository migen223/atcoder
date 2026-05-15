#edgeは(頂点,頂点、重さ)の形式の辺が格納されてるリスト、nodesは頂点数
#O(頂点数^3)
def WF(edge,nodes):
    res=[[10**32]*nodes for i in range(nodes)]
    for i in range(nodes):
        res[i][i]=0
    for u,v,w in edge:
        res[u][v]=min(res[u][v],w)
        res[v][u]=min(res[v][u],w)
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                res[i][j]=min(res[i][j],res[i][k]+res[k][j])
    
    return res

n,m=map(int,input().split())
p=list(map(int,input().split()))
s,t=map(lambda x:int(x)-1,input().split())
edge=[]
for i in range(m):
    u,v,w=map(int,input().split())
    edge.append((u-1,v-1,w))

wf=WF(edge,n)

#bitDP https://atcoder.jp/contests/abc318/tasks/abc318_d
dp=[[-10**32]*(2**n) for _ in range(n)]
dp[s][0|(1<<s)]=p[s]

for i in range(2**n):
    for j in range(n):
        if dp[j][i]!=-10**32:
            for k in range(n):
                if not (i>>k)&1:
                    next=i|(1<<k)
                    dp[k][next]=max(dp[k][next],dp[j][i]+p[k]-wf[j][k])

ans=-10**32
for i in range(2**n):
    if (i>>s)&1:
        ans=max(ans,dp[t][i])
#print(dp)
print(ans)
"""
for i in range(2**n):
    if dp[i]!=-1:
        for j in range(n):
            if not (i>>j)&1: #(i>>j)&1 →j bit目がたっているかどうか
                for k in range(j+1,n):
                    if not (i>>k)&1:
                        next=i|(1<<j)|(1<<k) #i|(1<<j) →iのjbit目を立たせる
                        dp[next]=max(dp[next],dp[i]+edge[(j,k)])
                        ans=max(ans,dp[next])

3 3
10 20 30
1 3
1 2 5
2 3 5
1 3 25

"""
"""
for i in range(m):
    u,v,w=map(int,input().split())
    edge.append((u,v,w))

use=set()

for p in product([0,1],repeat=n):
    if p[s]==0 or p[t]==0:
        continue
    nodes=[]
    for i in range(n):
        if p[i]==1:
            nodes.append(i)
    uf=DSU(len(nodes))
    graph=[[] for i in range(len(nodes))]
    dic={}
    count=0
    for i in range(len(nodes)):
        dic[nodes[i]]=count
        count+=1
    nodes=set(nodes)
    
    for u,v,w in edge:
        if u in nodes and v in nodes:
            graph[dic[u]].append(dic[v])
"""