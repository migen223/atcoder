import sys

n,p,q,R=map(int,input().split())
a=list(map(int,input().split()))

pl=[]
ql=[]
rl=[]
l=0
r=0

now=a[0]
while r<n:
    if now<p:
        
        r+=1
        if r==n:
            break
        else:
            now+=a[r]
    elif now>p:
        now-=a[l]
        l+=1
        if l>r:
            r=l
    else:
        pl.append([l,r])
        now-=a[l]
        l+=1
    if l==r and r!=n:
        now=a[r]

now=a[0]
l=0
r=0
while r<n:
    if now<q:
        
        r+=1
        if r==n:
            break
        else:
            now+=a[r]
    elif now>q:
        now-=a[l]
        l+=1
        if l>r:
            r=l
    else:
        ql.append([l,r])
        now-=a[l]
        l+=1
    if l==r and r!=n:
        now=a[r]

now=a[0]
l=0
r=0
while r<n:
    if now<R:
        
        r+=1
        if r==n:
            break
        else:
            now+=a[r]
    elif now>R:
        now-=a[l]
        l+=1
        if l>r:
            r=l
    else:
        rl.append([l,r])
        now-=a[l]
        l+=1
    if l==r and r!=n:
        now=a[r]

"""
print(pl)
print(ql)
print(rl)
"""

dic={}
for i in range(len(ql)):
    dic[ql[i][0]]=ql[i][1]

qs=set()
rs=set()
for i in range(len(ql)):
    qs.add(ql[i][0])
for i in range(len(rl)):
    rs.add(rl[i][0])

for i in range(len(pl)):
    if pl[i][1]+1 in qs:
        if dic[pl[i][1]+1]+1 in rs:
            print("Yes")
            sys.exit()
print("No")