from random import randint
import sys
from sortedcontainers import SortedList
from collections import defaultdict
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

for _ in range(100):
    n=randint(6,10)
    m=randint(3,n)
    k=randint(1,m)
    a=[1]*(n)
    #print(n,m,k)

    for i in range(n):
        a[i]=randint(1,10)
    #debug(a)
    sl=SortedList(a[:m])
    dic=defaultdict(int)
    su=sum(sl[:k])
    for i in sl[:k]:
        dic[i]+=1

    l1=[su]
    #print(su,end=" ")

    for i in range(n-m):
        if m==k:
            su-=a[i]
            su+=a[i+m]
            #print(su,end=" ")
            continue

        if a[i] in dic:
            dic[a[i]]-=1
            if dic[a[i]]==0:
                dic.pop(a[i])
            su-=a[i]
            sl.discard(a[i])
            c1=sl[k-1]
            c2=a[i+m]
            if c1>=c2:
                dic[c2]+=1
                su+=c2
            else:
                dic[c1]+=1
                su+=c1

        else:
            c1=sl[k-1]
            c2=a[i+m]
            if c1>=c2:
                dic[c2]+=1
                su+=c2
                dic[c1]-=1
                su-=c1
                if dic[c1]==0:
                    dic.pop(c1)
        sl.add(a[i+m])
        #print(dick,su,sl)
        l1.append(su)
        #print(su,end=" ")

    l=sorted(a[:m])
    su=sum(l[:k])
    l2=[su]
    #print(su,end=" ")

    for i in range(n-m):
        if m==k:
            su-=a[i]
            su+=a[i+m]
            #print(su,end=" ")
            continue
        l=[]
        for j in range(i+1,1+i+m):
            l.append(a[j])
        l.sort()
        #print(l)
        l2.append(sum(l[:k]))
        #print(sum(l[:k]),end=" ")
    
    if l1!=l2:
        print()
        print()
        debug(n,m,k)
        debug(a)
        debug(l1)
        debug(l2)
        debug(l)