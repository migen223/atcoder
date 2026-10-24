import sys
from sortedcontainers import SortedList
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
l=[[i,i,i+1] for i in range(n)]
l.append([-1,-1,-1])
l.append([inf,inf,inf])
sl=SortedList(l)
dic={i:1 for i in range(1,n+1)}

for _ in range(q):
    que=li()
    if que[0]==1:
        _,x,c=que
        ind=sl.bisect([x-1,inf,inf])-1
        s,e,col=sl[ind]
        dic[col]-=(e-s)+1
        if c in dic:
            dic[c]+=(e-s)+1
        else:
            dic[c]=(e-s)+1
        if dic[col]==0:
            dic.pop(col)
        bef=sl[ind-1]
        aft=sl[ind+1]
        if bef[2]==c and aft[2]!=c:
            sl[ind-1][1]=e
            sl.discard([s,e,col])
        elif bef[2]!=c and aft[2]==c:
            sl[ind+1][0]=s
            sl.discard([s,e,col])
        elif bef[2]==aft[2]==c:
            sl[ind-1][1]=aft[1]
            sl.discard(aft)
            sl.discard([s,e,col])
        else:
            sl[ind][2]=c
    else:
        _,c=que
        if c in dic:
            print(dic[c])
        else:
            print(0)

    #for i in range(1,len(sl)-1):
     #   print(sl[i],end=" ")
    #print()

"""
6 5
1 3 2
1 5 4
1 4 2
1 3 3
2 3

"""