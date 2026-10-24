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
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,q=mi()

col="a"
tile=[0]*n
end={}
keep={}

for _ in range(q):
    que=input().split()
    if que[0]=="1":
        x=int(que[1])-1
        if tile[x]==0:
            if x in keep:
                end[x]=keep[x]
                keep.pop(x)
            else:
                end[x]=col
            tile[x]=1
        else:   
            keep[x]=end[x]
            end.pop(x)
            tile[x]=0
    else:
        f+=1
        c=que[1]
        col=c
        keep={}

ans=[]
for i in range(n):
    if i in end :
        ans.append(end[i])
    elif i in keep :
        ans.append(keep[i])
    else:
        ans.append(col)
print("".join(ans))