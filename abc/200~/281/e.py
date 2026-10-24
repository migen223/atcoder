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

n,m,k=mi()
a=li()
sl=SortedList(a[:m])
dic=defaultdict(int)
su=sum(sl[:k])
for i in sl[:k]:
    dic[i]+=1

print(su,end=" ")

for i in range(n-m):
    if m==k:
        su-=a[i]
        su+=a[i+m]
        print(su,end=" ")
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
        sl.discard(a[i])
    sl.add(a[i+m])
    #debug(dic,sl,su)
    print(su,end=" ")
print()

"""
l=sorted(a[:m])
su=sum(l[:k])

print(su,end=" ")

for i in range(n-m):
    if m==k:
        su-=a[i]
        su+=a[i+m]
        print(su,end=" ")
        continue
    l=[]
    for j in range(i+1,1+i+m):
        l.append(a[j])
    l.sort()
    #print(l)
    print(sum(l[:k]),end=" ")
print()
"""
"""
8 3 2
2 5 6 3 1 4 8 10

"""