from collections import deque
n=int(input())
dist=[[-1 for _ in range(n)] for _ in range(n)]
graph=[[] for _ in range(n)]
for  _ in range(n-1):
    u,v=map(lambda x:int(x)-1,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    v=deque([[i,0]])
    dist[i][i]=0
    while v:
        now,dep=v.popleft()
        for ne in graph[now]:
            if dist[i][ne]==-1:
                dist[i][ne]=dep+1 
                v.append((ne,dep+1))

se=set()
pair=[]
for i in range(n-1):
    for j in range(i+1,n):
        if dist[i][j]>2 and dist[i][j]%2==1:
            pair.append((i,j))
            se.add(i)
            se.add(j)


#print()
#print(se)
#print(pair)
ban=set()
if len(pair)%2==0:
    print("Second")
    while True:
        u,v=map(lambda x:int(x)-1,input().split())
        if u==-2:
            exit()
        ban.add((u,v))
        while pair[-1] in ban:
            pair.pop()
        u,v=pair.pop()
        ban.add((u,v))
        print(u+1,v+1)
else:
    print("First")
    while True:
        
        while pair[-1] in ban:
            pair.pop()
        u,v=pair.pop()
        ban.add((u,v))
        print(u+1,v+1)
        u,v=map(lambda x:int(x)-1,input().split())
        #print("iaf",u)
        if u==-2:
            exit()
        ban.add((u,v))


"""
6 
1 2
2 5
2 6
1 3
1 4

9
1 7
4 1
6 1
8 6
5 7
3 4
2 8
9 3
"""