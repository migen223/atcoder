import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]
#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる

n,q=mi()
bits=[[-1 for _ in range(60)] for _ in range(n)]

que=[]
ma=-1
for _ in range(q):
    x,y,z,w=mi()
    w=bin(w)[2:]
    ma=max(ma,len(w))
    que.append([x-1,y-1,z-1,w])

for i  in range(q):
    que[i][-1]=que[i][-1].zfill(ma)

ans=1
#print(que)

for i in range(ma):
    res=0
    for j in range(2**n):
        f=0
        for k in range(q):
            x,y,z,w=que[k]
            #debug(((j>>x)&1),((j>>y)&1),((j>>z)&1),(j>>x)&1|((j>>y)&1)|((j>>z)&1),int(w[i]),bin(j)[2:],i)
            if (((j>>x)&1)|((j>>y)&1)|((j>>z)&1))!=int(w[i]):
                f+=1
                break
        if f==0:
            res+=1
    ans*=res
    ans%=mod
print(ans)




