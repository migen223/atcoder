from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)
x1,x2,x3=map(int,input().split())
mod=998244353

@lru_cache
def search(pre,l):
    res=0
    #print(now,l)
    if l[0]==l[1]==l[2]==0:
        return 1
    for i in [-1,0,1]:
        if 0<=pre+i<=2:
            if l[pre+i]>=1:
                #now.append(pre+i)
                nl=[l[0],l[1],l[2]]
                nl[pre+i]-=1
                res+=search(pre+i,tuple(nl))
                res%=mod
                #now.pop()
    #print(l)
    return res

ans=0
ans+=search(0,(x1-1,x2,x3))+search(1,(x1,x2-1,x3))+search(2,(x1,x2,x3-1))
ans%=mod
print(ans)