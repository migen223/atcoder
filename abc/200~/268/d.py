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

string={}
rstring={}
su=0
for i in range(n):
    s=input()
    string[s]=i
    rstring[i]=s
    su+=len(s)

used=set()
for _ in range(m):
    t=input()
    used.add(t)
    """
    s=[]
    bar=0
    f=0
    for i in range(t):
        if t[i]=="_" and s :
            st="".join(s)
            if st in string:"""

             

maxbar=16-(su+n-1)
def make(s,l,bar):
    #debug(s,l,bar)
    if sum(l)==n:
        #print(s)
        ans=[]
        for si in s:
            if si >=0:
                ans.append(rstring[si])
            else:
                for i in range(-si):
                    ans.append("_")
        #debug(ans)
        ans="".join(ans)

        if ans not in used and len(ans)>=3:
            print(ans)
            exit()

    
    for i in range(n):
        if l[i]==0:
            if len(s)!=0:
                
                for b in range(bar):
                    s.append(-1-b)
                    s.append(i)
                    bar-=b
                    l[i]=1
                    make(s,l,bar)
                    bar+=b
                    l[i]=0
                    s.pop()
                    s.pop()
                if bar==0:
                    s.append(-1)
                    s.append(i)
                    l[i]=1
                    make(s,l,bar)
                    l[i]=0
                    s.pop()
                    s.pop()
                else:
                    s.append(-1-bar)
                    s.append(i)
                    tmp=bar
                    bar=0
                    l[i]=1
                    make(s,l,bar)
                    bar=tmp
                    l[i]=0
                    s.pop()
                    s.pop()
            else:
                s.append(i)
                l[i]=1
                make(s,l,bar)
                s.pop()
                l[i]=0

make([],[0]*n,maxbar)
print(-1)

"""
2 15
a
b
a_b
a__b
a___b
a____b
a_____b
a______b
a_______b
a________b
a_________b
a__________b
a___________b
a____________b
a_____________b
a______________b
b_a
b__a

"""