import sys
from itertools import permutations
n,m=map(int,input().split())

words=[input() for i in range(n)]
for p in permutations([i for i in range(n)],n):
    per=list(p)
    now=words[per[0]]
    f=0
    for i in range(1,n):
        count=0
        for j in range(m):
            if now[j]!=words[per[i]][j]:
                count+=1
        now=words[per[i]]
        if count!=1:
            f+=1
            break
    if f==0:
        print("Yes")
        sys.exit()
print("No")



"""
dic={}

for i in range(n):
    for j in range(n):
        if i!=j:
            count=0
            for k in range(m):
                if words[i][k]!=words[j][k]:
                    count+=1
            if count==1:
                next[i].append(j)

for i in range(n):
    visit=set()
    visitable=[[i,[False]*n]]
    ma=0
    while visitable:
        #print(visitable)
        now=visitable.pop()
        visit.add(now[0])
        now[1][now[0]]=True
        count=0
        for p in range(n):
            if now[1][p]:
                count+=1
        ma=max(ma,count)
        for j in next[now[0]]:
            if not now[1][j]:
                l=[]
                for q in range(n):
                    l.append(now[1][q])
                l[j]=True
                visitable.append([j,l])

    if ma==n:
        print("Yes")
        sys.exit()
print("No")
"""
            






