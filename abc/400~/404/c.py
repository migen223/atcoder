import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visit=[0]*n

def check(g,start,v):
    if  not v[start]:
        v[start]=1
        for to in g[start]:
            check(g,to,v)

if n!=m:
    print("No")
else:
    count=0
    for i in range(n):
        if len(graph[i])==2:
            count+=1
    if count==n:
        check(graph,0,visit)          
        if sum(visit)==n:
            print("Yes")
        else:
            print("No")
        
    else:
        print("No")