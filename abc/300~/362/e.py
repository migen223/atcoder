import sys
from collections import Counter
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

n=ii()
a=li()
d=set()
for i in range(n):
    for j in range(n):
        d.add(a[i]-a[j])

ans=[0]*n
ans[0]=n
if n==1:
    print(1)
    sys.exit()
ans[1]=n*(n-1)//2
fact=[1,1,2]
for i in range(3,81):
    fact.append((fact[-1]*i)%mod)
def C(n,k):
    return (fact[n]*pow((fact[n-k]*fact[k])%mod,-1,mod))%mod

#長さが3以上のものだけ数える
def solve(d):
    global ans
    dic={a[0]:{1:1}} #[要素][長さ][個数]
    if d==0:
        c=Counter(a)
        for mc in c.most_common():
            if mc[1]>=3:
                for i in range(3,mc[1]+1):
                    ans[i-1]+=C(mc[1],i)
            else:
                break
        return
    for i in range(1,n):
        if a[i]-d in dic:
            if a[i] in dic:
                for di in dic[a[i]-d]:
                    if di+1 not in dic[a[i]]:
                        dic[a[i]][di+1]=dic[a[i]-d][di]
                        
                    else:
                        dic[a[i]][di+1]+=dic[a[i]-d][di]
                    dic[a[i]][di+1]%=mod
            else:
                dic[a[i]]={}
                for di in dic[a[i]-d]:
                    dic[a[i]][di+1]=dic[a[i]-d][di]
                    dic[a[i]][di+1]%=mod
        if a[i] in dic:
            if 1 in dic[a[i]]:
                dic[a[i]][1]+=1
            else:
                dic[a[i]][1]=1
        else:
            dic[a[i]]={1:1}
        #print(dic)
    for d in dic:
        for di in dic[d]:
            if di>=3:
                ans[di-1]+=dic[d][di]
                ans[di-1]%=mod
    #print(dic)
    #debug(d)

for i in d:
    solve(i)
print(*ans)