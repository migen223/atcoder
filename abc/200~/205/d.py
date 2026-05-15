from bisect import bisect_right
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
c=[]
for i in range(n):
    c.append(a[i]-(i+1))

for i in range(q):
    k=int(input())
    ind=bisect_right(c,k-1)
    print(k+ind)


"""
a.sort()
a0=[0]
for i in range(n):
    a0.append(a[i])
gaps=[]
plus=[]
g=0
p=0
count=1
for i in range(n):
    if a0[i]+1==a0[i+1]:
        count+=1
        continue
    else:
        g+=a0[i+1]-a0[i]-1
        gaps.append(g)
        #print(p,a0[i],a0[i+1])
        plus.append(p)
        p+=count
        count=1
if count>1:
    plus.append(p+count)
if len(gaps)==len(plus):
    plus.append(p)
if len(gaps)!=0:
    gaps.append(gaps[-1]+count)
else:
    gaps=[0]
    plus=[0,count]


if gaps[0]!=0:
    """
"""
    plus=[0]
    p=0
    for i in range(len(gaps)-1):
        p+=gaps[i+1]-gaps[i]
        plus.append(p)
    print(gaps)
    print(plus)
    gaps.pop()
    """"""
    gaps.pop()
else:
    plus=[0,count-1]
print(gaps)
print(plus)
for i in range(q):
    k=int(input())
    ind=bisect_left(gaps,k)
    #print(f"{k}+{plus[ind]}")
    print(k+plus[ind])
"""



    

