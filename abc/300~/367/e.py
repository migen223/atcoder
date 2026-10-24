import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,k=mi()
x=li()
a=li()
if k==0:
    print(*a)
    sys.exit()


s=format(k,'b')
db=[[0 for _ in range(n)] for _ in range(len(s))]
for i in range(n):
    db[0][i]=x[i]-1

for i in range(1,len(s)):
    for j in range(n):
        db[i][j]=db[i-1][db[i-1][j]]

#for i in range(len(s)):
#    debug(*db[i])


#debug(s)
ans=[]
for i in range(n):
    now=db[-1][i]
    for j in range(1,len(s)):
        if s[j]=="1":
            now=db[-j-1][now]
    ans.append(now)

for i in range(n):
    print(a[int(ans[i])],end=" ")
print()

"""
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i].append(x[i]-1)
#print(graph)
lse=set()
loops={}
vis=[-1]*n
enter=[[] for _ in range(n)] #各頂点ごとの[ループに入るまでの距離、入るループのインデックス]

for i in range(n):
    if  vis[i]==1:
        continue
    route=[i]
    ind=0
    se=set([i])
    vis[i]=1
    while ind<len(route):
        now=route[ind]
        for ne in graph[now]:
            if vis[ne]==-1:
                vis[ne]=1
                route.append(ne)
                ind+=1
                se.add(ne)
            elif vis[ne]==1 and ne in se:
                debug(route)
                loop=[]
                last=ne
                while last!=route[-1]:
                    loop.append(route.pop())
                loop.append(route.pop())
                loop.reverse()
                tl=tuple(loop)
                for i in range(len(loop)):
                    enter[loop[i]]=[0,i]
                    loops[loop[i]]=tl
                count=1
                while route:
                    i=route.pop()
                    enter[i]=[count,0]
                    loops[i]=tl
            else:
                count,d=enter[ne][0]+1,enter[ne][1]
                while route:
                    i=route.pop()
                    enter[i]=[count,d]
                    count+=1

#print(enter)
#print(loops)
ans=[-1]*n
for i in range(n):
    if enter[i][0]<k:

"""
"""
for i in range(k):
    na=[]
    for j in range(n):
        na.append(a[x[j]-1])
    a=na[::]
    print()
    print(*a," ",i)


7 10
5 2 6 3 1 4 6
1 2 3 5 7 9 11


4 1
3 4 1 2
4 3 2 1

"""