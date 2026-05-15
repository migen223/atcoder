from bisect import bisect_left

#union-find
from collections import defaultdict,deque

#uf=DSU(n) nは要素数
class DSU():
    #コンストラクタ
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.mycount=n

#要素の根を返す
    def leader(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.leader(self.parents[x])
            return self.parents[x]

#結合
    def merge(self, x, y):
        x = self.leader(x)
        y = self.leader(y)

        if x == y:
            return
        self.mycount-=1

        if self.parents[x] > self.parents[y]:
            x, y = y, x


        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.leader(x)]

    def same(self, x, y):
        return self.leader(x) == self.leader(y)

#全ての素集合を返す
    def groups(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.leader(member)].append(member)
        return group_members

    def count(self):
        return self.mycount
    
n=int(input())
a=list(map(int,input().split()))
dic={}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=deque([i])
    else:
        dic[a[i]].append(i)

graph=[[] for i in range(n)]
rgraph=[[] for i in range(n)]
for i in range(n):
    now=a[i]
    if now+1 in dic:
        ind =bisect_left(dic[now+1],i)
        if ind==len(dic[now+1]):
            continue
        graph[i].append(dic[now+1][ind])
        rgraph[dic[now+1][ind]].append(i)

#print(graph)
#print(rgraph) 
ans=[1]*n
for i in range(n-1,-1,-1):
    for j in rgraph[i]:
        ans[j]+=ans[i]
print(max(ans))
    #print(i,dic)

"""
uf=DSU(n)
ans=0
for i in range(n):
    now=a[i]
    if now in dic:
        if dic[now][0]==i:
            dic[now].popleft()
            if len(dic[now])==0:
                dic.pop(now)
    if now+1 in dic:
        if i<dic[now+1][0]:
            nind=dic[now+1].popleft()
            uf.merge(i,nind)
            if len(dic[now+1])==0:
                dic.pop(now+1)
    ans=max(uf.size(i),ans)
    #print(i,dic)

print(ans)
"""
"""
use=set()
ans=0
for i in range(n):
    if i not in use:
        now=a[i]
        ind=dic[now][0]
        res=1
        use.add(i)
        while True:
            now+=1
            
            if now not in dic:
                ans=max(ans,res)
                break
            else:
                nind=bisect_left(dic[now],ind)
                if nind ==len(dic[now]) :
                    ans=max(ans,res)
                    break
                #print("nind",nind)
                
                ind=dic[now][nind]
                if ind in use:
                    ans=max(res,ans)
                    break
                use.add(ind)
                res+=1
            #print(now,ind,i)
    

print(ans)"""