import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
#dy=[-1,1,0,0]
#dx=[0,0,-1,1]
dy=[-1,-1,-1,1,1,1,0,0]
dx=[-1,0,1,-1,0,1,-1,1]

h,w,k=mi()

dic={}
for _ in range(k):
    r,c=mi()
    r-=1
    c-=1
    if r not in dic:
        nd={}
        nd[c]=-1
        dic[r]=nd
    else:
        dic[r][c]=-1

def check(l):
    res=[0]*4
    if l[0]==0:
        res[0]+=1
    if l[2]==0:
        res[2]+=1
    if l[1]==h-1:
        res[1]+=1
    if l[3]==w-1:
        res[3]+=1
   # print(res)
    if res[0]*res[2]>0 or res[0]*res[1]>0 or res[1]*res[3]>0 or res[2]*res[3]>0 :
        return True
    return False

#print(dic)
for yi in dic:
    for xi in dic[yi]:
        if dic[yi][xi]==-1:
            minmax=[yi,yi,xi ,xi] #miny,maxy,minx,maxx
            v=[(yi,xi)]
            dic[yi][xi]=0
            while v:
                y,x=v.pop()
                for d in range(8):
                    ny=y+dy[d]
                    nx=x+dx[d]
                    if 0<=ny<=h-1 and 0<=nx<=w-1 :
                        if ny in dic and nx in dic[ny] and dic[ny][nx]==-1:
                            dic[ny][nx]=0
                            v.append((ny,nx))
                            minmax[0]=min(ny,minmax[0])
                            minmax[1]=max(ny,minmax[1])
                            minmax[2]=min(nx,minmax[2])
                            minmax[3]=max(nx,minmax[3])
            #print(minmax)
            #print(dic)
            if check(minmax):
                print("No")
                sys.exit()
print("Yes")
