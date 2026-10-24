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
#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる

on={}
n,q=mi()
maxbit=q.bit_length()

bit=[0]*maxbit

for _ in range(q):
    que=li()
    if que[0]==1:
        x=que[1]
        if x in on:
            for b in range(maxbit):
                if (on[x]>>b)&1:
                    bit[b]-=1
                if ((on[x]+1)>>b)&1:
                    bit[b]+=1
            on[x]+=1
        else:
            bit[0]+=1
            on[x]=1

    else:
        ban=[]
        for i in on:
            for b in range(maxbit):
                if (on[i]>>b)&1:
                    bit[b]-=1
                if ((on[i]-1)>>b)&1:
                    bit[b]+=1
            on[i]-=1
            if on[i]==0:
                ban.append(i)
        for bi in ban:
            on.pop(bi)
    ans=0
    for i in range(maxbit):
        ans+=(bit[i]%2)*pow(2,i)
    #debug(on)
    #debug(bit)
    #debug(ans)
    print(ans)