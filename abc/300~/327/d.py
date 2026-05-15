import sys
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def swap(n):
    if n==1:
        return 0
    else:
        return 1
    
graph=[[] for i in range(n+1)]
for i in range(m):
    if a[i]==b[i]:
        print("No")
        sys.exit()
    else:
        graph[a[i]].append(b[i])
        graph[b[i]].append(a[i])

visit=[-1]*(n+1)

for i in range(1,n+1):
    if visit[i]==-1:
        visitable=[(i,0)]
        visit[i]=0
        while visitable:
            pos,num=visitable.pop()
            for ne in graph[pos]:
                if visit[ne]==-1:
                    visit[ne]=swap(num)
                    visitable.append((ne,swap(num)))
                elif visit[ne]==num:
                    print("No")
                    sys.exit()

print("Yes")
#print(visit)
"""
for i in range(m):
    if visit[a[i]]==visit[b[i]]:
        print("No")
        sys,exit()
"""


