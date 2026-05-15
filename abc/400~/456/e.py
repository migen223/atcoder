import sys
sys.setrecursionlimit(10**7)
#seen finish は要素数nのbool配列
#nvが今の位置 pv が前の位置
#cycleには始点から検出したサイクルまでの頂点が入ってる
def dfs(graph ,nv ,pv):
    global cycle,seen,finish
    seen[nv]=True
    cycle.append(nv)
    for ne in graph[nv]:

        if finish[ne]:
            continue
        if seen[ne] and not finish[ne]:
            cycle.append(ne)
            return ne
        res=dfs(graph,ne,nv)
        if res is not False:
            return res
    
    finish[nv]=True
    cycle.pop()
    return False

t=int(input())


for _ in range(t):
    n,m=map(int,input().split())
    graph=[set() for i in range(n)]
    for _ in range(m):
        u,v=map(lambda x:int(x)-1,input().split())
        graph[u].add(v)
        graph[v].add(u)
    w=int(input())
    grid=[input() for i in range(n)]
    vac=[set() for i in range(w)]
    ngraph=[[] for _ in range(w*n)]
    cycle=[]
    seen=[False]*(w*n)
    finish=[False]*(w*n)
    for i in range(w):
        for j in range(n):
            seen[n*i+j]=False
            finish[n*i+j]=False
            if grid[j][i]=="o":
                vac[i].add(j)
            if i==0:
                graph[j].add(j)
            
    for i in range(w):
        v=vac[i]
        for s in v:
            for ne in graph[s]:
                if ne in vac[(i+1)%w]:
                    ngraph[n*i+s].append(n*((i+1)%w)+ne)
   # print("seen",seen)
    #print("g",graph)
    #print("ng",ngraph)
    #print(vac)
    f=0
    for s in vac[0]:
        if not seen[s]:
            #print("is",0,s)
            res=dfs(ngraph,s,-1)
            if res is not False:
                print("Yes")
                f+=1
                break
    if f==0:
        print("No")

        
