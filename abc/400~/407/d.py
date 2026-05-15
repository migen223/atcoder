import sys
sys.setrecursionlimit(10**7)

def xor(l):
    if len(l)==0:
        return 0
    ans=l[0]
    for i in range(1,len(l)):
        ans^=l[i]
    return ans
def totuple(ll):
    #print(tuple([tuple(ll[i]) for i in range(len(ll))]))
    return tuple([tuple(ll[i]) for i in range(len(ll))])

dy=[-1,1,0,0]
dx=[0,0,-1,1]

h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]  

syoki=[]
for i in range(h):
    for j in range(w):
        syoki.append(grid[i][j])
ans=xor(syoki)

check=[[0]*w for i in range(h)]
se=set()

def solve(cond):
    global ans,se
    now=[]
    for i in range(h):
        for j in range(w):
            if cond[i][j]==0:
                now.append(grid[i][j])
    ans=max(ans,xor(now))
    for i in range(h):
        for j in range(w):
            if cond[i][j]==0:
                for k in range(4):
                    ny=i+dy[k]
                    nx=j+dx[k]
                    if 0<=ny<=h-1 and 0<=nx<=w-1:
                        if cond[ny][nx]==0:
                            cond[ny][nx]=1
                            cond[i][j]=1
                            tu=totuple(cond)
                            if tu not in se:
                                solve(cond)
                                se.add(tu)
                            cond[ny][nx]=0
                            cond[i][j]=0
se.add(totuple(check))
solve(check)
print(ans)



