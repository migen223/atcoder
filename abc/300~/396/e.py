import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,m=mi()

graph=[[] for  i in range(n)]
for i in range(m):
    x,y,z=mi()
    x-=1
    y-=1
    graph[x].append((y,z))
    graph[y].append((x,z))

vis=[-1]*n

def dfs(start):
    global vis
    v=[start]
    path=[start]
    while v:
        now=v.pop()
        for ne,z in graph[now]:
            if vis[ne]==-1:
                vis[ne]=vis[now]^z
                path.append(ne)
                v.append(ne)
            else:
                if vis[ne]!=vis[now]^z:
                    print(-1)
                    sys.exit()
    return path
ans=[0]*n
for i in range(n):
    if vis[i]!=-1:
        continue
    vis[i]=0
    path=dfs(i)
    for j in range(30):
        on=0
        for pi in path:
            if (vis[pi]>>j)&1:
                on+=1
        if on<=len(path)-on:
            for pi in path:
                if (vis[pi]>>j)&1:
                    ans[pi]|=(1<<j)
        else:
            for pi in path:
                if not ((vis[pi]>>j)&1):
                    ans[pi]|=(1<<j)

print(*ans)

"""
k=len(format(maxz,'b'))
graph=[[] for i in range(n)]
for x,y,z in q:
    z=format(z, f"0{k}b")
    x-=1
    y-=1
    graph[x].append((y,z))
    graph[y].append((x,z))

ans=[-1]*n
def pair(i,st):
    if st=="1":
        if i==1:
            return 0
        else:
            return 1
    else:
        if i==1:
            return 1
        else:
            return 0
def check(a,b,st):
    return a^b==int(st)

def mini(l):
    if len(l)==1:
        return l[0]
    l1=l[0]
    l2=l[1]
    
    s1=0
    s2=0
    for  i in range(len(l1)):
        s1+=l1[i][1]
        s2+=l2[i][1]
    #print(l1,s1)
    #print(l2,s2)
    if s1>=s2:
        return l2
    return l1

ansn=[]
for i in range(k):
    vis=[[-1,-1] for _ in range(n)]
    ans=[-1]*n
    for j in range(n):
        if vis[j][0]==-1:
            res=[[[j,0]],[[j,1]]]
            vis[j]=[0,1]
            v=[[j,j]]
            while v:
                now,p=v.pop()
                flag=[0,0]
                for ne,st in graph[now]:
                    if vis[ne][0]==-1:
                        for l in range(2):
                            vis[ne][l]=pair(vis[now][l],st[i])
                            res[l].append([ne,vis[ne][l]])
                        v.append([ne,now])
                    elif ne!=p:
                        for l in range(2):
                            #print((vis[now][l],vis[ne][l],st[i]))
                            if not check(vis[now][l],vis[ne][l],st[i]):
                                #print(vis[now][l],vis[ne][l],st[i],now,ne)
                                #vis[now][l]=-1
                                flag[l]+=1
            #print(flag)
            #print(vis)
            l=[]
            if not flag[0]:
                l.append(res[0])
            if not flag[1]:
                l.append(res[1])
            if not l:
                print(-1)
                sys.exit()
            l=mini(l)
            for li in l:
                ans[li[0]]=li[1]
    ansn.append(ans)

a=[]

for i in range(n):
    ai=[]
    for j in range(k):
        ai.append(str(ansn[j][i]))
    #print("".join(ai))
    a.append(int("".join(ai),2))
print(*a)
        
            
                
                
    #print(vis)



    """
