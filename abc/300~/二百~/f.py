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

graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=mi()
    u-=1
    v-=1
    graph[u].append(v)

def dfs(graph ,nv ,pv):
    global cycle,loop,seen,finish
    
    seen[nv]=True
    cycle.append(nv)
    #debug(nv,cycle,loop)
    for ne in graph[nv]:

        
        #print("ne",ne)
        if loop[ne]==1:
            while cycle:
                loop[cycle.pop()]=1
        if finish[ne]:
            continue
        
        if seen[ne] and not finish[ne]:
            #cycle.append(ne)
            while cycle:
                loop[cycle.pop()]=1
            #return ne
        if seen[ne]==0:
            dfs(graph,ne,nv)
        
    
    finish[nv]=True
    if cycle and cycle[-1]==nv:
        cycle.pop()
    return False



seen=[0]*n
finish=[0]*n
cycle=[]
loop=[0]*n

for  i in range(n):
    if finish[i]==0:
        dfs(graph,i,-1)
print(sum(loop))



"""
8 11
1 2
2 5
1 7
7 8
1 3
3 1
2 4
5 6
4 3
6 4
8 6

8 9
1 2
2 3
8 3
7 8
5 7
4 5
2 4
4 6
6 1
"""