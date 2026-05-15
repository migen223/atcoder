import sys
n,m=map(int,input().split())
r=list(map(int,input().split()))
people=[(r[i],i) for i in range(n)]
people.sort()
pair=[[] for i in range(n)]

for i in range(m):
    u,v=map(lambda x:int(x)-1,input().split())
    pair[u].append(v)
    pair[v].append(u)
for i in range(n):
    pair[i].sort()

ban=[-1]*n
while people:
    now=people.pop()
    if ban[now[1]]!=-1 :
        continue
    #print(now)
    #print(pair[now[1]])
    for i in range(len(pair[now[1]])):
        #print("agufie",pair[now[1]])
        if ban[pair[now[1]][i]]==-1:
            p=pair[now[1]][i]
            ban[p]=now[1]
            ban[now[1]]=p
            break

print(ban[0]+1)

