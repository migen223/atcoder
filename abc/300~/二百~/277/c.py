import sys
n=int(input())
graph=[]
dic={}
se=set()

ma=0
for i in range(n):
    a,b=map(int,input().split())
    if a not in se:
        dic[a]=len(graph)
        se.add(a)
        graph.append([b])
    else:
        graph[dic[a]].append(b)
    if b not in se:
        dic[b]=len(graph)
        se.add(b)
        graph.append([a])
    else:
        graph[dic[b]].append(a)
    ma=max(a,b,ma)
"""
if 1 in se:
    ans=1
    visit=set()
    visitable=[[dic[1],1]]
    while visitable:
        now=visitable.pop()
        visit.add(now[0])
        ans=max(ans,now[1])
        if now[1]==ma:
            print(ma)
            sys.exit()
        for i in graph[now[0]]:
            if dic[i] not in visit:
                visitable.append([dic[i],i])
    print(ans)
else:
    print(1)
"""
    
if 1 in se:
    ans=1
    visit=set([dic[1]])
    visitable=[[dic[1],1]]
    while visitable:
        now=visitable.pop()
        ans=max(ans,now[1])
        if now[1]==ma:
            print(ma)
            sys.exit()
        for i in graph[now[0]]:
            if dic[i] not in visit:
                visitable.append([dic[i],i])
                visit.add(dic[i])
    print(ans)
else:
    print(1)
