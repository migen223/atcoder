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


n,m=mi()

wins=[]
cand=[]
win=[]
se=set()
ans=0
for _ in range(m):
    a,b=mi()
    wins.append(set([a,b]))
    win.append((a,b))
    se.add(a)
    se.add(b)
if len(se)==2:
    print(2*n-3)
    sys.exit()

check=set()
for i in range(2):
    one=win[0][i]
    two=-1
    next=[]
    restart=-1
    for j in range(1,m):
        if one not in wins[j]:
            next.append(win[j][0])
            next.append(win[j][1])
            restart=j+1
            break
    if not next:
        for x in range(n):
            if one==x:
                continue
            if (min(one,x),max(one,x)) not in check:
                ans+=1
                #debug("iaoef")
                check.add((min(one,x),max(one,x)))
        continue
    for two in next:
        if (min(one,two),max(one,two)) in check:
            continue 
        check.add((min(one,two),max(one,two)))
        f=0
        for k in range(restart,m):
            if one not in wins[k] and two not in wins[k]:
                f+=1
                break
        if f==0:
            ans+=1
            #debug(one,two)
print(ans)


"""
5 5
1 2
2 3
2 4
2 5
2 5



for a,b in win:
    if a not in se:
        se.add(a)
        cand.append(a)
    if b not in se:
        se.add(b)
        cand.append(b)
    if len(cand)>4:
        break

ans=0
for i in range(len(cand)-1):
    for j in range(i+1,len(cand)):
        a,b=cand[i],cand[j]
        f=0
        for k in range(m):
            if a not in wins[k] and b not in wins[k]:
                f+=1
                break
        if f==0:
            ans+=1
print(ans)
"""