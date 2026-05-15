import sys
n,k=map(int,input().split())

def count(n):
    ys=str(n)
    for i in ys:
        n+=int(i)
    n%=10**5
    return n

if n!=0:
    graph=[[] for i in range(10**5)]

    for i in range(10**5):
        graph[i].append(count(i))

    vis=[-1]*(10**5)
    vis[n]=0
    v=[n]
    all=[]
    c=0
    while v:
        now=v.pop()
        all.append(now)
        c+=1
        for ne in graph[now]:
            if vis[ne]==-1:
                vis[ne]=c
                v.append(ne)
            else:
                s=ne
                v=[]
                break
    roop=[]
    for i in range(vis[s],len(all)):
        roop.append(all[i])
    #print(roop[0],roop[-1],len(roop),len(all))
    if 0<=k<len(all):
        print(all[k])
    else:
        print(roop[(k-(len(all)-len(roop)))%len(roop)])

else:
    print(0)