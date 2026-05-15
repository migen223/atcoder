
n=int(input())
a=list(map(int,input().split()))

se=set(a)
setl=list(se)
setl.sort()
dic={}
dic2={}
for i in range(len(setl)):
    dic[setl[i]]=i
    dic2[i]=setl[i]

graph=[[] for i in range(len(setl))]
for i in range(n//2):
    if a[i]!=a[-1-i]:
        graph[dic[a[i]]].append(dic[a[-1-i]])
        graph[dic[a[-1-i]]].append(dic[a[i]])

visit=[0]*len(se)
ren=0
for i in range(len(se)):
    if visit[i]==0:
        visitable=[i]
        visit[i]=1
        ren+=1
        while visitable:
            now=visitable.pop()
            for j in range(len(graph[now])):
                if visit[graph[now][j]]==0:
                    visit[graph[now][j]]=1
                    visitable.append(graph[now][j])

print(len(se)-ren)
