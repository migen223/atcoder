from bisect import bisect_left
n,L=map(int,input().split())
k=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
a.append(L)

def check(n):

  nind=0
  for i in range(k):
    ind=bisect_left(a,n+a[nind])
    #print(nind,a[nind])
    if ind==len(a):
       #print(n,"F")
       return False
    nind=ind
  if L-a[nind]>=n:
     #print(n,nind,"T")
     return True
  else:
     #print(n,"F")
     return False
        
l=0
r=10**9+1

while (r-l)>1:
  mid=(r+l)//2
  if (check(mid)):
    l=mid
  else:
    r=mid

print(l)
