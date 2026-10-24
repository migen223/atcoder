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
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]
#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる
a,b,c=mi()
pc=c.bit_count()
#print(pc)
#print(format(c,'b'))


if c==0:
    if a==b:
        x=0
        y=0
        for i in range(a):
            x|=(1<<i)
            y|=(1<<i)
        print(x,y)
    else:
        print(-1)
    sys.exit()
if a+b<pc:
    print(-1)
    sys.exit()

if abs(b-a)<=pc:
    x=0
    y=0
    #print(a,b)
    count=0
    onbit=[]
    offbit=[]
    for i in range(60):
        if (c>>i)&1:
            onbit.append(i)
        else:
            offbit.append(i)
    offbit.sort(reverse=True)
    #print(onbit)
    #print(offbit)
    for i in range(abs(b-a)):
        if a>b:
            x|=(1<<onbit.pop())
        else:
            y|=(1<<onbit.pop())
    pc-=abs(b-a)
    a,b=min(a,b),min(a,b)
    #print(x)
    if pc%2!=0:
        print(-1)
        sys.exit()
    #print(a,b,pc,len(onbit),onbit)
    for i in range(len(onbit)//2):
        x|=(1<<onbit.pop())
        y|=(1<<onbit.pop())
        a-=1
        b-=1
    #print(onbit,a,b)
    for i in range(a):
        if offbit:
            on=offbit.pop()
            x|=(1<<on)
            y|=(1<<on)
        else:
            print(-1)
            sys.exit()
    print(x,y)
    #print(format(x,'b'),format(y,'b'))
    debug(x.bit_count(),y.bit_count())
    debug(x>(2**60),y>(2**60))
    debug(x^y)
    
else:
    print(-1)


"""
530423800524412070
530423800524412070
1 59 1152921504606846975
58 58 1152921504606846975
"""