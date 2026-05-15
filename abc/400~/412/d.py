from itertools import permutations


n,m=map(int,input().split())
graph=[set() for i in range(n+1)]
for _ in range(m):
    a,b=map(lambda x:int(x)-1,input().split())
    graph[a].add(b)
    graph[b].add(a)

ans=float('inf')

for p in permutations(range(n)):
    res=0
    need={}
    for i in range(n):
        need[p[i]]=set([p[i-1],p[(i+1)%n]])
    for i in range(n):
        res+=len(graph[p[i]]|need[p[i]])-len(graph[p[i]]&need[p[i]])
        """
        if p[i-1] in graph[p[i]]:
            minus+=1
        else:
            res+=1
            #graph[p[i-1]].add(p[i])
            #graph[p[i]].add(p[i-1])
        if p[(i+1)%n] in graph[p[i]]:
            minus=1
        else:
            res+=1
            #graph[p[(i+1)%n]].add(p[i])
            #graph[p[i]].add(p[(i+1)%n])
        """
    ans=min(ans,res//2)

if n>=6:
    for p in permutations(range(n)):
        res=0
        need={}
        cir1=[]
        cir2=[]
        for i in range(3):
            cir1.append(p[i])
        for i in range(3,n):
            cir2.append(p[i])
       # print(cir1,cir2)
        for i in range(3):
            need[cir1[i]]=set([cir1[i-1],cir1[(i+1)%3]])
        for i in range(n-3):
            need[cir2[i]]=set([cir2[i-1],cir2[(i+1)%(n-3)]])
        for i in range(n):
            res+=len(graph[p[i]]|need[p[i]])-len(graph[p[i]]&need[p[i]])
        #print(res,cir1,cir2,need)
        ans=min(res//2,ans)

if n==8:
    for p in permutations(range(n)):
        res=0
        need={}
        cir1=[]
        cir2=[]
        for i in range(4):
            cir1.append(p[i])
        for i in range(4,n):
            cir2.append(p[i])
        for i in range(4):
            need[cir1[i]]=set([cir1[i-1],cir1[(i+1)%4]])
        for i in range(4):
            need[cir2[i]]=set([cir2[i-1],cir2[(i+1)%4]])
        for i in range(n):
            res+=len(graph[p[i]]|need[p[i]])-len(graph[p[i]]&need[p[i]])
        ans=min(res//2,ans)


print(ans)