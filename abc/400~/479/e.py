import sys
#BIT(フェネック木)　一点加算、区間取得
# 1-indexに注意
#https://qiita.com/iorn121/items/d3c24c4d4b014531b782

    

#双対BIT 区間加算、一点取得
class DBIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    #内部用 i番目以降にxを加算
    def _add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    #lからrまでにxを加算する
    def add(self, l, r, x):
        self._add(l, x)
        self._add(r + 1, -x)

    #i番目の値を求める
    def get(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    #初期設定 リストを渡してその値を埋め込む
    def setl(self,l):
        for i in range(len(l)):
            self.add(i+1,i+1,l[i])
        
    #値の設定　i番目の要素をxにする
    def set(self,i,x):
        now=self.get(i)
        self.add(i,i,x-now)

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n=ii()

edge={}
graph=[[] for _ in range(n)]
for i in range(1,n):
    a,b=mmi()
    edge[(a,b)]=i
    graph[a].append(b)
    graph[b].append(a)

bit=DBIT(n)
l=[]

v=[]
vis=[-1]*n

for i in range(n):
    if len(graph[i])==1:
        v.append(i)
        vis[i]=1
        root=i
        break

ngraph=[[] for _ in range(n)]
rgraph=[[] for _ in range(n)]
#print(v,vis)
while v:
    now=v.pop()
    l.append(now)
    #debug(now)
    for ne in graph[now]:
        
        if vis[ne]==-1:
            ngraph[now].append(ne)
            rgraph[ne].append(now)
            vis[ne]=1
            v.append(ne)
            #debug("ai",ne)

leaf=[]
count=[0]*n
sub=[0]*n
ma=[-1]*n
ind={}
rind={}

for i in range(n):
    if len(ngraph[i])==0:
        leaf.append(i)
    ind[l[i]]=i
    rind[i]=l[i]
    sub[i]=1
for i in range(len(leaf)):
    ma[leaf[i]]=ind[leaf[i]]


while leaf:
    now=leaf.pop()
    for ne in rgraph[now]:
        ma[ne]=max(ind[now],ma[ne],ma[now])
        #debug(ma[ne],ind[now],now,ne)
        count[ne]+=1
        sub[ne]+=sub[now]
        #debug(sub[now],now)
        if count[ne]==len(ngraph[ne]):
            leaf.append(ne)

#print(l)
#print(ma)
#print(root)
#print(sub)
#print(edge)

ans=[0]*n
v=[root]
while v:
    now=v.pop()
    for ne in ngraph[now]:
        i=edge[min(now,ne),max(now,ne)]
        if 2*sub[ne]>n:#この下が過半数
            bit.add(ind[ne]+1,ma[ne]+1,i)
        else:
            bit.add(1,n,i)
            bit.add(ind[ne]+1,ma[ne]+1,-i)
        v.append(ne)
        #debug(now,ne,ind[ne],ma[ne],i)
        #for i in range(1,n+1):
        #    print(bit.get(i),end=" ")
        #print()

for i in range(1,1+n):
    ans[rind[i-1]]=bit.get(i)

print(*ans)

"""
11
1 2
2 3
2 4
2 7
4 5
4 6
7 8
7 9
9 10
9 11

"""